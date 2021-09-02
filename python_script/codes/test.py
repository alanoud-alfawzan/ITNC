
from functools import cache
from os import truncate
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
import getpass
import datetime
import os
#-------------------------------------------------------------#


#take the username & password 
now = datetime.datetime.now()
final_time=now.strftime('%H:%M:%S on %A, %B the %dth, %Y')





#Open files, Readlines, Store values as list, Return the list
def open_files(user_file):

    try:
        open_files=open(r'C:\Users\alfawzaf\python_script\\'+user_file ,'r')
        read_file=open_files.readlines()
        for line in read_file:
            list_of_IP=[]
            list_of_IP.append(line.strip())
            return list_of_IP
    except FileNotFoundError:
        print('sorry the file was')
            
#-------------------------------------------------------------#
#to check the extention of the input files, must end with .txt

def test_file_extension(file_name):
    extension=file_name[len(file_name)-4: len(file_name)]
    while extension !='.txt':
        print('!!! WRONG !!! \n Please your file name must end with .txt extension')
        file_name=input('Enter your file name again: \n')
        extension=file_name[len(file_name)-4: len(file_name)]
    return file_name

#-------------------------------------------------------------#

# Call functions to pass user input 
IP_file =input ('Enter your file IP name end with .txt extension: \n').strip()
#call function, test the extension
IP_extension= test_file_extension(IP_file)
#call function, save the contant in list 
IP_list=open_files(IP_extension)

Command_file=input('Enter your file command name end with .txt extension:\n').strip()
#call function, test the extension
Command_extension=test_file_extension(Command_file)
#call function, save the contant in list 
Command_list=open_files(Command_extension)

print('alanous')