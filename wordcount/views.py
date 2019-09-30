from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    for char in '-.,\n':
        fulltext = fulltext.replace(char,' ')
    fulltext = fulltext.lower()
    wordlist = fulltext.split()

    wordcount = len(wordlist)

    word_dictionary = {}
    for word in wordlist:
        if word in word_dictionary:
            word_dictionary[word] +=1
        else:
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'wordcount':wordcount,'sorted_words': sorted_words})
