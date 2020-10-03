import pandas as pd
import streamlit as st
import altair as alt
import cleanWords
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.probability import FreqDist


def make_bar_chart(clean_words):
    fdist = FreqDist(clean_words)
    # print("fdist most common:", fdist.most_common(10))
    # print("fdist type:", type(fdist))
    # print("fdist keys:", fdist.keys()) #<- prints all keys
    # print("fdist values:", fdist.values()) # <- prints all values

    fdist_common = fdist.most_common(10)
    # print("fdist_common type:", type(fdist_common))
    # print("fdist_common:", fdist_common)
    # print("fdist_common[3]:", fdist_common[3])
    # print("for i in fdist_common:")
    # for i in fdist_common:
    #     print(type(i))

    # since fdist_common has the top 10, take out each item and put it into a new list
    subject = []
    frequency = []
    for i in fdist_common:
        subject.append(i[0])
        frequency.append(i[1])

    # print(subject)
    # print(frequency)

    data = pd.DataFrame({
        "subject": subject,
        "frequency": frequency
    })

    st.write(alt.Chart(data).mark_bar(clip=True).encode(
        x="frequency",
        y=alt.Y("subject", sort="-x")
    ).properties(width=500))

# not used becuase still need to learn how to make a matplotlib figure inside of a func
# def make_word_cloud(topic_articles):
#
#     str_concat = cleanWords.get_concatted_abstracts(topic_articles)
#     word_cloud = WordCloud().generate(str_concat)
#     fig = plt.figure(figsize=(6, 6))
#     plt.imshow(word_cloud)
#     plt.axis("off")
#     plt.show()
#     st.pyplot(fig)


# def make_word_cloud2(topic_articles, word_cloud):
#
#     str_concat = cleanWords.get_concatted_abstracts(topic_articles)
#     word_cloud = WordCloud().generate(str_concat)
#     fig = plt.figure(figsize=(6, 6))
#     plt.imshow(word_cloud)
#     plt.axis("off")
#     plt.show()
#     st.pyplot(fig)