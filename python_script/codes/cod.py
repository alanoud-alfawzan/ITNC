'''import xmltodict
import os


f=open('xml.xml').read()
xml_f=xmltodict.parse(f)

print(xml_f)





#==================================================================
switch_ip=open('ip.txt','r')
ip =switch_ip.readlines()

command_files=open('command.txt','r')
cc=command_files.readlines()

for switche in ip :
    ask=switche.strip()
    list_of_IP_adresses.append(ask)
for ccmm in cc :
    com=ccmm.strip()
    lisy_of_command.append(com)
#=============================================='''


#-------------------------------------------------------------#
# This script surve to pull information from the devices (Switches and Routers) and stor it in seperated file.
# 1- It will logging to device using ssh (username - password).
# 2- Take the files name from the user: 
#       - file contain the list of IP's.
#       - file contain the list fo commmand.
# 3- Run the command once for each ip.
# 4- Handling erorr.
# calculate the time current time.
# 5- Support diffrent type of Devices, just change the devie type depending on the devices you are working on.

#-------------------------------------------------------------#

from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import getpass
import datetime
#-------------------------------------------------------------#


#take the username & password 
now = datetime.datetime.now()
final_time=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')


User_name=input('User: \n')
Password= getpass.getpass('Password: ')


#-------------------------------------------------------------#
#to open files, readlines, store values as list, return the list
def open_file(f):
    list_of_swi=[]
    try:
        command_files=open(r'C:\Users\alfawzaf\python_script\\'+f,'r')
        cc=command_files.readlines()
    except NameError:
        print('file name error')
    for txt in cc:
        ask=txt.strip()
        list_of_swi.append(ask)
    return list_of_swi
#-------------------------------------------------------------#


#to check the extention of the input files, must end with .txt

def test_file_name(fn):
    
    g=fn[len(fn)-4: len(fn)]
    while g !='.txt':
        print('!!! WRONG !!! \n Please your file name must end with .txt extention')
        fn=input('Enter your file name again: \n')
        g=fn[len(fn)-4: len(fn)]
    return fn



#-------------------------------------------------------------#

# call the function to open the files come from the user 
try:
    fi =input ('Enter your file ip name end with .txt extension: \n').strip()
    after= test_file_name(fi)
    files=open_file(after)
    
except FileNotFoundError:
    print('the file not found pls try aginal ')
except NameError:
    print('file name error')
fc=input('Enter your file command name end with .txt extension:\n')
afte=test_file_name(fc)
file_c=open_file(afte)
#-------------------------------------------------------------#
#the old example of how to open files and readlines
'''
#==================================================================
switch_ip=open('ip.txt','r')
ip =switch_ip.readlines()

command_files=open('command.txt','r')
cc=command_files.readlines()

for switche in ip :
    ask=switche.strip()
    list_of_IP_adresses.append(ask)
for ccmm in cc :
    com=ccmm.strip()
    lisy_of_command.append(com)
#=============================================='''

#-------------------------------------------------------------#
# strat excuting, and connecting to the switches
for switches in files:
    print(' now will gother info from ip :'+switches)
    print(final_time)#print the current time 
    network_device={'host':switches,'username':User_name,'password':Password,'device_type':'cisco_ios'}#take info pass it to ConnectHandler 
    
    try:#if'username/password was wrong' erorr happen it will catched by the except

        connect_to_device=ConnectHandler(**network_device)
    except AuthenticationException:# if the 
        print("Authentication Failure"+switches)
        continue
    try:#if erorr 'authoristion' happen it will catched by the except
        connect_to_device.enable()      
    except SSHException:
        print("Not Authorised")
        continue

    # to save the output in .txt file / to show the result in CMD
    for command in file_c:
        output=connect_to_device.send_command(command)
        print(output)
        with open ('pull_from_Switches.txt','a') as f:
            f.write('\n')
            f.write(switches+'#'+command)
            f.write(connect_to_device.send_command(command))
            f.write('\n')



print('All done...\n Hope it was good')

'''i have to write small description for each function what was done on it '''



