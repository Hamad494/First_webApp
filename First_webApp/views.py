import operator

from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
    return render(request, 'index.html',{'key1':'I am coming from python codes'})

def result(request):
    artical = request.GET['artical']
    var_dict,word_count = counter.count(artical)


    return render(request, 'result.html', {'artical':artical, 'word_count':word_count, 'dict_words':var_dict} )
