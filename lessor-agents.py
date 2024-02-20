# Retrieves the agency frequency histogram for rental real estate
# listings on realestate.com.au. More info on explanatory blog article

import requests, bs4

# Put the headers and cookies in a separate file

import re_headers

# Initialise the dictionary that will contain the frequency histogram

ag_freq = dict()

# Initialise the URL of the first page of listings, edit suburb, state and
# postcode as required

nextURL = "https://www.realestate.com.au/rent/in-carlisle,+wa+6101/list-1"

# Loop through pages

while nextURL != "terminate":

# Grab the page, put it in a Beautiful Soup

    exfile = requests.get(nextURL,headers=re_headers.headers,cookies=re_headers.cookies)
    print(nextURL, exfile.status_code)
    exsoup = bs4.BeautifulSoup(exfile.text,'html.parser')

# Agent names are in the alt attribute of img tags with class attribute "branding__image"

    agents = exsoup.find_all("img", {"class": "branding__image"})

    for brand_img in agents:
        agent = brand_img['alt']
        if agent in ag_freq:
            ag_freq[agent]+=1   
        else:
            ag_freq[agent]=1

# Grab the URL for the next page

    next = exsoup.find_all("a",{"title": "Go to Next Page"})

# print statement for debugging    
#    print(next)

# If there is no next page, terminate

    if not next :
        nextURL = "terminate"
    else:
        nextURL = "https://www.realestate.com.au" + next[0]['href']

# end while

# Print out the dictionary

for brand in ag_freq:
    print(brand,",", ag_freq[brand])
