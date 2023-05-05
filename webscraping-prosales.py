
import requests
import selenium
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


url = 'https://www.careershift.com/App/Contacts/SearchDetails?personId=1495139144'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
   
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)



prospectInfo = soup.findAll("h1", class_="title")
print(prospectInfo)

#session = requests.Session()

#Look up selenium for login part
#login_url = 'https://www.careershift.com/login'
#crape_url = 'https://www.careershift.com/search/jobs'

#login_payload = {
#    'username': 'reece_modisette1@baylor.edu',
#    'password': 'MarineCorp2024!'
#}

#session.post(login_url, data=login_payload)

#response = session.get(scrape_url)

#soup = BeautifulSoup(response.text, 'lxml')

#job_list = soup.find_all('div', {'class': 'job-results'})[0]

#for job in job_list.find_all('div', {'class': 'job-title'}):
#    print(job.text.strip())