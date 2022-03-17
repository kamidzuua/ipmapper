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

* download geckodriver from [](https://github.com/mozilla/geckodriver/releases)
* put downloaded driver to /usr/local/bin and add it to $PATH
```bash
$ sudo mv geckodriver /usr/local/bin 
$ sudo -s
$ export PATH=$PATH:/path/to/geckodriver
```
* now you can run and have fun
* ``` $ ./run.sh ```
* enter port of interest when prompted
