import requests
import lxml
from bs4 import BeautifulSoup
import pyperclip
import re

def has_class_but_no_id(tag):
    return not tag.has_attr('class') and tag.has_attr('rel')

def is_backlog(href):
    return href and not re.compile("backlog").search(href)

def char_data_row(tag):
    return tag.name=="tr" and tag.has_attr('bgcolor') and not tag.has_attr('class')

def char_info(tag):
    return tag.name=="tr" and tag.has_attr('bgcolor') and not tag.has_attr('class')

def list_contains_string(lst, string):
    for v in lst:
        if string==v:
            return True
    return False
    

def is_online():
    return False

#def print_dictionary(dic):#    for v in dic.values