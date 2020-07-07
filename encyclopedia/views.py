from django.shortcuts import render,redirect
from django  import forms
from . import util
from django.http import HttpResponseRedirect
from markdown2 import Markdown
from django.urls import reverse
import random
import re

md= Markdown()

class TitleEntry(forms.Form):
    title=forms.CharField(label="")
class DataEntry(forms.Form):
    cont=forms.CharField(widget=forms.Textarea,label="")
    

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "message" : "All Pages"
    })
def content(request,title):
    if request.method == "POST":
        form=DataEntry(request.POST)
        if form.is_valid():
            print("Hello")
            cont=form.cleaned_data["cont"].encode("utf-8")
            util.save_entry(title,cont)
            return redirect("content" ,title=title)
    else:

        if util.get_entry(title) is None:
            return render(request,"encyclopedia/error.html",{
                "message": "Page Not Found" 
            } )
        else:
            cont=md.convert(util.get_entry(title))
            return render(request,"encyclopedia/content.html",{
                "content":cont,
                "title":title
                })

    return render(request,"encyclopedia/content.html")
def edit(request,title):
    cont=util.get_entry(title)
    if cont is None:
        return render(request,"encyclopedia/error.html",{
            "message": "Content Not Found" 
        } )
    else:
        form=DataEntry({"cont":util.get_entry(title)})
    return render (request,"encyclopedia/edit.html",{
            "form": form,
            "title":title
    })

def add(request):
    
    if request.method == "POST" and 'title_submit' in request.POST:
        form=TitleEntry(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if util.get_entry(title) is None:
                return render(request,"encyclopedia/add.html",{
                    "titlecheck":True, "form":DataEntry(),
                    "title":title
            })
            else:
                return render(request,"encyclopedia/error.html",{
                    "message":"Page Already Exists"
                })
        else:
            return render(request, "encyclopedia/add.html", {
                "form": form
            })
    elif request.method =="POST" and 'data_submit' in request.POST:
        form=DataEntry(request.POST)
        title=request.POST["title"]
        if form.is_valid():
            cont=form.cleaned_data["cont"].encode("utf-8")
            util.save_entry(title,cont)
            return redirect("content", title=title)
        else:
            return render(request,"encyclopedia/error.html",{
                "message":"Unexpected Error"
            })

            
    else:
        return render(request,"encyclopedia/add.html",{
            "titlecheck":False, "form":TitleEntry()
        })

def rand(request):
    title=random.choice(util.list_entries())
    return redirect("content",title=title)

def search(request):
    
    rtitle=request.GET["q"]
    print("Hello")
    if util.get_entry(rtitle):
        return redirect("content",title=rtitle)
    else:
        request.session["titles"]=[]
        alltitles=util.list_entries()
        for title in alltitles:
            if(re.findall(rtitle,title,re.IGNORECASE)):
                request.session["titles"].append(title)
        return render(request,"encyclopedia/index.html",{
            "entries":request.session["titles"],
            "message": f"Search Results for '{rtitle}'"
        })

        


        
        



