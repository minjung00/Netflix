import streamlit as st
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import common
common.page_config()
st.title("Number of Movies and TV shows in South Korea and the United States")
data = common.get_sales()
# Tab 구성
tab1, tab2, tab3 = st.tabs(["South Korea", "United States", "Comparison"])
sk_data = data[data['country'] == 'South Korea']
usa_data = data[data['country'] == 'United States']
sk_data_counts = sk_data['type'].value_counts()
usa_data_counts = usa_data['type'].value_counts()
with tab1:
    #sk_data_counts = sk_data['type'].value_counts()
    colors = ['violet', 'mistyrose']
    plt.pie(sk_data_counts, labels=sk_data_counts.index, autopct='%1.1f%%', startangle=90,
            wedgeprops={'edgecolor': 'white', 'width': 0.7}, colors=colors)
    plt.axis('equal')
    plt.title('Netflix Shows in South Korea')
    plt.show()
with tab2:
    #usa_data_counts = usa_data['type'].value_counts()
    colors = ['green', 'mistyrose']
    plt.pie(usa_data_counts, labels=usa_data_counts.index, autopct='%1.1f%%', startangle=90,
            wedgeprops={'edgecolor': 'white', 'width': 0.7}, colors=colors)
    plt.axis('equal')
    plt.title('Netflix Shows in the United States')
    plt.show()
    st.pyplot(plt)
with tab3:
    #sk_data_counts = sk_data['type'].value_counts()
    #usa_data_counts = usa_data['type'].value_counts()
    fig, ax = plt.subplots()
    ax.plot(sk_data_counts.index, sk_data_counts, marker='o', linestyle='-', color='violet', label='South Korea')
    ax.plot(usa_data_counts.index, usa_data_counts, marker='o', linestyle='-', color='green', label='United States')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.title('Netflix Shows Comparison')
    plt.legend()
    plt.show()
    st.pyplot(plt)
