# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 01:59:20 2025

@author: iadef
"""
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Option 1: Using fuzzy matching (robust for short text and word reordering)

# You may need to install fuzzywuzzy and rapidfuzz
# pip install fuzzywuzzy 
from fuzzywuzzy import fuzz

# Read the CSV file; the file has no header so we assign our own column names.
file_path = r"C:\Users\Downloads\model_diagnosis_py.csv"
df = pd.read_csv(file_path, header=None, names=['Doctor', 'AI'])

# Defining a function to compute similarity between two diagnosis strings.
def compute_similarity(row):
    # Using token_set_ratio to allow for differences in word order
    return fuzz.token_set_ratio(row['Doctor'], row['AI'])

# Applying the function to each row and create a new column for similarity scores.
df['similarity'] = df.apply(compute_similarity, axis=1)

# Define a threshold to consider the AI diagnosis as matching the doctor's diagnosis.
threshold = 65  # You can adjust this threshold based on your needs.
df['match'] = df['similarity'] >= threshold

# Calculate matching accuracy (i.e. percentage of rows where the similarity is above the threshold)
accuracy = df['match'].mean() * 100
print("Fuzzy Matching Accuracy: {:.2f}%".format(accuracy))

# Plot 1: Distribution of similarity scores
plt.figure(figsize=(10,6))
sns.histplot(df['similarity'], bins=20, kde=True, color='skyblue')
plt.title("Distribution of Fuzzy Similarity Scores")
plt.xlabel("Similarity Score")
plt.ylabel("Frequency")
plt.show()

# Plot 2: Count plot for matches vs. non-matches
plt.figure(figsize=(6,4))
sns.countplot(x='match', data=df, palette='viridis')
plt.title("Count of Matches vs Non-Matches (Threshold = {})".format(threshold))
plt.xlabel("Match (True = Match, False = Non-Match)")
plt.ylabel("Count")
plt.show()



# Display first few rows to inspect the computed scores
print(df.head())


ax = sns.countplot(x='match', data=df, palette='viridis')
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='black', xytext=(0, 5),
                textcoords='offset points')
    
    

plt.figure(figsize=(8, 6))
sns.boxplot(y='similarity', data=df, color='lightgreen')
plt.title("Box Plot of Similarity Scores")
plt.ylabel("Similarity Score")
plt.show()


plt.figure(figsize=(10, 8))
sns.heatmap(df.pivot_table(index='Doctor', columns='AI', values='similarity', aggfunc='mean'),
            cmap='coolwarm', annot=True, fmt=".0f")
plt.title("Heatmap of Similarity Scores")
plt.xlabel("AI Diagnosis")
plt.ylabel("Doctor Diagnosis")
plt.show()

sns.pairplot(df)
plt.show()


from wordcloud import WordCloud

# Combine all text from the Doctor column
doctor_text = ' '.join(df['Doctor'].dropna())
ai_text = ' '.join(df['AI'].dropna())

# Generate word clouds
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
wordcloud_doctor = WordCloud(width=800, height=400, background_color='white').generate(doctor_text)
wordcloud_ai = WordCloud(width=800, height=400, background_color='white').generate(ai_text)

axes[0].imshow(wordcloud_doctor, interpolation='bilinear')
axes[0].set_title("Word Cloud: Doctor Diagnoses")
axes[0].axis('off')

axes[1].imshow(wordcloud_ai, interpolation='bilinear')
axes[1].set_title("Word Cloud: AI Diagnoses")
axes[1].axis('off')

plt.show()
