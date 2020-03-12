from bs4 import BeautifulSoup as bs
import requests
import  re
from pprint import pprint

def parcer_hh(vacancy):



    main_link = 'https://hh.ru/search/vacancy'

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}

    params = {
        'text': vacancy,
        'search_field': 'name',
        'items_on_page': '100',
        'page': ''
    }

    html = requests.get(main_link, params=params, headers=headers)

    if html.ok:
        parsed_html = bs(html.text, 'lxml')

    vacance_block = parsed_html.find('div', {'class':'vacancy-serp'})
    #vacancy_list = vacance_block.findChild(recursive=False)
    #print(vacance_block)

    for vacan in vacance_block:
        vacancy_date = {}
        vacancy_main_info = vacan.find('span', {'class':'g-user-content'})
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
             #print(check_salary)
             if check_salary == 'до':
                salary_min = None
                salary_max = vacan_salary.getText().split(' ', 1)[1]
                salary_currency = None
                print(salary_min)
                print(salary_max)
                print(salary_currency)
             elif check_salary =='от':
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
parcer_hh('Python')