#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib.request # to pull html content from a webpage

# Get html page from url
fp = urllib.request.urlopen("https://en.wikipedia.org/wiki/Representational_state_transfer")
contents = fp.read().decode("utf-8")
# print(contents)
fp.close()

soup = BeautifulSoup(contents, 'html.parser')

pageTitle = soup.find("h1", id = "firstHeading")
# print(pageTitle.string)

toc = soup.find("div", id = "toc")

toc_list = toc.find_all("li")

for item in toc_list:
    print(item.getText())