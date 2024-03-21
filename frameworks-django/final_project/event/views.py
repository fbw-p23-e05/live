from django.shortcuts import render
import requests

def api_consume(request):

    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url)

    url2 = "http://127.0.0.1:8000/api/events/"
    response2 = requests.get(url2)
    events = response2.json()[:5]

    if response.status_code == 200:
        data = response.json()[:5]
    else:
        print("Error:", response.status_code)

    return render(request, 'event/api_event.html', {'data': data, 'events': events})




