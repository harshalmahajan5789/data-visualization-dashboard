import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "students.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "StudentsPerformance.csv")

st.title("Dashboard - Students Performance Data")

img = image.imread(IMAGE_PATH)
st.image(img)

st.subheader("About Dataset")
st.write("This data set consists of the marks secured by the students in various subjects.The objective of this dataset is to understand the influence of the parents background, test preparation etc on students performance.")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)

pol = st.selectbox("Select the parental level of education:", df['parental level of education'].unique())
col1, col2, col3 = st.columns(3)

fig_1 = px.histogram(df[df['parental level of education'] == pol], x="math score")
col1.plotly_chart(fig_1, use_container_width=True)


fig_2 = px.box(df[df['parental level of education'] == pol], y="reading score")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.line(df[df['parental level of education'] == pol], x="writing score")
col3.plotly_chart(fig_3, use_container_width=True)


gen = st.selectbox("Select gender:", df['gender'].unique())
col1, col2, col3 = st.columns(3)

fig_1 = px.histogram(df[df['gender'] == gen], x="math score")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['gender'] == gen], y="reading score")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.line(df[df['gender'] == gen], x="writing score")
col3.plotly_chart(fig_3, use_container_width=True)

st.subheader("Student writing performance by test preparation course :")
fig = px.scatter(df, x="test preparation course", y="writing score")
st.plotly_chart(fig, use_container_width=False)


gend = st.selectbox("Select the Gender:", df['gender'].unique())
fig= px.pie(df[df['gender'] == gend], values='reading score', names='race/ethnicity', title='Reading score percentage of students belonging to particular race/ethnicity genderwise')
st.plotly_chart(fig, use_container_width=True)