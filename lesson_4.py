import requests
from lxml import html

def get_html(url):
  header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
  }

  response = requests.get(
    url,
    headers = header
  ).text

  return html.fromstring(response)

#-------------------------------------------------------
#Парсинг лентару
from get_html import get_html

main_link = 'https://lenta.ru/'

def get_date(url):
  tree = get_html(url)
  dates = tree.xpath("//time[@class='g-date']/@datetime")
  return dates[0] if dates else None

def get_lenta_data(links):
  output = []
  for link in links:
    href = link.xpath('./@href')[0]
    href = href if href.find('http') != -1 else main_link + href[1:]

    data = {
      'href': href,
      'title': link.xpath('./text()')[0],
      'date': get_date(href),
      'newsmaker': 'lenta'
    }

    output.append(data)

  return output
#-------------------------------------------------------
#Парсинг майл
from get_html import get_html

def get_date(url):
  tree = get_html(url)
  dates = tree.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
  return dates[0] if dates else None

def get_mail_data(links, url):
  output = []
  for link in links:
    href = link.xpath('./@href')[0]
    href = href if href.find('http') != -1 else url + href[1:]

    data = {
      'href': href,
      'title': link.xpath('./text()')[0] if link.xpath('./text()') else link.xpath('./span/text()')[0],
      'datetime': get_date(href),
      'newsmaker': 'mail'
    }

    output.append(data)

  return output
#-------------------------------------------------------
#Парсинг яндекса 
from get_html import get_html

main_link = 'https://yandex.ru/'

def get_date(url):
  tree = get_html(url)
  dates = tree.xpath("//time[@class='g-date']/@datetime")
  return dates[0] if dates else None

def get_yandex_data(links):
  output = []
  for link in links:
    href = link.xpath('./@href')[0]
    href = href if href and href.find('http') != -1 else main_link + href[1:]

    data = {
      'href': href,
      'title': link.xpath('./text()')[0],
      'datetime': None,
      'newsmaker': 'yandex'
    }

    output.append(data)

  return output
#-------------------------------------------------------
#Главная
from pprint import pprint

from HW_03.Mongo import Mongo
mongo = Mongo('news')

from get_html import get_html
from get_mail_data import get_mail_data
from get_lenta_data import get_lenta_data
from get_yandex_data import get_yandex_data

newsmaker_links = {
  'mail': 'https://news.mail.ru/',
  'lenta': 'https://lenta.ru/parts/news/',
  'yandex': 'https://yandex.ru/news/'
}

def get_links(html, newsmaker):
  match = {
    'mail': "//a[@class='list__text']|//a[contains(@class, 'newsitem__title')]|//a[contains(@class, 'link link_flex')]",
    'lenta': "//h3/a|//div[@class='item']/a",
    'yandex': "//h2[@class='story__title']/a"
  }

  return html.xpath(match[newsmaker])

def get_data(links, newsmaker):
  result = None
  if newsmaker == 'mail':
    result = get_mail_data(links, newsmaker_links[newsmaker])
  elif newsmaker == 'lenta':
    result = get_lenta_data(links)
  elif newsmaker == 'yandex':
    result = get_yandex_data(links)

  return result


result = []
for key in newsmaker_links:
  tree = get_html(newsmaker_links[key])
  links = get_links(tree, key)

  result.extend(get_data(links, key))

mongo.set_many(result)
pprint(result)
