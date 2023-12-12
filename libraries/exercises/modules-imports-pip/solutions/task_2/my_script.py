import the_pytech_calculator as ptc 
import requests 

sum = ptc.add(90, 450)
print(sum)

url = "https://moviesdatabase.p.rapidapi.com/titles"

headers = {
	"X-RapidAPI-Key": "ab794a4f47msh7109b91f8ad7cefp19b78bjsn33ffa8dd8d92",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

r = requests.get(url, headers=headers)
results = r.json()
print(results)
