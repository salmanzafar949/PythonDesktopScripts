import requests
from bs4 import BeautifulSoup

def trade(max_pages):
    page  = 1
    while page <= max_pages:
        url ='https://www.google.com.pk/search?q=google&rlz=1C1CHZL_enPK743PK743&oq=go&aqs=chrome.0.69i59j69i60l2j69i57j69i60j0.934j0j7&sourceid=chrome&ie=UTF-8#q=google&start=40' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a'):
            href = "https://www.google.com.pk" + link.get('href')
            title = link.string
            #print(href)
            #print(title)
            get_single_item_date(href)
            page += 1

def get_single_item_date(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('div'):
        print(item_name.string)

    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)



trade(2)
