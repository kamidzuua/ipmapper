# ipmapper

### description

ipmapper is python script purpose of which is to run nmap for list of ips and put port of interest into output file. 
That output file can be used for DDoS using simple bash scripts.

### to do
- [x] output.txt name will depend on mapping port
- [ ] mapping few ports simultaneously
- [ ] scrap bgp.he.net page without download

### requirements
```python
termcolor
bs4
```

### usage

* download page from bgp.he.net and save it in repository folder as ru - bgp.he.net.html
* ``` ./run.sh ```
