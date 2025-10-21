import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load data
df = pd.read_csv('Research_text_files_cleaned.csv')

st.title("📊 CORD-19 Research Explorer Dashboard")
st.write("Interactive analysis of COVID-19 research papers")

# Sidebar Filters
st.sidebar.header("Filters")
years = df['year'].dropna().unique()
selected_years = st.sidebar.multiselect("Select Years", sorted(years), default=sorted(years))
selected_df = df[df['year'].isin(selected_years)]

# 1. Show sample data
st.subheader("📁 Sample Data")
st.write(selected_df.head())

# 2. Publications by Year (Bar Chart)
st.subheader("📈 Publications by Year")
year_counts = df['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values)
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.title("Publications per Year")
st.pyplot(plt)

# 3. Top 10 Journals
st.subheader("🏆 Top 10 Journals by Number of Publications")
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(8,5))
plt.barh(top_journals.index, top_journals.values)
plt.xlabel("Number of Publications")
plt.title("Top Journals")
st.pyplot(plt)

# 4. Word Cloud of Titles
st.subheader("☁️ Word Cloud of Paper Titles")
titles = " ".join(df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
st.pyplot(plt)

# 5. Abstract Word Count Distribution
st.subheader("📊 Abstract Word Count Distribution")
plt.figure(figsize=(8,5))
plt.hist(df['abstract_word_count'].dropna(), bins=50)
plt.xlabel("Word Count")
plt.ylabel("Frequency")
plt.title("Distribution of Abstract Length")
st.pyplot(plt)

# 6. Trend Line of Publications
st.subheader("📉 Trend of Publications Over Time")
plt.figure(figsize=(8,5))
plt.plot(year_counts.index, year_counts.values, marker='o')
plt.xlabel("Year")
plt.ylabel("Publications")
plt.title("Trend of Publications Over Time")
st.pyplot(plt)

# 7. Distribution of Papers by Source
if 'source_x' in df.columns:
    st.subheader("📚 Papers by Source")
    source_counts = df['source_x'].value_counts().head(10)
    plt.figure(figsize=(8,5))
    plt.bar(source_counts.index, source_counts.values)
    plt.xticks(rotation=45)
    plt.title("Top Data Sources")
    st.pyplot(plt)
