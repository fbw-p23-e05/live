import requests

API_KEY = "7a6a91bd4eef48edb0d0de42e2b75229"
url = f"https://newsapi.org/v2/everything?q=Microsoft&sortBy=popularity&apiKey={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    json_res = response.json()
    articles = json_res['articles'][0]
    author = articles['author']
    
