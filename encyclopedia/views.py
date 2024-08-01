
from django.shortcuts import render
from markdown2 import Markdown 
from . import util
import random

def change_md(title):
    content= util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    html_info = change_md(title)
    if html_info == None:
        return render(request, "encyclopedia/mistake.html", {
            "alert":"Not available!"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":html_info,
        })

def search(request):
    if request.method == "POST":
        search_content=request.POST['q']
        html_info= change_md(search_content)
        if html_info is not None:
            return render(request, "encyclopedia/entry.html", {
                "title":search_content,
                "content":html_info,
            })
        else:
            all_searches= util.list_entries()
            new_search= []
            for search in all_searches:
                if search_content.lower() in search.lower():
                    new_search.append(search)
        return render(request,  "encyclopedia/search.html", {
                "new_search":new_search,
                
            })
    

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/newEntries.html")
    else:
        title= request.POST['title']
        content= request.POST['content']
        converted_title= util.get_entry(title)
        if converted_title != None:
            return render(request, "encyclopedia/mistake.html",{
                "alert": "The entry already exist"
            })
        else:
            util.save_entry(title, content)
            html_info= change_md(title)
            return render(request, "encyclopedia/entry.html", {
                "title":title,
                "content":html_info,
            })


def edit_view(request):
    if request.method == 'POST':
        title= request.POST['new_title']
        content= util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content":content,
        })
    
def save_edit(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        util.save_entry(title, content)
        html_info= change_md(title)
        return render(request, "encyclopedia/entry.html", {
            "title":title,
            "content":html_info,
        })

 

def random_searches(request):
    all_searches= util.list_entries()
    random_search= random.choice(all_searches)
    html_info= change_md(random_search)
    return render(request, "encyclopedia/entry.html", {
            "title":random_search,
            "content":html_info,
        })
