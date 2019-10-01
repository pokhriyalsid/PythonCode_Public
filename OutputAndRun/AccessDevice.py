from netmiko import ConnectHandler
import netmiko   ## Netmiko needs to be imported to catch exception
                 ## netmiko.ssh_exception.NetMikoAuthenticationException
                 ## Else it wont recognize netmiko

import os
import time
import sys

filewithcmd = open("cmd.txt")
#outputfile = open("output.txt", 'a+')
cmdlist = filewithcmd.readlines()
filewithcmd.close()
#output = []
x = time.asctime()    # x is a string object returned
timestring = x.split()

def LoginDevice(dict):
    try:
        net_connect = ConnectHandler(**dict) # This will pass all items of List which in this case
                                             # are dict items

#        net_connect.send_command("terminal length 0") ## This command is automatically sent
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print ("Wrong Credentials entered for {}".format(dict['host']))
        sys.exit()
    try :
        os.mkdir(dict['host']) ## This will create a folder with name of the Router
                               ## This code is under try to catch exception if folder already exists
    except FileExistsError:
        pass
    path = dict['host'] + "\\" + dict['host'] + "_" + timestring[2] + "_" + timestring[1] + "_" +  timestring[3].split(':')[0] + "Hour" + "_" + "output.txt"
    pathrun = dict['host'] + "\\" + dict['host'] + "_" + timestring[2] + "_" + timestring[1] + "_" +  timestring[3].split(':')[0] + "Hour" + "_" + "run.txt"
    outputfile = open(path, 'a+')
    for cmd in cmdlist:
        print (cmd, file = outputfile, end = '')
        output = net_connect.send_command(cmd)
        outputfile.write(output)
        print ( "\n", file = outputfile)
        print ( "_"*20, file = outputfile)
    cmd1 = "show runn"
    #net_connect.send_command("\n")
    Runconfig = net_connect.send_command(cmd1)
    #Runconfig = net_connect.send_command("show history")
    with open(pathrun, 'w') as runconfig:
        runconfig.write(Runconfig)


#outputfile.close()
