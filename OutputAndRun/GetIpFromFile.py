def GetIpFromFile():
    with open("DeviceList.txt") as DeviceList:
        abc = DeviceList.readlines()
        NoOfDevice = len(abc)
        #print (NoOfDevice)
        #print (abc[NoOfDevice - 1].split()[-1])
        DeviceIP = []
        while NoOfDevice > 0:
            DeviceIP.append(abc[NoOfDevice - 1].split()[-1]) # This pulls out the ip address the rows of
                                                             # DeviceList.txt
            NoOfDevice = NoOfDevice - 1
            #print (DeviceIP[NoOfDevice - 1]
        return DeviceIP
