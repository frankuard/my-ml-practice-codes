import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

data = {'Name':[], 'Wins':[],}
url= "https://www.scrapethissite.com/pages/forms/"
r = requests.get(url, headers=headers)


soup= BeautifulSoup(r.text,"html.parser")

# print(soup.prettify())

spans = soup.select("td.name")
wins = soup.select("td.wins")

for span in spans:
    print(span.get_text(strip=True))
    data["Name"].append(span.get_text(strip=True))
    
for win in wins:
    print(win.get_text(strip=True))
    data["Wins"].append(win.get_text(strip=True))
    
df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False, sep=";")
df.to_json("data.json")
