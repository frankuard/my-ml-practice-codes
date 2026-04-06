import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetchAndSavetoFile(url, path):
    r = requests.get(url, headers=headers)
    with open(path, "w",encoding="utf-8") as f:
        f.write(r.text)    
url= "https://timesofindia.indiatimes.com/city/delhi/fire-breaks-out-at-plastic-bag-factory-in-delhis-shahzada-bagh/articleshow/128417590.cms"

fetchAndSavetoFile(url, "data/times.html")
