import operator

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Wordcount index page success")


def homepage(request):
    context = {'greeting': 'How are you doing today?'}
    return render(request, 'wordcount/home.html', context)


def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # increase
            word_dictionary[word] += 1
        else:
            # add to dictionary
            word_dictionary[word] = 1

    sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)
    context = {"fulltext": fulltext, 'words': word_list, 'count': len(word_list), 'sorted_words': sorted_words}
    return render(request, 'wordcount/count.html', context)


def about(request):
    about_text = 'Linguistics Sandbox for Development of Django Conda Based Word Iteration Tools'
    return render(request, 'wordcount/about.html', {'about_text': about_text})
