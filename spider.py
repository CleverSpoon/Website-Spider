#!/usr/bin/env python

import requests
import re
import urlparse
import linkdiscovery

target_url = "http://192.168.188.203/dvwa/"
links_to_ignore = ["http://192.168.188.203/dvwa/logout.php"]
data_dict = {"username": "admin", "password": "password", "Login": "submit"}

spider = linkdiscovery.LinkDiscovery(target_url, links_to_ignore)
spider.session.post("http://192.168.188.203/dvwa/login.php", data=data_dict)
spider.crawl()





