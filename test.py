import requests
from bs4 import BeautifulSoup

site = requests.get('https://moodle-2019-2020.fullerton.edu/grade/report/overview/index.php')
soup = BeautifulSoup(site.content, 'lxml')
print(soup.prettify())




'''page = requests.get('https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia')
soup = BeautifulSoup(page.content, 'lxml')
results = soup.find(id='ResultsContainer')

python_jobs = results.find_all('h2', 
                                string=lambda text: 'analyst' in text.lower())
for pyjobs in python_jobs:
    link = pyjobs.find('a')['href']
    print(pyjobs.text.strip())
    print(link)


job_elems = results.find_all('section', class_='card-content')
for job_elem in job_elems:
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()'''