from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

from django.shortcuts import render
import requests


def button(request):
    return render(request, 'home.html')

def output(request):
    data = requests.get("https://www.google.com/")
    print(data.text)
    data = data.text
    return render(request, 'home.html', {' data ': data})

def summarizer(request):
    inp=request.POST['geturl']

    LANGUAGE = "english"
    SENTENCES_COUNT = 10

    url = str(inp)

    f = open("denemedosyasiU3.txt", "w")

    f.write(url)

    f.close()

    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        return render(request, 'home.html', {'data1': sentence})


    '''
    cmd="python C://Users//elmas.gonen//PycharmProjects//denemeB//deneme11.py "+str(inp)
    out=os.popen(cmd).read()
    p=subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    out, err =p.communicate()
    result = out.split('\n')
    print(result)
    f = open("external.txt", "w")
    # time=datetime.datetime.now()
    f.write(out)
    f.close()
    '''




'''
LANGUAGE = "english"
SENTENCES_COUNT = 10


url = data

parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
stemmer = Stemmer(LANGUAGE)

summarizer = Summarizer(stemmer)
summarizer.stop_words = get_stop_words(LANGUAGE)

for sentence in summarizer(parser.document, SENTENCES_COUNT):
   print(sentence)
'''

