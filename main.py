import time
import threading
from termcolor import colored
from mapper import Mapper
mapPort = input(colored("Which port you are looking for?:","yellow"))


# openReg = f"/tcp {'' * len(mapPort)}"


startTime = time.time()
inputFile = 'list.txt'
fileName = "output"+mapPort+".txt"

mp = Mapper(mapPort, startTime, inputFile, fileName)
ipTotal, ipNets = mp.getIPinfo()
print("Total IP count: "+colored(ipTotal,"green"))
time.sleep(0.5)

count = len(ipNets)
progress = 0
progressIPglobal = 1

for k in ipNets:
    progress+=1
    progressIP = 1
    ipList = k
    for i,ip in enumerate(ipList):
        try:
            thread = threading.Thread(target=mp.runIP, args=((str(ip)), ))
            thread.start()
            print(colored(mp.countETA(ipTotal),"green"))  #class exemplar
        except:
            print(colored("THREAD ERROR","red"))
        # time.sleep(0.1)
    # time.sleep(5)
    print("------------------------")
    print("["+colored("mapper.py","yellow")+"]["+colored("PROGRESS","yellow")+"]" + colored(str(progress/count*100),"blue") + colored("%","blue"))
    print("------------------------")
    time.sleep(5)
print("["+colored("OK","green")+"]["+colored("mapper.py","yellow")+"] time taken for execution "+str(time.time()-startTime)+"s")

