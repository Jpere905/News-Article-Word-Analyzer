# Jean Perez Dulzaides - FIU





import cleanWords
import main_functions
import requestArticles
import createVisual
import requests
import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import time
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk import sent_tokenize          # turn catted str sentences into indivi. sentences
from nltk import word_tokenize          # turn str sentence words into tokens
from nltk.probability import FreqDist   # count occurrences
from nltk.corpus import stopwords       # removes stopwords

nltk.download("punkt")
nltk.download("stopwords")

# contains strings of various categories of news
topics = [
    "", "arts", "automobiles", "books",
    "business","fashion","food",
    "health","home","insider",
    "magazine", "movies", "nyregion",
    "obituaries", "opinion", "politics",
    "realestate", "science", "sports",
    "sundayreview", "technology", "theater",
    "t-magazine", "travel", "upshot",
    "us", "world"
]


def main():

    st.title("New York Times Text Analyzer-9000")

    user_name = st.text_input("What is your name?")
    if not user_name:
        st.stop()

    st.success("Hello {} :grinning:".format(user_name))

    pages = {
        "Recent stories" : top_stories_page,
        "Most popular": most_popular_page
    }

    st.sidebar.title("Pages")

    page = st.sidebar.radio("Select a page", tuple(pages.keys()))

    pages[page]()


def top_stories_page():
    st.header("Recent Stories")
    selected_topic = st.selectbox("Please select a topic", topics)
    # selected_topic = "technology" # <---- remember to remove after you finish working in terminal
    if selected_topic:
        st.write("Displaying top 10 most common words found in articles relating to", selected_topic)
    else:
        st.stop()

    requestArticles.get_topics(selected_topic)
    topic_articles = main_functions.read_from_file("JSON_documents/topicResults.json")
    clean_words = cleanWords.get_clean_words(topic_articles)

    print("topic_articles:", topic_articles)
    #print("clean_words type:",type(clean_words))
    #print("main.py - clean_words:", clean_words)

    createVisual.make_bar_chart(clean_words)

    show_word_cloud = st.checkbox("Show word cloud")

    # does not work as intended, fix later?
    # if (show_word_cloud):
    #     createVisual.make_word_cloud(topic_articles)
    # else:
    #     st.stop()

    # create wordcloud but without using a function
    if (show_word_cloud):
        str_concat = cleanWords.get_concatted_abstracts(topic_articles)
        word_cloud = WordCloud().generate(str_concat)
        fig1 = plt.figure(1, figsize=(6, 6))
        plt.imshow(word_cloud)
        plt.axis("off")
        plt.show()
        st.pyplot(fig1)
    else:
        st.stop()


def most_popular_page():
    st.header("Most Popular")
    selected_articles = st.selectbox(
        "Which set of articles would you like to examine?",
        ["", "Most emailed","Most shared", "Most viewed"]
    )

    if selected_articles:
        selected_timeframe = st.selectbox(
            "Within which time frame?",
            ["", "1 Day", "7 Days", "30 Days"]
        )
    else:
        st.stop()

    # st.write("selected_articles:", selected_articles)
    # st.write("selected_timeframe:", selected_timeframe)

    # progress bar visual
    latest_iteration = st.empty()
    bar = st.progress(0)
    finished_loading = False

    # progress bar animation
    if selected_timeframe:
        # JPD Florida Int Uni
        # increment the progress bar
        for i in range(100):
            latest_iteration.text(f"Crunching some numbers: {i + 1}")
            bar.progress(i + 1)
            time.sleep(0.03)

        finished_loading = True

    requestArticles.get_popular(selected_articles, selected_timeframe)
    popular_articles = main_functions.read_from_file("JSON_documents/popularResults.json")

    #st.write("just before loaded")
    if finished_loading:
        #st.write("inside loaded")
        # popular_word_cloud = WordCloud()
        # code below doesn't work edit: maybe it was becuase It was never even reaching into
        # this if statement
        #createVisual.make_word_cloud(popular_articles)

        # second try
        str_concat = cleanWords.get_concatted_abstracts(popular_articles)
        word_cloud = WordCloud().generate((str_concat))
        fig2 = plt.figure(2, figsize=(6, 6))
        plt.imshow(word_cloud)
        plt.axis("off")
        plt.show()
        st.pyplot(fig2)


if __name__ == "__main__":
    main()
