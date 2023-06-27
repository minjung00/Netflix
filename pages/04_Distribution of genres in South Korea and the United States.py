import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import common
import seaborn as sns

common.page_config()

st.title("Distribution of genres in South Korea and the United States")

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

# Tab 구성
tab1, tab2 = st.tabs(["South Korea", "United States"])

st.title("South Korea-Data")
st.write(sk_data)

st.title("United States-Data")
st.write(usa_data)

with tab1:
    sk_genre_counts = sk_data['listed_in'].str.split(',').explode().str.strip().value_counts()
    genre_table = pd.DataFrame({'Genre': sk_genre_counts.index, 'Count': sk_genre_counts})
    sk_top_10_genres = genre_table.head(10)
    plt.pie(sk_top_10_genres.Count, labels=sk_top_10_genres.index, autopct='%1.1f%%')
    plt.title('Netflix Shows in South Korea')
    plt.show()
    st.pyplot(plt)

with tab2:
    usa_genre_counts = usa_data['listed_in'].str.split(',').explode().str.strip().value_counts()
    genre_table = pd.DataFrame({'Genre': usa_genre_counts.index, 'Count': usa_genre_counts})
    usa_top_10_genres = genre_table.head(10)
    plt.pie(usa_top_10_genres.Count, labels=usa_top_10_genres.index, autopct='%1.1f%%')
    plt.title('Netflix Shows in the United States')
    plt.show()
    st.pyplot(plt)
