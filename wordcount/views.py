from django.http import HttpResponse #for giving direct response
from django.shortcuts import render #for passing in new page
import operator 
def homepage(request):
    return render(request,'home.html')
    

# def page1(request):
#     return HttpResponse("<h2> u are in the page1 broo ....</h2>")

def count(request):
    data = request.GET['fulltextarea']
    words = data.split()
    para_len= len(words)
    word_dictionary ={}
    for word in words :
        if word in word_dictionary:
            word_dictionary[word] += 1
        else :
            word_dictionary[word] = 1 
    sorted_item = sorted(word_dictionary.items(), key = operator.itemgetter(1),reverse = True)           
    return render(request,'count.html',{'key1': data , 'key2' : para_len, 'key3' : sorted_item })