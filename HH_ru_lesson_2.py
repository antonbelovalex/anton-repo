from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import re
import  json

main_link_hh = 'https://hh.ru'
main_link_sj = 'https://www.superjob.ru'

header = {'Accept': '*/*',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'
}

function_name = input('Введите интересующую вакансию----> ')
function_name_correct = function_name.replace(' ', '+')

parameter = {
    'text': function_name_correct,
    'search_period': "30" #1,3,7,30
}

session = requests.session()


def parse_hh(html):
    data = list()
    vacancys_block = html.find('div', {'class':'vacancy-serp'})
    pattern = re.compile('vacancy-serp-item')
    #vacancy_block = vacancys_block.findChildren('div', {'class': pattern}, recursive=False)
    vacance_block = html.find('div', {'class': 'vacancy-serp'})
    # vacancy_list = vacance_block.findChild(recursive=False)
    # print(vacance_block)

    for vacan in vacance_block:
        vacancy_date = {}
        vacancy_main_info = vacan.find('span', {'class': 'g-user-content'})
        if not vacancy_main_info == None:
            vacancy_name = vacancy_main_info.getText()
            print(vacancy_name)

        vacan_salary = vacan.find('span', {'data-qa': 'vacancy-serp__vacancy-compensation'})

        if not vacan_salary:
            salary_min = None
            salary_max = None
            salary_currency = None
            print(salary_min)
            print(salary_max)
            print(salary_currency)
        else:
            check_salary = vacan_salary.getText()
            check_salary = check_salary.split(' ', 1)[0]
            # print(check_salary)
            if check_salary == 'до':
                salary_min = None
                salary_max = vacan_salary.getText().split(' ', 1)[1]
                salary_currency = None
                print(salary_min)
                print(salary_max)
                print(salary_currency)
            elif check_salary == 'от':
                salary_min = vacan_salary.getText().split(' ', 1)[1]
                salary_max = None
                salary_currency = None
                print(salary_min)
                print(salary_max)
                print(salary_currency)
            else:
                salary_min = None
                salary_max = None
                salary_currency = vacan_salary.getText()
                print(salary_min)
                print(salary_max)
                print(salary_currency)

        # print(dict_)
        data.append(vacancy_date)
    return data


def parse_sj(html):
    data = list()
    vacancy_blocks = html.find('div', {'style': "display:block"})
    # print(vacancy_blocks)

    vacancy_block = vacancy_blocks.findChildren('div', {'class': '_3zucV _2GPIV f-test-vacancy-item i6-sc _3VcZr'},
                                                recursive=False)
    # print(vacancy_block)

    for vacancy in vacancy_block:
        dict_ = {}

        pattern_name = re.compile('icMQ_ _1QIBo .*')
        name_module = vacancy.find('a', {'class': pattern_name})
        dict_['name'] = name_module.text
        dict_['href'] = main_link_sj + name_module['href']

        pattern_company = re.compile('icMQ_ _205Zx .*')
        company_module = vacancy.find('a', {'class': pattern_company})
        if company_module:
            dict_['company'] = company_module.text
        else:
            dict_['company'] = None

        pattern_position = re.compile('_3mfro f-test-text-company-item-location.*')
        position_module = vacancy.find('span', {'class': pattern_position})
        if company_module:
            dict_['position'] = position_module.text
        else:
            dict_['position'] = None

        dict_['site'] = main_link_sj

        pattern_finance = re.compile('_3mfro _2Wp8I f-test-text-company-item-salary PlM3e _2JVkc _2VHxz')
        finance_module = vacancy.find('span', {'class': pattern_finance})
        finance = finance_module.text.replace('\xa0', ' ')
        # dict_['finance'] = finance
        if finance == 'По договорённости':
            dict_['finance_min'] = 'По договорённости'
            dict_['finance_max'] = 'По договорённости'
            dict_['valuta'] = 'no data'
        else:
            pattern_number = re.compile('[0-9]{1,3}\s{1}[0-9]{3}')
            pattren_valuta = re.compile('₽')
            pattren_ot = re.compile('от')
            pattren_do = re.compile('до')

            number = re.findall(pattern_number, finance)
            valuta = re.findall(pattren_valuta, finance)
            if valuta:
                valuta = valuta[0]
            if len(number) == 2:
                dict_['finance_min'] = number[0]
                dict_['finance_max'] = number[1]
                dict_['valuta'] = valuta
            elif len(number) == 1:
                ot = re.findall(pattren_ot, finance)
                do = re.findall(pattren_do, finance)
                if not do:
                    dict_['finance_min'] = number[0]
                    dict_['finance_max'] = '-'
                    dict_['valuta'] = valuta
                elif not ot:
                    dict_['finance_min'] = '-'
                    dict_['finance_max'] = number[0]
                    dict_['valuta'] = valuta

        # print(dict_)
        data.append(dict_)
    return data
def get_html_proxies(link, header):
    proxies = {
    "http": ""
}
    response = session.get(link, headers=header, proxies=proxies)
    # print(response.status_code)
    html = bs(response.text,'lxml')
    print(response.status_code)
    return html
def get_html(link, header):
    response = session.get(link, headers=header)
    # print(response.status_code)
    html = bs(response.text,'lxml')
    print(response.status_code)
    return html
def get_next_link_hh(html):
    bufer = html.find('a', {'class':"bloko-button HH-Pager-Controls-Next HH-Pager-Control"})
    if bufer:
        return main_link_hh + bufer['href']
        link = bufer['href']
    else:
        return ''
def get_next_link_sj(html):
    bufer = html.find('a', {'class':"icMQ_ _1_Cht _3ze9n f-test-button-dalshe f-test-link-Dalshe"})
    if bufer:
        return main_link_sj + bufer['href']
        link = bufer['href']
    else:
        return ''


result = list()
link = main_link_hh + f'/search/vacancy?search_period=30&salary=&st=searchVacancy&text={function_name_correct}'
# link = 'https://hh.ru/search/vacancy?L_is_autosearch=false&clusters=true&enable_snippets=true&search_period=30&text=Data+science&page=16'
while link:
    print(link)
    html = get_html(link, header)
    # html = get_html_proxies(link, header)
    result = result + parse_hh(html)
    link = get_next_link_hh(html)

link = main_link_sj + f'/vacancy/search/?keywords={function_name}&geo[c][0]=1'
while link:
    print(link)
    html = get_html(link, header)
    # html = get_html_proxies(link, header)
    result = result + parse_sj(html)
    link = ''
    link = get_next_link_sj(html)

with open("Lesson2_result.json", "w", encoding="utf-8") as file:
    json.dump(result, file)
