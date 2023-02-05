from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from threading import Thread, Barrier
from selenium.webdriver.common.proxy import Proxy, ProxyType
import os, random

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument('--ignore-certificate-errors')
option.add_argument("disable-infobars")
option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument("disable-popup-blocking")


#proxy_ip_port = '194.156.124.91:8085'

#proxy = Proxy()
#proxy.proxy_type = ProxyType.MANUAL
#proxy.http_proxy = proxy_ip_port
#proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
#proxy.add_to_capabilities(capabilities)

def func(barrier):

    driver = webdriver.Chrome(options=option, desired_capabilities=capabilities)
    #driver.set_window_size(920, 680)
    driver.get(url) 
    time.sleep(1)
    driver.quit()
    os.system('python test.py')

# ---

url = 'http://ncom.live'
number_of_threads = 1

barrier = Barrier(number_of_threads)

threads = []

for _ in range(number_of_threads):
    t = Thread(target=func, args=(barrier,)) 
    t.start()
    threads.append(t)

for t in threads:
    t.join()
