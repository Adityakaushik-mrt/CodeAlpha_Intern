# 📱 Flipkart Multi-Brand Smartphone Scraper

A robust web scraping and data extraction pipeline built with Python, BeautifulSoup, and Regular Expressions (Regex) to extract, parse, clean, and organize mobile phone specifications and pricing data across 13 major smartphone brands on Flipkart.

Developed as part of the **CodeAlpha Data Analytics Internship (Task 1: Web Scraping)**.

---

## 📌 Project Overview

E-commerce websites present dynamic, nested HTML layouts where specifications are often bundled inside lists or irregular text blocks. This project automates the extraction of structured data directly from search listings, cleans non-numeric currency characters, regularizes technical specifications (RAM, Storage, Display), removes duplicates, and exports a ready-to-analyze dataset.

### Key Features
- **Multi-Brand Automation**: Iteratively scrapes 13 top smartphone brands (`Samsung`, `Apple`, `Vivo`, `Oppo`, `Realme`, `Xiaomi`, `OnePlus`, `Motorola`, `Poco`, `iQOO`, `Infinix`, `Google Pixel`, `Nothing`).
- **Regex-Powered Parsing**: Accurately isolates numeric prices, RAM (GB), internal storage (GB/TB), and screen specifications using regular expressions.
- **Data Hygiene**: Cleans currency symbols (`₹`, commas), removes duplicate entries, and encodes output in `utf-8-sig` for clean rendering in Excel and Power BI.
- **Ethical Crawling**: Implements custom browser headers (`User-Agent`) and polite request delays (`time.sleep`) to prevent server throttling.

---

## 📊 Dataset Schema

The scraper exports data into `all_brands_smartphones_clean.csv` with the following schema:

| Column Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `Brand` | String | Target brand name | `Samsung` |
| `Model_Name` | String | Full listed title of the smartphone | `SAMSUNG Galaxy F15 5G (Jazzy Green, 128 GB)` |
| `Price_INR` | Integer | Clean numeric selling price in INR | `12999` |
| `RAM` | String | System memory configuration | `6 GB` |
| `Storage` | String | Internal ROM capacity | `128 GB` |
| `Screen_Display` | String | Screen size and panel technology | `16.51 cm (6.5 inch) Full HD+ Display` |

---

## 🛠️ Tech Stack & Prerequisites

- **Language**: Python 3.8+
- **Libraries**:
  - `requests`: HTTP requests and webpage fetching
  - `beautifulsoup4`: HTML parsing and DOM traversal
  - `pandas`: Data structuring, de-duplication, and CSV generation
  - `re`: Regular expressions for pattern-matching specifications

### Installation

Clone the repository and install the dependencies:

```bash
git clone [https://github.com/](https://github.com/)<Aditya Sharma>/CodeAlpha_Web_Scraping.git
cd CodeAlpha_Web_Scraping
pip install requests beautifulsoup4 pandas
```

---

## 🚀 Execution

Run the scraper script directly:

```bash
python flipkart.py
```

Upon execution, the script fetches up to 15 unique phone configurations per brand, displays live console logs, and writes the output file `all_brands_smartphones_clean.csv` to your current working directory.

---

## 📁 Repository Structure

```text
├── flipkart.py                        # Core web scraping script
├── all_brands_smartphones_clean.csv   # Scraped and cleaned dataset
├── README.md                          # Project documentation
└── .gitignore                         # Python cache ignores
```

---

## ⚖️ Disclaimer & Ethics
This script was developed strictly for educational and analytical purposes within the scope of the CodeAlpha Data Analytics Internship. Data scraping was conducted responsibly with rate limits and lightweight requests adhering to public search listing layouts.

---

### 👤 Author
- **Intern:** [Aditya Sharma]
- **Role:** Data Analytics Intern
- **O