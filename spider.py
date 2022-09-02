#!/usr/bin/env python

import requests
import re
import urlparse


target_url = "http://www.controltechnology.co.za/"
target_links = []


def extract_links_from(url):
    response = requests.get(url)
    return re.findall('(?:href=")(.*?)"', response.content)


def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urlparse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]
        # if "mailto:?body=" in link:
        #     link = link.split("mailto:?body=")[1]

        if url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)


crawl(target_url)

