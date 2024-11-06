import requests
import json
from bs4 import BeautifulSoup
import threading

root_url='https://country-leaders.onrender.com/status'
req=requests.get(root_url)

status_url=200
# if req.status_code==status_url:
#     print('The contents was imported')
# else:
#     print(req.status_code)

countries_url='https://country-leaders.onrender.com'
endpoint_countries='/countries'

req_countries=requests.get(f"{countries_url}/{endpoint_countries}")
countries=requests.get(f"{countries_url}/{endpoint_countries}")



#print(countries, req.status_code)     #{'message': 'The cookie is missing'} 403 (: Forbidden)

cookie_url='https://country-leaders.onrender.com'
endpoint_cookie='/cookie'

req_cookie=requests.get(f"{countries_url}/{endpoint_cookie}")
cookie=req_cookie.cookies
#print(req_cookie.status_code, cookie)       #200 {'message': 'The cookie has been created'} without cookie 
                                            # 200 <RequestsCookieJar[<Cookie user_cookie=12fb6a72-5637-4fb5-8103-b39768a744f3 for country-leaders.onrender.com/>]>


# Try to query the countries endpoint using the cookie, save the output and print it.
url='https://country-leaders.onrender.com'
req_with_cookie=requests.get(f"{url}/{endpoint_countries}", cookies=cookie)
req_with_cookie.json()                       #['us', 'be', 'ma', 'ru', 'fr']

# Getting the actual leaders_per_country from the API
leaders_url='https://country-leaders.onrender.com/leaders'
parameters={'country':'us'}
leaders=requests.get(leaders_url, cookies=cookie, params=parameters)
leaders.json()

leaders_per_country = {}
def get_leaders():
    url='https://country-leaders.onrender.com/leaders'
    liste=['us', 'be', 'ma', 'ru', 'fr']
    for i in liste:
        leaders=requests.get(url, cookies=cookie, params={'country': i})
        leaders_dic={i:leaders.json()}
        leaders_per_country.update(leaders_dic)
    return leaders_per_country
leaders_per_country=get_leaders()

print(leaders_per_country)

#Fetch and persing
url_1='https://en.wikipedia.org/wiki/George_Washington'
page=requests.get(url_1)
soup=BeautifulSoup(page.content, features='html.parser')
soup.prettify()

paragraph_1=soup.find_all('p')
# print(paragraph_1[1].text)
# George Washington (February 22, 1732 – December 14, 1799) was a Founding Father of the United States, military officer, and farmer who served as the first president of the United States from 1789 to 1797. Appointed by the Second Continental Congress as commander of the Continental Army in 1775, Washington led Patriot forces to victory in the American Revolutionary War and then served as president of the Constitutional Convention in 1787, which drafted the current Constitution of the United States. Washington has thus become commonly known as the "Father of his Country".


lock = threading.Lock()
def get_first_paragraph(wikipedia_url:str)->str:
    # print(wikipedia_url) # keep this for the rest of the notebook
    with lock:
            page=requests.get(wikipedia_url)
            soup=BeautifulSoup(page.content, features='html.parser')
            page.encoding = 'utf-8'  
            # table = soup.find("div", id="mw-content-text").find("div", class_="mw-content-ltr mw-parser-output").find("table")
            # first_paragraph= table.find_next("p")
            table = soup.find('table')
            first_paragraph = table.find_next('p')
            print(first_paragraph.text)
    return first_paragraph.text


wikipedia_links=[]
for country in leaders_per_country.keys():
    for president in leaders_per_country[country]:
        wikipedia_links.append(president['wikipedia_url'])


threads = []
for link in wikipedia_links:
    thread = threading.Thread(target=get_first_paragraph, args=(link,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()