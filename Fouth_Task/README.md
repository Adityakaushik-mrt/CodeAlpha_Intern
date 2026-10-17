# Sentiment Analysis on App Reviews & Social Media Data

## Project Overview

This project uses Python-based Natural Language Processing (NLP), machine learning, and data visualization to analyze customer feedback from mobile app stores and social media channels. The notebook preprocesses raw review text, computes sentiment polarity scores, trains a supervised classification model, and builds a comprehensive visual sentiment analytics dashboard to uncover operational and product-level insights.

The analysis is designed to help product development and customer support teams evaluate user sentiment, categorize underlying themes, monitor star rating alignment, and identify critical category-level pain points such as app crashes, delivery delays, and refund processing issues.

## Business Questions

The notebook explores these core questions:

1. What is the overall distribution of customer sentiment across Positive, Neutral, and Negative feedback tiers[cite: 1]?
2. How does review volume vary across digital platforms (Google Play Store, Apple App Store, and Twitter/X)[cite: 1]?
3. How well do numerical star ratings (1 to 5) correlate and align with semantic text sentiment[cite: 1]?
4. Which functional app categories (e.g., UI/UX, Customer Support, Delivery) drive positive experiences versus negative complaints[cite: 1]?
5. Can an automated machine learning model accurately classify review sentiment using text feature extraction[cite: 1]?
6. How can live or custom user feedback be classified in real-time with polarity scoring[cite: 1]?

## Tools & Libraries

- **Python** — core analysis and data manipulation[cite: 1]
- **Jupyter Notebook** — interactive development and documentation[cite: 1]
- **Pandas** & **NumPy** — data loading, text preprocessing, and matrix operations[cite: 1]
- **Regular Expressions (`re`)** — pattern-based noise removal, URL scrubbing, and text normalization[cite: 1]
- **TextBlob** — sentiment polarity lexicon scoring[cite: 1]
- **Scikit-Learn** — English stopwords, TF-IDF vectorization, train-test splitting, Logistic Regression classification, and performance evaluation metrics[cite: 1]
- **Matplotlib** & **Seaborn** — custom multi-panel dashboard generation and confusion matrix heatmaps[cite: 1]

## Dataset

The notebook expects a CSV file named **`App_Reviews_Sentiment_Data.csv`** in the same directory as `Task4.ipynb`[cite: 1].

The code references these fields: `Review_ID`, `Date`, `Platform`, `User_City`, `Rating`, `Review_Text`, `Category`, `Helpful_Votes`, `Verified_Purchase`, and `Sentiment`[cite: 1].

> **Important:** The CSV dataset is required to run the notebook, but it must be provided alongside the notebook file. Add the dataset to your repository only if you have permission to share it, and avoid committing confidential or restricted customer data.

## Analysis & Visualizations

### 1. Data Cleaning & Corpus Preprocessing
Extracts standardized word tokens by[cite: 1]:
- Converting raw text to lowercase[cite: 1]
- Stripping web URLs and hyperlinks[cite: 1]
- Removing HTML tags, special characters, and digits[cite: 1]
- Removing Scikit-Learn's built-in English stop words and short word tokens[cite: 1]
- Creating auxiliary features including `Review_Length`, `Word_Count`, and TextBlob `Polarity_Score`[cite: 1]

### 2. Supervised Sentiment Classification Model
Converts cleaned text tokens into numerical features using **TF-IDF Vectorization** (`ngram_range=(1, 2)` with a 1,500 feature ceiling)[cite: 1]. A **Logistic Regression** classifier is trained on an 80/20 stratified split (`random_state=42`), evaluating test performance via classification reports and confusion matrices[cite: 1].

### 3. Visual Sentiment Analytics Dashboard
Combines four visual components into a unified 2 × 2 dashboard and exports the figure as `sentiment_analysis_dashboard.png`[cite: 1]:
- **Overall Sentiment Distribution:** A bar chart showing the count distribution across Positive, Neutral, and Negative classes[cite: 1].
- **Star Rating vs. Sentiment Alignment:** A stacked bar chart visualizing how star ratings (1 to 5) align with assigned sentiment tiers[cite: 1].
- **Sentiment Breakdown Across App Categories:** A horizontal stacked bar chart identifying positive and negative sentiment volumes across categories[cite: 1].
- **Logistic Regression Confusion Matrix:** An annotated heatmap highlighting true vs. predicted classifications across test set categories[cite: 1].

### 4. Real-Time Inference Pipeline
Provides a reusable function `predict_new_feedback(text)` that accepts custom review text or social media posts, applies standard cleaning and vectorization, and returns predicted sentiment alongside lexicon polarity scores[cite: 1].

## Key Findings Documented in the Notebook

The notebook's analysis highlights the following key findings[cite: 1]:

- **Platform & Dataset Breakdown:** The dataset contains 15,000 balanced review records distributed across Google Play Store (8,289), Apple App Store (4,489), and Twitter/X (2,222)[cite: 1].
- **Rating vs. Text Alignment:** Star ratings strongly match semantic polarity; 1- and 2-star ratings map almost exclusively to negative feedback, while 4- and 5-star ratings correspond directly to positive reviews[cite: 1].
- **High-Performing Segments:** Users consistently commend fast delivery timelines and smooth, clean UI/UX navigation[cite: 1].
- **Critical Failure Points:** Customer complaints cluster predominantly around customer support responsiveness, payment/double billing issues, and delayed refund reconciliations[cite: 1].
- **Classification Performance:** The TF-IDF vectorizer coupled with Logistic Regression achieves robust classification performance across all three sentiment classes[cite: 1].

## Recommendations Listed in the Notebook

- **Automate Refund Tickets:** Implement automated bank and UPI refund reconciliation workflows within 24 hours to eliminate the primary driver of 1-star reviews[cite: 1].
- **App Performance Optimization:** Prioritize engineering bug fixes for checkout screen crashes reported on Android devices[cite: 1].
- **Promotional Marketing Alignment:** Highlight top-rated features, such as intuitive UI/UX and real-time tracking, in social media marketing campaigns[cite: 1].

These findings and recommendations reflect the sample data analyzed. Validate findings with ongoing production feedback and domain-specific context before making operational changes.

## Repository Structure

```text
.
├── Task4.ipynb
├── App_Reviews_Sentiment_Data.csv         # Required input; add if permitted
├── sentiment_analysis_dashboard.png       # Generated by the notebook
└── README.md