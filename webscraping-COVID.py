# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
   
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

#<tr> = stands for table ROW
#<td> = stands for table COLUMN
table_rows = soup.findAll('tr')
#print(table_rows[2:20])


state_death_ratio = ""
state_best_testing  = ""
state_worst_testing = ""
high_death_ratio = 0.0
high_test_ratio = 0.0
low_test_ratio = 100.0

for row in table_rows[2:52]:
    td = row.findAll('td')
    #print(td)
    state = td[1].text.strip('\n')
    tot_cases = int(td[2].text.replace(",",""))
    tot_deaths = int(td[4].text.replace(",",""))
    tot_tested = int(td[10].text.replace(",",""))
    tot_pop = int(td[12].text.replace(",",""))

    #print("State:",state, "\nTotal Cases:",tot_cases, "\nTotal Deaths:",
           #tot_deaths, "\nTotal Tested:", tot_tested, "\nTotal Population:", tot_pop, "\n")
    
    death_ratio = tot_deaths/tot_cases
    test_ratio = tot_tested/tot_pop

    if death_ratio > high_death_ratio:
        high_death_ratio = death_ratio
        state_death_ratio = state
        
    if test_ratio > high_test_ratio:
        high_test_ratio = test_ratio
        state_best_testing = state

    if test_ratio < low_test_ratio:
        low_test_ratio = test_ratio
        state_worst_testing = state

    

print("\nHighest Death Ratio St.:", state_death_ratio,"=", format(high_death_ratio,".2%"))
print("Highest Test Ratio St.:", state_best_testing, "=", format(high_test_ratio,".2%"))
print("Worst Test Ratio St.:", state_worst_testing, "=", format(low_test_ratio,".2%"))









#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")


