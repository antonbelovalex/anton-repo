from scrapingjob import ScrapingJob
from pprint import pprint

vacancy_db = ScrapingJob('mongodb://172.17.0.2:27017/', 'vacancy', 'vacancy_db')
vacancy_db.print_salary(300_000)
