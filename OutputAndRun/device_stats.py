from GetIpFromFile import GetIpFromFile
from netmiko import ConnectHandler
from getpass import getpass
from AccessDevice import LoginDevice
import threading


Username = input("Enter Username: ")
Pwd = getpass("Enter Password: ")
IPList = GetIpFromFile() # This will return List of device's ip address
num = len(IPList)
DeviceDictList = [] # Each items in this list would be a dictionary containing netmiko needed parameter's
while num > 0:
    DeviceDictList.append({'device_type':'cisco_ios' , 'host':IPList[num - 1], 'username':Username, 'password':Pwd, 'secret' : 'test'})
    num = num - 1
## Till now we have created a dictionary with all the details ConnectHandler
## would need for each device import ipdb; ipdb.set_trace()
thread = []  # This is a list of thread's
n = 1
#print (DeviceDictList)

for elem in DeviceDictList:
    thread.append(threading.Thread(target = LoginDevice, name = "Thread" + str(n), args = [elem]))
    ## In the above we are using [elem] since elem is list and args will send its individual items
    ## to function as args refer's a list and pass its elements individually
    n = n + 1
for elemt in thread:        # Here we are starting each thread 1 by 1
    elemt.start()

## Try below if works faster

#thread[0].start()
#thread[1].start()
