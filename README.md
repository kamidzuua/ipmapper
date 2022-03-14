# ipmapper

![stand with Ukraine](https://badgen.net/badge/stand%20with/UKRAINE/?color=0057B8&labelColor=FFD700)

### description

ipmapper is python script purpose of which is to run nmap for list of ips and put port of interest into output file. 
That output file can be used for DDoS using simple bash scripts.
Appoximate speed is 870 ip per minute.

### to do
- [x] output.txt name will depend on mapping port
- [x] implement threads
- [ ] mapping few ports simultaneously
- [ ] scrap bgp.he.net page without download
- [ ] check to prevent mapping same range few times

### requirements
```bash
$ python3 -m pip install -r requirements.txt
```

### usage

* download page from bgp.he.net and save it in repository folder as ru - bgp.he.net.html
* ``` ./run.sh ```
* enter port of interest when prompted
