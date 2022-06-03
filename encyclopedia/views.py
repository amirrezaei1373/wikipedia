from django.shortcuts import render,redirect
from django.http import HttpResponse 

import random
import markdown2
from .forms import EntryForm

from . import util



def index(request):   
    return render(request, "encyclopedia/index.html",{
        "entries": util.list_entries()
    })

def home(request, title):
    entry = util.get_entry(title)
    entry = markdown2.markdown(entry)
    return render(request, 'encyclopedia/entry.html', {
        'entry': entry,
        'title':title
    })

def search(request):
    entry = util.get_entry(request.GET.get('q'))

    if entry is not None:
        return redirect('entry', request.GET.get('q'))
    else:
        entries = util.list_entries()
        return render(request, 'encyclopedia/index.html', 
                      {'entries': [ i for i in entries if request.GET.get('q').lower() in i.lower()]})


def create(request):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'encyclopedia/create.html',{'form': form})
    elif request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            util.save_entry(form.cleaned_data['title'], form.cleaned_data['content'])
            return redirect('entry', form.cleaned_data['title'])
        return render(request, 'encyclopedia/create.html', {'form': form})

def get_random(request):
    title = random.choice(util.list_entries())
    return redirect(f'/wiki/{title}/')



