import subprocess
from termcolor import colored
import ipaddress
import re

print(colored("Which port you are looking for?","yellow"))
mapPort = input()

listFile = open("list.txt","r")
ipNets = listFile.read().split(' ')
listFile.close()
outputFile = open("output.txt","w")
outputFile.close()
count = len(ipNets)
for k in ipNets:
    ipList = []
    for ip in ipaddress.IPv4Network(k):
        ipList.append(ip)
    for i in range(0,255):    
        args = str(ipList[i])
        print(colored("executing","yellow")+colored(" nmap "+args,"green"))
        shell = subprocess.Popen(['nmap',args] ,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
        try:
            stdout, stderr = shell.communicate(timeout=30)
        except:
            print(colored("BROKE DUE TO TIMEOUT","yellow"))
            continue
        while True:
            return_code = shell.poll()
            output = stdout
            downDetector = re.findall(r'Host seems down.',output)
            if bool(downDetector):
                print(colored(output.strip(),"red"))
            else:
                print(colored(output.strip(),"green"))
                findPort = re.findall(r"%s/tcp" % mapPort,output)
                if bool(findPort): 
                    print(colored('Found '+mapPort+' here',"blue"))
                    outputFile = open("output.txt","a")
                    outputFile.write(str(ipList[i])+" ")
                    outputFile.close()
            if return_code is not None:
                break

