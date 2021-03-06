"""
declare imports
"""
import time
import subprocess
import ipaddress
import re
import datetime
from termcolor import colored


class Mapper:

    def __init__(self, mapPort, startTime, inputFile, outputFile):
        self.inputFile = inputFile
        self.startTime = startTime
        self.outputFile = outputFile
        self.mapPort = mapPort
        self.openReg = self.__getOpenReg(mapPort)
        self.progressIPglobal = 0
        self.ipList = []
        self.speedAVG = 25.6

    def getIPinfo(self):
        """
        define totalIPcount function
        returns total number of IPs through all subnets
        """
        with open(self.inputFile, 'r') as f:
            ipNets = f.read().rstrip("\n").split(' ')
        ipNets = [[ip for ip in ipaddress.IPv4Network(net)] for net in ipNets]
        ipTotal = sum([len(net) for net in ipNets])
        return ipTotal, ipNets

    def countETA(self, ipTotal):
        """
        define countETA function
        returns estimated processing time
        t=S/v
        calculating based on speedAVG property(base=25.6)
        """
        #timeIP = 25.6
        DEATHadder = self.progressIPglobal/(time.time() - self.startTime)
        self.speedAVG = round(DEATHadder+self.speedAVG)/2
        print(self.speedAVG)
        ipLeft = ipTotal - self.progressIPglobal
        return str(datetime.timedelta(seconds=round(ipLeft / self.speedAVG, 1)))

    def runIP(self, args, ):
        """
        define runIP function
        is running inside of the thread
        returns nothing
        prints logs
        """
        print("[" + colored("mapper.py", "yellow") + "][" + colored("EXEC", "yellow") + "]" + colored(
            " nmap " + str(args),
            "green"))
        stdout, stderr = '', ''

        self.progressIPglobal += 1.0
        shell = subprocess.Popen(['nmap', args], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 universal_newlines=True)
        try:
            stdout, stderr = shell.communicate(timeout=30)
        except:
            print("[" + colored("SHELL", "yellow") + "][" + colored(args, "yellow") + "]" + colored(
                "BROKE DUE TO TIMEOUT", "red"))
        while True:
            return_code = shell.poll()
            output = stdout
            downDetector = re.findall(r'Host seems down.', output)
            if downDetector:
                print("[" + colored("NMAP", "yellow") + "][" + colored(args, "yellow") + "][" + colored("HOSTERR",
                                                                                                        "red") + "]")
            else:
                findPort = re.findall(self.openReg, output)
                if findPort:
                    print("[" + colored("NMAP", "yellow") + "][" + colored(args, "yellow") + "]" + colored(
                        'Found ' + self.mapPort + ' here', "blue"))
                    with open(self.outputFile, 'a') as f:
                        f.write(args + " ")
            if return_code is not None:
                break

    def __getOpenReg(self, mapPort):
        if len(mapPort) == 2:
            return r"%s/tcp   open" % mapPort
        elif len(mapPort) == 3:
            return r"%s/tcp  open" % mapPort
        elif len(mapPort):
            return r"%s/tcp open" % mapPort
