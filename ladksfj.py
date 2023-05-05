from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.careershift.com/App/Contacts/SearchDetails?personId=1495139144'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

# Send HTTP request to the URL and get the HTML content
req = Request(url, headers=headers)
webpage = urlopen(req).read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(webpage, 'html.parser')

# Locate the HTML element containing the person's title using the class or id attribute
title_element = soup.findAll('h3')#, {'class': 'contact-job-title'})
print(title_element)
# Extract the text of the HTML element containing the person's title
#title = title_element.text.strip()

# Print the extracted title
#print('Person\'s title:', title)
