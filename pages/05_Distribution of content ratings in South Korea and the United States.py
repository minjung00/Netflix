import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common

common.page_config()
st.title("Distribution of content ratings in South Korea and the United States")
data = common.get_sales()

# Tab 구성
tab1, tab2 = st.tabs(["South Korea", "United States"])

sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']

sk_rating_counts = sk_data['rating'].value_counts().head(10)
usa_rating_counts = usa_data['rating'].value_counts().head(10)

with tab1:
  plt.pie(sk_rating_counts, labels=sk_rating_counts.index, autopct='%1.1f%%', colors=['skyblue', 'limegreen', 'orange', 'red', 'purple'])
  
  # 그래프 제목 설정
  plt.title('Distribution of Top 10 Ratings for Netflix Content in the South Korea')
  
  # 그래프 출력
  plt.show()
  st.pyplot(plt)
  
with tab2:
  plt.pie(usa_rating_counts, labels=rating_counts.index, autopct='%1.1f%%', colors=['skyblue', 'limegreen', 'orange', 'red', 'purple'])
  
  # 그래프 제목 설정
  plt.title('Distribution of Top 10 Ratings for Netflix Content in the United States')
  
  # 그래프 출력
  plt.show()
  st.pyplot(plt)
