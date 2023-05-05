# pip install requests (to be able to get HTML pages and load them into Python)
# pip install bs4 (for beautifulsoup - python tool to parse HTML)


#from urllib.request import urlopen, Request
#from bs4 import BeautifulSoup


##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"



#url = 'https://www.worldometers.info/coronavirus/country/us'
# Request in case 404 Forbidden error
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
   
#req = Request(url, headers=headers)

#webpage = urlopen(req).read()

#soup = BeautifulSoup(webpage, 'html.parser')

#print(soup.title.text)

#<tr> = stands for table ROW
#<td> = stands for table COLUMN

#table_rows = soup.findAll('tr')
##########################################################################

#add required assignment header comment lines here

#Import Modules
import csv
import os

#Global Constants 
MEMBERSHIP_S_H = 'Membership_Service_Hours.csv'
BKUPFILE = 'Membership_hrs-BKUP.csv'
TEMPFILE = 'Membership_hrs-TEMP.csv'


#MAIN--------------------------------------------------------------------------------------
def main():

# Main Menu
    menu_choice = ''

    while menu_choice != 99:

       # Hard Coded Menu
        print('*'*60)
        print(format('Victorino Customer Data', '^60'))
        print()
        print('1 - View Member list')
        print('2 - Lookup a Member')
        print('3 - Enter new Service Event')
        print('4 - Update a Service Event')
        print('5 - Enter Service hours for an event')
        print('\n7- Copy customer data from BKUP (for testing only)')
        print('99 - Exit')
        print('*'*60)
        print()

        # Input Validation
        invalid_value = False
        while not invalid_value:
            #Prompt for menu selection
            menu_choice = input("\nEnter a menu choice: ")
            print('-'*50)
            
            print()
            
            #doesn't work with " "(blank space)
            if int(menu_choice) >= 1 and int(menu_choice) <= 5:
                invalid_value = True
            elif int(menu_choice) == 7:
                invalid_value = True
            elif int(menu_choice) == 99:
                invalid_value = True
            else:
                print('Invalid Choice, try again')


        # Menu Functions
        if menu_choice == '1':
            view_cust_list()
        elif menu_choice == '2':
            lookup_mem()
        elif menu_choice == '3':
            enter_new_event()
        elif menu_choice == '4':
            update_cust()
        elif menu_choice == '5':
            delete_cust()
        elif menu_choice == '7':
            restore()
        elif menu_choice == '99':
            print('Thank you for running the program. Have a great day!')
            break

        # Pause Processing    
        input('\nPress enter to continue...')
        


#FUNCTIONS---------------------------------------------------------------------------------
# Fn1--------------------------------------------------------------------------------------
def view_cust_list():
    print()
    print(format('*** Membership List ***', '^41'))
    print()
    print('    ', format('Last Name', '15'), format('First Name', '12'),format('Pledge Class', '13'))# \
     #   format('Service Hours', '10'))
    print('    ', format('-'*9, '15'), format('-'*9, '12'), format('-'*13, '1'))
    #open file for READING:
    infile = open(MEMBERSHIP_S_H, 'r', newline='')

    #create reader object
    reader = csv.reader(infile)

    #skip field names row
    next(reader)
 
    #Loop through reader
    i = 0
    for row in reader:
        #assign variable name
        l_name = row[0]
        f_name = row[1]
        pc = row[2]
        #ser_hrs = row[4]
        i += 1
        print('    ', format(l_name, '15'), format(f_name, '12'),format(pc, '13')) #\
        #format(ser_hrs, '10'))
    print()
    print('     >>> Total Members:', i)

    infile.close()

# Fn2--------------------------------------------------------------------------------------
def lookup_mem():   
    infile = open(MEMBERSHIP_S_H, 'r', newline='')
    #create reader object
    reader = csv.reader(infile)
    #skip field names row
    next(reader)

    print()
    print(format('*** Lookup Member ***', '^41'))
    print()
    search_id = input("    Enter a Member's Last Name: ").title()
    print()
    
    found = False
 
    for row in reader:
        l_name = row[0]
        f_name = row[1]
        pc = row[2]

        if l_name == search_id:
            found = True
            print('    Last Name:   ', l_name)
            print('    First Name: ', f_name)
            print('    Pledge Class:', pc)
            break

    if not found:
        print('Member not found.')

    infile.close()

# Fn3--------------------------------------------------------------------------------------
def enter_new_event():
    outfile = open(MEMBERSHIP_S_H, 'a', newline='')
    writer = csv.writer(outfile, delimiter = ',')

    print()
    print(format('*** Enter Service Event ***', '^41'))
    print()
    event = input('    Enter Event Name:  ')



    if event == '':
        print('\n     STATUS: No value was entered. Record was not saved')
    else:
        new_col = [event]
        writer.writerow(new_col)
        print('\n     STATUS: Event ' + event + ' saved!')

    #Close the file
    outfile.close()        


# Fn4--------------------------------------------------------------------------------------
def update_cust():
    print()
    print(format('*** Update Customer ***', '^41'))
    print()

    found = False
    
    #Open files 
    infile = open(CUSTFILE, 'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')
       
    #Create reader & writer objects
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter = ',')

    #Read & write field names
    fieldnames = next(reader)
    writer.writerow(fieldnames)
 
    search_id = input('    Enter a customer ID: ')
    print()
    print('    Enter new values (or press enter to skip')
    print('     ','-'*50)
    for row in reader:
        cust_id = row[0]
        l_name = row[1]
        f_name = row[2]
        if search_id == cust_id:
            found = True
            new_cust_id = input('Enter new custoemr id: ')
            new_l_name = input('Enter new last name:   ')
            new_f_name = input('Enter new first name:  ')
            if new_cust_id == '':
                new_cust_id = cust_id
            else:
                new_cust_id
            if new_l_name == '':
                new_l_name = l_name
            else:
                new_l_name
            if new_f_name == '':
                new_f_name = f_name
            else:
                new_f_name
            
            new_row = [new_cust_id, new_l_name, new_f_name]
            writer.writerow(new_row)
        else:
            writer.writerow(row)

    if found:
        print('STATUS: Customer ' + search_id + ' updated!')
        print()
    else:
        print('Customer ID not found')

    infile.close()
    outfile.close()

    os.remove(CUSTFILE)
    os.rename(TEMPFILE, CUSTFILE)

# Fn5--------------------------------------------------------------------------------------
def delete_cust():
    print()
    print(format('*** Update Customer ***', '^41'))
    print()

    found = False

    infile = open(CUSTFILE, 'r', newline='')
    outfile = open(TEMPFILE, 'w', newline='')

    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter = ',')

    fieldnames = next(reader)
    writer.writerow(fieldnames)

    search_id = input('    Enter a customer ID: ')
    
    for row in reader:
        cust_id = row[0]
        l_name = row[1]
        f_name = row[2]

        if cust_id == search_id:
            found = True
            print()
            print(format('Customer record found', '>26'))
            print('    ', '-'*30)
            print('    ', 'Customer ID: ', cust_id)
            print('    ', 'Last name: ', l_name)
            print('    ', 'First name: ', f_name)
        else:
            writer.writerow(row)
    if found:
        confirm = input('Are you sure you want to delete (y/n) ').lower()
        if confirm == 'y':
            print('STATUS: Customer 101 deleted!')
            print()
    else:
        print()
        print('    Customer ID no found')
        print()
    
    infile.close()
    outfile.close()

    os.remove(CUSTFILE)
    os.rename(TEMPFILE, CUSTFILE)

# Fn7--------------------------------------------------------------------------------------
def restore():
    from shutil import copyfile
    copyfile(BKUPFILE, CUSTFILE)
    print('You data was recovered from the backup file.')

#Call main() here--------------------------------------------------------------------------
main()
