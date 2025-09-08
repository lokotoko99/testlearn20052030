# Loading unkeyed JSON from a Python string

import json
# Here the JSON data is in a big string named json_string.
# It starts with the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
"people": [
    {
        "Full Name": "Angst, Annie",
        "Birth Year": 1982,
        "Date Joined": "01/11/2011",
        "Is Active": true,
        "Balance": 300
    },
    {
        "Full Name": "Schadenfreude, Sandy",
        "Birth Year": 2004,
        "Date Joined": "03/03/2003",
        "Is Active": true,
        "Balance": 0
    }
]
}
"""

# Load JSON data from the big json_string string. s stands for strings
peep_data = json.loads(json_string)
print(type(peep_data))

# Now you can loop through the peep_data collection.
for p in peep_data['people']:
    print(p["Full Name"], p["Birth Year"], p["Date Joined"],p['Is Active'], p['Balance'])


import json
# Here the JSON data is in a big string named json_string.
# It starts with the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
    "1": {
        "count": 9061,
        "lastreferrer": "https://difference-engine.com/Courses/tml-5-1118/",
        "lastvisit": "12/20/2018",
        "page": "/etg/downloadpdf.html"
    },
    "2": {
        "count": 3342,
        "lastreferrer": "https://alansimpson.me/",
        "lastvisit": "12/19/2018",
        "page": "/html_css/index.html"
    }
}
"""
# Load JSON data from the big json_string string.
hits_data = json.loads(json_string)
print(type(hits_data))
# Now you can loop through the hits_data collection.
for k, v in hits_data.items():
    print(f"{k}. {v['count']:>5} - {v['page']}")


# Changing JSON data

import json
import datetime as dt
from datetime import timezone
# This is the Firebase JSON data (keyed).
filename = 'firebase.json'
# Open the file (standard file open stuff).
with open(filename, 'r', encoding='utf-8', newline='') as f:
# Load the whole json file into an object named people
    hits = json.load(f)
print(type(hits))    

for k, v in hits.items():
    # Convert the Firebase date to a Python date.
    pydate = dt.datetime.utcfromtimestamp(v['lastvisit'] / 1000).date()
    # In the dictionary, replace the Firebase date with Python date.
    v['lastvisit'] = f"{pydate:%m/%d/%Y})"
    # Remove the entire last referrer column.
    v.pop('lastreferrer', None)

# now look at the lastvisit date int he hits dictionary.
for k, v in hits.items():
    print(k,v)
