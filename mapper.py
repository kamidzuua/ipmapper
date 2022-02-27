import subprocess
from termcolor import colored
import ipaddress
import re

listFile = open("list.txt","r")
ipNets = listFile.read().split(' ')
count = len(ipNets)
for k in ipNets:
    ipList = []
    for ip in ipaddress.IPv4Network(k):
        ipList.append(ip)
    for i in range(0,255):    
        args = str(ipList[i])
        print(colored("executing","yellow")+colored(" nmap "+args,"green"))
        shell = subprocess.Popen(['nmap',args] ,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
        stdout, stderr = shell.communicate()
        while True:
            return_code = shell.poll()
            output = stdout
            print(killTime)
            downDetector = re.findall(r'Host seems down.',output)
            if bool(downDetector):
                print(colored(output.strip(),"red"))
            else:
                print(colored(output.strip(),"green"))
            if return_code is not None:
                break

listFile.close()
