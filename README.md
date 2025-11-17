# Truthlens
---

# 📌 Overview

Truthlens is a machine learning–powered application built to detect whether a news article is *real or fake*.
The system uses:

* Natural Language Processing (NLP)
* ML classification models
* News scraping utilities
* Flask-based prediction API

It provides an end-to-end pipeline:
`Scrape → Clean → Train → Predict → Evaluate`.

---

# 📂 Project Structure

```
Truthlens/
│── app.py                   # Flask server for predictions
│── fakenews.py              # Model training script
│── PredictionNews.py        # Script to test and generate predictions
│── FetchReal.py             # Scrapes real-time news
│── newscrape_common.py      # Shared scraping helpers
│── sources.py               # List of news source URLs
│── data.csv                 # Main training dataset
│── data - Copy.csv          # Dataset backup
│── data - Copy - Copy.csv   # Additional/older dataset
│── twitter.json             # Sample scraped Twitter dataset
│── README.md                # Documentation
```

---

# 🧠 How It Works

```
             ┌────────────────────┐
             │  Raw News Article  │
             └─────────┬──────────┘
                       ▼
            Text Preprocessing (NLP)
         Tokenize • Clean • Remove Stopwords
                       ▼
             TF-IDF Vector Conversion
                       ▼
                ML Classification Model
         (Logistic Regression / Naive Bayes / SVM)
                       ▼
               Output: REAL or FAKE
```

---

# 🚀 Features

* ✔ NLP-powered text preprocessing
* ✔ ML classification for fake/real news
* ✔ Flask backend for real-time predictions
* ✔ Automated scraping scripts
* ✔ Ready-made datasets
* ✔ Modular and easy to extend

---

# 📊 Dataset Information

Included datasets:

* `data.csv` (main)
* `data - Copy.csv` (backup copy)
* `data - Copy - Copy.csv` (extended version)

Supported sources:

* News websites (via scraping)
* Twitter (via `twitter.json`)

---

# ▶️ How to Run the Project

### 1. Install dependencies

If you have a `requirements.txt`:

```bash
pip install -r requirements.txt
```

If not — I can generate one for you.

---

### **2. Run the Flask server**

```bash
python app.py
```

Server runs at:

```
http://localhost:5000
```

---

### 3. Run prediction script manually

```bash
python PredictionNews.py
```

Modify the script to insert custom news text.

---

### 4. (Optional) Retrain the model

```bash
python fakenews.py
```

---

# 🌐 News Scraping Utilities

### **Run scraping**

```bash
python FetchReal.py
```

### Uses helper:

* `newscrape_common.py`
* `sources.py`

This updates your dataset with real-time news.

---

# 🎯 Why This Project Matters

Misleading information spreads quickly.
Truthlens helps:

* Identify fake content
* Demonstrate an end-to-end ML pipeline
* Combine NLP + ML + Data Scraping + Deployment
* Provide an accessible prediction system

---

# 🧑‍💻 Author

Priyanshu 
Machine Learning & Backend Developer

---

