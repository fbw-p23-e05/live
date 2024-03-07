import requests

API_KEY = "7a6a91bd4eef48edb0d0de42e2b75229"
url = f"https://newsapi.org/v2/everything?q=Microsoft&sortBy=popularity&apiKey={API_KEY}"

try:
    session = requests.Session()
    session.max_redirects = 0
    response = session.get(url, allow_redirects=False, timeout=0.0001)
    # response = requests.get(url)

    if response.status_code == 200:
        json_res = response.json()
        articles = json_res['articles'][0]
        author = articles['author']
        print(author)
        
    # raise exception if it occurs
    response.raise_for_status()
    
# except requests.exceptions.HTTPError as error:
#     print(error)

# except requests.exceptions.TooManyRedirects as redirects_err:
#     print(redirects_err)
    
except requests.ConnectionError as conn_err:
    print(conn_err)

except requests.Timeout as timeout_err:
    print(timeout_err)
    