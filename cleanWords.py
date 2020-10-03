import main_functions
import requestArticles
import requests
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import time
from pprint import pprint               # pretty print
from wordcloud import WordCloud
import nltk
from nltk import sent_tokenize          # turn catted str sentences into indivi. sentences
from nltk import word_tokenize          # turn str sentence words into tokens
from nltk.probability import FreqDist   # count occurrences
from nltk.corpus import stopwords       # removes stopwords

def get_concatted_abstracts(response_json):
    str_concat = ""

    # put together every abstract sentence in a string
    for i in response_json["results"]:
        str_concat += i["abstract"]

    return str_concat


def get_clean_words(response_json):
    stopwords = nltk.corpus.stopwords.words("english")

    str_concat = get_concatted_abstracts(response_json)

    tokenized_words = word_tokenize(str_concat)
    #print("tokeinzed_words:", tokenized_words)
    # JPD Florida Int Uni

    words_no_punc = []
    # remove numeric and convert words to lower
    for word in tokenized_words:
        if word.isalnum():
            words_no_punc.append(word.lower())

    clean_words = []
    # if a word is not found in the stopwords list, then append it to another list
    for word in words_no_punc:
        if word not in stopwords:
            clean_words.append(word)

    return clean_words
