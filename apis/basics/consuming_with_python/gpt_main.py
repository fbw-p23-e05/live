import requests

url = "https://open-ai21.p.rapidapi.com"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "ab794a4f47msh7109b91f8ad7cefp19b78bjsn33ffa8dd8d92",
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
}

payload = {
    "text": "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
            " Complex is better than complicated. Flat is better than nested. Sparse is better than dense."
            "Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity." 
            " Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess."
            "There should be one-- and preferably only one --obvious way to do it."
            " Although that way may not be obvious at first unless you're Dutch. Now is better than never."
            " Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea."
            "If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
}

response = requests.post(url=f"{url}/summary", headers=headers, json=payload)

print(response.json())
