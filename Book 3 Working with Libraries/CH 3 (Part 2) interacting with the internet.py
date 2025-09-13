#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# If you want to dump date to the json file.
import json
# Get request module from url library.
from urllib import request# This one has handy tools for scraping a web page.

from urllib.request import Request

# This one has handy tools for scraping a web page.
from bs4 import BeautifulSoup
# Sample page for practice.
page_url = 'https://www.rona.ca/en/product/dewalt-20-v-6-1-2-in-cordless-circular-saw-5150-rpm-50-bevel-capacity-bare-tool-battery-not-included-dcs391b-00275733?int_cmp=promo-_-homepage_tending_deals-_-hp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
}

req = Request(page_url,headers=headers)

# Open that page.
raw_page = request.urlopen(req)

#Make a BeautifulSoup object from the html page.
soup = BeautifulSoup(raw_page, 'html5lib')

# Isolate the main content block.
#content = soup.article

# Create an empty list to hold a dictionary for each item.
links_list = []

# Loop through all the links in the article.

for link in soup.find_all('a'):
    # Try to get the href, image url, and text.
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'URL':url,'IMG':img,'TEXT':text})
    except AttributeError:
        #... skip it, don't blow up.
        pass

# Save as a JSON file.
with open('links.json', 'w', encoding ='utf-8') as links_file:
    json.dump(links_list,links_file, ensure_ascii=False)