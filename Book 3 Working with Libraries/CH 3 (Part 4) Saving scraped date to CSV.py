
from urllib import request
from urllib.request import Request
from bs4 import BeautifulSoup
import json
import csv

page_url = 'https://books.toscrape.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
}

req = Request(page_url, headers=headers)
raw_page = request.urlopen(req)
soup = BeautifulSoup(raw_page, 'html5lib')

links_list = []

for link in soup.find_all('a'):
    try:
        url = link.get('href')

        # Safely get image src
        img = link.img.get('src') if link.img else None

        # Get all text inside <a>, not just from <span>
        text = link.get_text(strip=True)

        # Save only if something useful is found
        if url or img or text:
            links_list.append({'URL': url, 'IMG': img, 'TEXT': text})

    except AttributeError:
        # ... skip it, don't blow up.
        pass


# Save as JSON file.

with open('links.json', 'w', newline='') as links_file:
    json.dump(links_list, links_file, ensure_ascii=False, indent = 2)

# Saving scraped date to a CSV file
# If you want to save to CSV.

# Save it to a CSV.
with open('links.csv', 'w', newline ='') as csv_out:
    csv_writer = csv.writer(csv_out)
    # Create the header row
    csv_writer.writerow(['url','img','text'])
    for row in links_list:
        csv_writer.writerow([str(row['URL']),str(row['IMG']),str(row['TEXT'])])

print('Done')