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

nltk.download("punkt")
nltk.download("stopwords")
