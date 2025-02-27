**AI Diagnosis Evaluator**

**Overview**
This codebase performs a comparative analysis between doctor-generated diagnoses and AI-generated diagnoses using fuzzy string matching. It computes similarity scores, evaluates accuracy based on a configurable threshold, and visualizes the results through various plots and word clouds.

**Key Features**

**Fuzzy Matching :**
Utilizes fuzzywuzzy to compute similarity scores between doctor and AI diagnoses.
Handles differences in word order using token_set_ratio.

**Accuracy Calculation :**
Determines the percentage of diagnoses that meet or exceed a user-defined similarity threshold.

**Data Visualization :**
**Includes histograms, count plots, box plots, heatmaps, pair plots, and word clouds to provide insights into the data.

**Customizable Threshold :**
Allows adjustment of the similarity threshold to suit specific requirements.

**Word Clouds :**
Generates word clouds for both doctor and AI diagnoses to highlight frequently used terms.

**Installation and Setup**

**Prerequisites**
Ensure you have the following Python libraries installed:

pandas
matplotlib
seaborn
fuzzywuzzy
rapidfuzz (optional, for faster performance)
wordcloud
You can install these dependencies using pip:

**bash code**

pip install pandas matplotlib seaborn fuzzywuzzy wordcloud

**Input Data**

The script reads a CSV file located at C:\Users\Downloads\model_diagnosis_py.csv.

The file should contain two columns: one for doctor diagnoses and one for AI diagnoses.

Ensure the file has no header; column names are assigned programmatically.

**Usage**

**Run the Script :**

Execute the script in your Python environment.

Adjust the threshold variable if needed to evaluate different levels of similarity.

**Output :**

**Console Output :**
Prints the fuzzy matching accuracy as a percentage.
Displays the first few rows of the dataset with computed similarity scores.

**Visualizations :**

Distribution of similarity scores.

Count of matches vs. non-matches.

Box plot of similarity scores.

Heatmap of average similarity scores grouped by doctor and AI diagnoses.

Pair plot for exploratory data analysis.

Word clouds for doctor and AI diagnoses.

**Code Walkthrough**

**Data Loading :**
Reads the CSV file and assigns column names: Doctor and AI.

**Similarity Computation :**
Defines a function compute_similarity to calculate similarity scores using fuzz.token_set_ratio.
Applies this function to each row of the DataFrame.

**Threshold-Based Matching :**
Compares similarity scores against a threshold to classify matches and non-matches.
Computes overall matching accuracy.

**Visualization :**
Generates multiple plots to analyze the distribution, trends, and relationships in the data.

**Word Cloud Generation :**
Creates word clouds to visualize frequently occurring terms in both doctor and AI diagnoses.
