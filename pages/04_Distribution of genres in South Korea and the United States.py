import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common

common.page_config()

st.title("Distribution of genres in South Korea and the United States.")

data = common.get_sales()

# Tab 구성
tab1, tab2 = st.tabs(["South Korea", "United States"])

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

# 맨 앞에 있는 값만 추출하여 새로운 열에 저장
data['main_genre'] = data['listed_in'].str.split(',').str[0]

sk_type_counts = sk_data['release_year'].value_counts().sort_index()
type_counts = usa_data['release_year'].value_counts().sort_index()

with tab1:
    #색깔
  color = ['violet']
  
  #선그래프
  plt.bar(sk_type_counts.index, sk_type_counts.values, color= color)
  plt.xlabel('Year')
  plt.ylabel('Count')
  plt.xticks(sk_type_counts.index, sk_type_counts.index.astype(int), rotation=45)
  plt.title('Netflix Shows in the South Korea')
  plt.show()
  st.pyplot(plt)

with tab2:
    #색깔
  color = ['olive']
  
  #선그래프
  plt.bar(type_counts.index, type_counts.values, color= color)
  plt.xlabel('Year')
  plt.ylabel('Count')
  plt.xticks(rotation=45)
  plt.title('Netflix Shows in the United States')
  plt.show()
  st.pyplot(plt)
