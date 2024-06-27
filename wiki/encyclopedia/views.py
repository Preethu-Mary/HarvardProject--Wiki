
from django.shortcuts import redirect, render
import markdown2
import random 
from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry_page(request, title):
    entry = util.get_entry(title)
    if entry == None:
        return render(request, "encyclopedia/error.html", {
            "message": "Requested page was not found."
        })
    else:
        content = markdown2.markdown(entry)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": content
        })
  
def search(request):
    query = request.GET.get('q', '')
    recommendations = []
    if util.get_entry(query):
        return redirect('entry', title=query)
    else:
        entries = util.list_entries()
        for e in entries:
            if query.lower() in e.lower():
                recommendations.append(e)
        return render(request, "encyclopedia/search.html", {
            "recommendations": recommendations
        })
    
def create(request):
     if request.method == 'GET':
         return render(request, "encyclopedia/create.html")
     else:
        title = request.POST['title']
        content = request.POST['description']
        if util.get_entry(title):
              return render(request, "encyclopedia/error.html", {
            "message": "The page already exists."
        })
        else:
            util.save_entry(title, content)
            html_content = markdown2.markdown(content)
            return render(request, "encyclopedia/entry.html", {
                "title" : title,
                "content" : html_content
            })

def edit(request, title):
    content = util.get_entry(title)
    return render(request, "encyclopedia/edit.html",{
        'title': title,
        'content': content
    })

    
def save_changes(request):
    if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['description']
       util.save_entry(title, content)
       html_content = markdown2.markdown(util.get_entry(title))
       return render(request, "encyclopedia/entry.html",{
           'title': title,
           'content': html_content
       })
    

def random_choice(request):
    entries = util.list_entries()
    random_page = random.choice(entries)
    html_content = markdown2.markdown(util.get_entry(random_page))
    return render(request, "encyclopedia/entry.html",{
        'title': random_page,
        'content': html_content
    })
    
 



