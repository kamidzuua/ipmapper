import subprocess
from termcolor import colored
import ipaddress
import re
import time
import _thread
import keyboard
import datetime

def totalIPcount(nets):
    listed = []
    for net in nets:
        if bool(net) is not False:
            for ip in ipaddress.IPv4Network(net):
                listed.append(ip)
    return len(listed)


def countETA(progress):
    global progressIPglobal
    timeIP = (time.time()-startTime)/progress
    ipLeft = ipTotal-progressIPglobal
    return str(datetime.timedelta(seconds=round((ipLeft/timeIP))))

def runIP(args,fileName): 
        print("["+colored("mapper.py","yellow")+"]["+colored("EXEC","yellow")+"]"+colored(" nmap "+args,"green"))
        shell = subprocess.Popen(['nmap',args] ,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
        try:
            stdout, stderr = shell.communicate(timeout=30)
        except:
            print("["+colored("SHELL","yellow")+"]["+colored(args,"yellow")+"]"+colored("BROKE DUE TO TIMEOUT","red"))
            #continue
        while True:
            return_code = shell.poll()
            output = stdout
            global progressIPglobal
            global openReg
            progressIPglobal+=1
            downDetector = re.findall(r'Host seems down.',output)
            if bool(downDetector):
                #print(colored(output.strip(),"red"))
                print("["+colored("NMAP","yellow")+"]["+colored(args,"yellow")+"]["+colored("HOSTERR","red")+"]")
            else:
                print("["+colored("OK","green")+"]["+colored(args,"yellow")+"]time taken for execution "+str(time.time()-subnetTime)+"s")
                #print(colored(output.strip(),"green"))
                findPort = re.findall(openReg,output)
                if bool(findPort): 
                    print("["+colored("NMAP","yellow")+"]["+colored(args,"yellow")+"]"+colored('Found '+mapPort+' here',"blue"))
                    outputFile.write(str(ipList[i])+" ")
            if return_code is not None:
                break


print(colored("Which port you are looking for?","yellow"))
mapPort = input()

if len(mapPort) == 2:
    openReg = r"%s/tcp   open" % mapPort
elif len(mapPort) ==3:
    openReg = r"%s/tcp  open" % mapPort
elif len(mapPort):
    openReg = r"%s/tcp open" % mapPort

startTime = time.time() 
fileName = "output"+mapPort+".txt"
listFile = open("list.txt","r")

ipNets = listFile.read().rstrip("\n").split(' ')
listFile.close()
ipTotal = totalIPcount(ipNets)
print("Total IP count: "+colored(ipTotal,"green"))
time.sleep(3)

outputFile = open(fileName,"w")
outputFile.close()
count = len(ipNets)
progress = 0
progressIPglobal = 1

for k in ipNets:
    outputFile = open(fileName,"w")
    progress+=1
    progressIP = 1
    subnetTime=time.time()
    ipList = []
    for ip in ipaddress.IPv4Network(k):
        ipList.append(ip)
    for i in range(0,len(ipList)):    
        args = str(ipList[i])
        try:
            _thread.start_new_thread(runIP,(args,fileName))
            print(colored(countETA(progressIPglobal),"green"))
        except:
            print(colored("THREAD ERROR","red"))
        time.sleep(0.1)
    time.sleep(5)
    print("------------------------")
    print("["+colored("mapper.py","yellow")+"]["+colored("PROGRESS","yellow")+"]" + colored(str(progress/count*100),"blue") + colored("%","blue"))
    print("["+colored("OK","green")+"]["+colored("SUBNET","yellow")+"]["+colored(k,"yellow")+"] "+str((time.time()-subnetTime)/60)+"m")
    print("------------------------")
    time.sleep(5)
    outputFile.close()
print("["+colored("OK","green")+"]["+colored("mapper.py","yellow")+"] time taken for execution "+str(time.time()-startTime)+"s")

outputFile.close()
