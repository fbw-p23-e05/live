from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Hello World!")


def listings(request):
    return HttpResponse("<ol><li>Maksym</li><li>Monica</li><li>Shilpa</li></ol>")


def search_item(request, item_id):
    items = ["Laptop", "Android Phone", "Keyboard", "Mouse"]
    next_item = item_id + 1
    print(next_item)
    item = items[item_id]
    return HttpResponse(f"You requested the item {item}.")  


def search_item_by_key(request, item_name):
    items = {
        "Phones": "We have some android phones in stock",
        "Laptops": "We also sell high-end laptops",
        "Monitors": "Top of the line monitors available.",
    }
    item = items[item_name]
    return HttpResponse(item)
