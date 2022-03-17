"""
declare imports
"""
import time
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox, FirefoxProfile, FirefoxOptions
from termcolor import colored
from fake_useragent import UserAgent


def parse_AS(link):
    """
    parsing AS ip lists
    """
    driver.get(f'https://bgp.he.net/{link}')
    try:
        driver.find_element_by_xpath('//*[@id="tab_prefixes"]').click()
    except:
        return
    html_page = driver.page_source
    bs = BeautifulSoup(html_page, 'html.parser')
    for tr in bs.find_all('tr')[2:]:
        ip = tr.find_next('a').get_text()
        ipSplit = ip.split('.')
        if ipSplit[0].isalpha():
            continue
        elif len(ipSplit[0]) > 3:
            continue
        print(colored(flag + ' ' + ip, 'green'))
        listFile.write(ip + ' ')
    return
PATH_TO_GECKODRIVER = "geckodriver" # insert path to your geckodriver

listFile = open("list.txt", "w")
startTime = time.time()

options = FirefoxOptions()
profile = FirefoxProfile()
ua = UserAgent()
user_agent = ua.random

print(user_agent)
profile.set_preference("general.useragent.override", user_agent)
options.set_preference("dom.webnotifications.serviceworker.enabled", False)
options.set_preference("dom.webnotifications.enabled", False)
options.add_argument("--width=1400")
options.add_argument("--height=600")

driver = Firefox(executable_path=PATH_TO_GECKODRIVER, firefox_profile=profile, options=options)
driver.get("https://bgp.he.net/")

search = driver.find_element_by_xpath('//*[@id="search_search"]').send_keys("ru")
go = driver.find_element_by_xpath('/html/body/div[1]/form/div/input[2]').click()
time.sleep(3)

html_page = driver.page_source
bs = BeautifulSoup(html_page, 'html.parser')

for tr in bs.find_all('tr')[2:]:
    ip = tr.find_next('a').get_text()
    flag = tr.find_next('img')['title']
    if flag != 'Russian Federation':
        print(colored(flag + ' ' + ip, 'red'))
        continue
    if 'AS' in ip:
        previous_page = driver.current_url
        parse_AS(ip)
        driver.get(previous_page)
        continue
    elif "::" in ip:
        continue
    print(colored(flag + ' ' + ip, 'green'))
    listFile.write(ip + ' ')

driver.close()
print("[" + colored("OK", "green") + "][" + colored("scrap.py", "yellow") + "] time taken for execution " + (
    str(time.time() - startTime)) + "s")
