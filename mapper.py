import subprocess
from termcolor import colored
import ipaddress
import re
import time
import _thread

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
            downDetector = re.findall(r'Host seems down.',output)
            if bool(downDetector):
                #print(colored(output.strip(),"red"))
                print("["+colored("NMAP","yellow")+"]["+colored(args,"yellow")+"]["+colored("HOSTERR","red")+"]")
            else:
                print("["+colored("OK","green")+"]["+colored(args,"yellow")+"]time taken for execution "+str(time.time()-subnetTime)+"s")
                #print(colored(output.strip(),"green"))
                findPort = re.findall(r"%s/tcp" % mapPort,output)
                if bool(findPort): 
                    print("["+colored("NMAP","yellow")+"]["+colored(args,"yellow")+"]"+colored('Found '+mapPort+' here',"blue"))
                    outputFile = open(fileName,"a")
                    outputFile.write(str(ipList[i])+" ")
                    outputFile.close()
            if return_code is not None:
                break



print(colored("Which port you are looking for?","yellow"))
mapPort = input()
startTime = time.time() 
fileName = "output"+mapPort+".txt"
listFile = open("list.txt","r")
ipNets = listFile.read().split(' ')
listFile.close()
outputFile = open(fileName,"w")
outputFile.close()
count = len(ipNets)
progress = 0

for k in ipNets:
    progress+=1
    progressIP = 0
    subnetTime=time.time()
    ipList = []
    for ip in ipaddress.IPv4Network(k):
        ipList.append(ip)
    for i in range(0,len(ipList)):    
        args = str(ipList[i])
        try:
            _thread.start_new_thread(runIP,(args,fileName))
        except:
            print(colored("THREAD ERROR","read"))
        time.sleep(0.33)
    time.sleep(5)
    print("------------------------")
    print("["+colored("mapper.py","yellow")+"]["+colored("PROGRESS","yellow")+"]" + colored(str(progress/count*100),"blue") + colored("%","blue"))
    print("["+colored("OK","green")+"]["+colored("SUBNET","yellow")+"]["+colored(k,"yellow")+"] "+str((time.time()-subnetTime)/60)+"m")
    print("------------------------")
    time.sleep(5) 
print("["+colored("OK","green")+"]["+colored("mapper.py","yellow")+"] time taken for execution "+str(time.time()-startTime)+"s")
