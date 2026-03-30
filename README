# 📊 Flipkart Laptop Data Analysis

## 🔍 Project Overview

This project performs end-to-end data analysis on laptop listings scraped from Flipkart. It includes data collection, cleaning, transformation, visualization, and insight generation to understand brand performance, product popularity, and user preferences.

---

## ⚙️ Tech Stack

* **Python**
* **BeautifulSoup** – Web scraping
* **Pandas** – Data cleaning & analysis
* **NumPy** – Numerical operations
* **Matplotlib & Seaborn** – Data visualization

---

## 📥 Data Collection

* Scraped laptop listings from Flipkart search pages
* Extracted:

  * Laptop Name
  * Ratings
  * Number of Reviews

---

## 🧹 Data Cleaning

* Converted ratings and reviews into numeric format
* Handled invalid values using `pd.to_numeric()`
* Removed missing/null values
* Fixed incorrect rating values (e.g., 4367 → 4.367)
* Filtered valid ratings range (0–5)

---

## 🧠 Feature Engineering

* Extracted **Brand** from laptop name
* Created **Popularity Metric**:

  * `popularity = Ratings + Reviews`
* Created **Score Metric**:

  * `score = Ratings × Reviews`

---

## 📊 Analysis Performed

### 🔹 Brand Distribution

* Count of laptops per brand

### 🔹 Brand Popularity

* Total reviews per brand

### 🔹 Brand Quality

* Average rating per brand

### 🔹 Combined Analysis

Used pandas `groupby` with aggregation:

* Mean & Max Ratings
* Sum & Max Reviews

---


---



## 🔑 Key Insights

* **Lenovo dominates** in terms of number of listings and total reviews, indicating strong market presence and popularity.
* **Acer has the highest average rating**, suggesting strong product quality.
* **HP shows balanced performance** in both ratings and reviews.
* **ASUS has moderate presence but comparatively lower average ratings.**
* High number of reviews does not always guarantee higher ratings.
* Best laptops are those that balance both high ratings and high review counts.

---

## 📁 Project Structure

```
PROJECTS DS/
│
├── htmls/                # Saved HTML pages
├── scraper.py           # Web scraping logic
├── analysis.py          # Data cleaning, analysis & visualization
├── data1.csv            # Raw data
├── cleaned_data.csv     # Cleaned dataset
├── brand_distribution.png
├── avg_ratings.png
├── reviews.png
├── top_laptops.png
└── README.md
```

---

## 🚀 Future Improvements

* Add price-based analysis
* Use Selenium for dynamic scraping
* Build interactive dashboards (Plotly / Streamlit)
* Automate daily data collection

---

## 💡 Key Learnings

* End-to-end data pipeline: scraping → cleaning → analysis → visualization
* Importance of data cleaning in real-world datasets
* Practical use of pandas `groupby` and aggregation
* Creating meaningful metrics for better insights

---

## 📌 Conclusion

This project demonstrates how raw web data can be transformed into actionable insights. It highlights the difference between popularity and quality, showing that dominant brands are not always the highest-rated.

---
