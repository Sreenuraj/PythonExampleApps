import time
from datetime import datetime as dt

# variable containing the hostfile
host_file = 'test_hosts'
# where to redirect
redirect = '127.0.0.1'
# A list of websites to block
website = ['www.gmail.com','www.facebook.com']

# put the logic in a never ending loop
while True:
    # check the currnt time and have a logical if loop to check if time is insde
    # the working hours (11am to 16pm)
    if dt.now().hour >= 13 and dt.now().hour <= 16:
        print ('Working hours...')
        # open the host file and read the file to content
        with open(host_file, 'r+') as file:
            content = file.read()
            # check if the websites in the host_file
            for eachsite in website:
                if eachsite in content:
                    # nothing to be done
                    pass
                else:
                    # insert the entries into the host file
                    file.write(redirect + ' ' + eachsite +'\n')
    # if it is not the working hours
    else:
        print('fun hours....')
        # open the the host file and read the lines as a list to content
        with open(host_file, 'r+') as file:
            content = file.readlines()
            # file.seek method to go to the first line of the file
            file.seek(0)
            # Loop through the content
            for eachline in content:
                # check if the websites not in the line read
                if not any(eachwebsite in eachline for eachwebsite in website):
                    # write that line
                    file.write(eachline)
            # truncate the remaining
            file.truncate()
    # check every 5 sec
    time.sleep(5)
