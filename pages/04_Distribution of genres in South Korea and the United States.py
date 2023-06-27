import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common

common.page_config()

st.title("Distribution of genres in South Korea and the United States")

data = common.get_sales()

# Tab 구성
tab1, tab2 = st.tabs(["South Korea", "United States"])

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

data['main_genre'] = data['listed_in'].str.split(',').str[0]

sk_genre_counts = sk_data['listed_in'].str.split(',').explode().str.strip().value_counts()

# DataFrame 생성
genre_table = pd.DataFrame({'Genre': sk_genre_counts.index, 'Count': sk_genre_counts})

sk_top_10_genres = genre_table.head(10)

usa_genre_counts = data['listed_in'].str.split(',').explode().str.strip().value_counts()

# DataFrame 생성
us_genre_table = pd.DataFrame({'Genre': usa_genre_counts.index, 'Count': usa_genre_counts})

usa_top_10_genres = us_genre_table.head(10)

with tab1:
  plt.pie(sk_top_10_genres.Count, labels=sk_top_10_genres.index, autopct='%1.1f%%')

  #차트 제목
  plt.title('Netflix genres in the South Korea')

  #출력
  plt.show()
  st.pyplot(plt)

with tab2:
  #파이 차트
  plt.pie(usa_top_10_genres.Count, labels=usa_top_10_genres.index, autopct='%1.1f%%')

  #차트 제목
  plt.title('Netflix genres in the United States')

  #출력
  plt.show()
  st.pyplot(plt)
