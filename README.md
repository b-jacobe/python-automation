# 🛠️ Python Automation

## 🚀 Overview

This repository contains a collection of Python scripts for **data processing, automation, web scraping, and utility functions**. Each project is structured independently with its own dependencies.

---

## 📂 Repository Structure

```
📦 python-automation/
│── 📂 attribute_status_audit/    # Project: Attribute Status Audit Script
│   ├── 📜 attribute_status_audit.py
│   ├── 📜 README.md
│   ├── 📂 sample_data/
│   │   ├── sample_input.xlsx
│   │   ├── expected_output.xlsx
│
│── 📂 utilities/                  # Reusable helper functions
│   ├── 📜 file_utils.py
│   ├── 📜 log_utils.py
│   ├── 📜 config_loader.py
│
│── 📂 data-processing/             # Other data processing scripts
│   ├── 📜 clean_excel_data.py
│   ├── 📜 transform_csv.py
│
│── 📂 web-scraping/                # Web scraping projects
│   ├── 📜 scrape_amazon_reviews.py
│   ├── 📜 scrape_stock_prices.py
│
│── 📂 automation/                   # Task automation scripts
│   ├── 📜 auto_email_report.py
│   ├── 📜 auto_backup.py
│
│── 📂 venv/                        # Virtual Environment (ignored in .gitignore)
│── 📜 setup.py                     # Setup script (if needed)
│── 📜 .gitignore                    # Ignore venv, logs, etc.
│── 📜 README.md                    # Main repository README
```

---

## 🛠️ Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/python-automation-scripts.git
cd python-automation-scripts
```

### **2️⃣ Set Up a Virtual Environment (Recommended)**

```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate   # On Windows
```

### **3️⃣ Install Dependencies**

For each project, navigate to its folder and install dependencies:

```bash
cd attribute_status_audit
pip install -r requirements.txt
```

---

## 📌 Projects & Features

| Project Name                | Description                                           |
| --------------------------- | ----------------------------------------------------- |
| **Attribute Status Audit**  | Parses Excel logs to extract attribute status changes |
| **Excel Data Cleaner**      | Cleans and formats raw Excel/CSV files                |
| **Web Scraper - Amazon**    | Scrapes product reviews from Amazon                   |
| **Automated Email Reports** | Sends scheduled reports via email                     |

---

## 📌 Contributing

1. **Fork the repository** on GitHub.
2. **Clone your fork** to your local machine.
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature-new-script
   ```
4. **Commit and push** your changes:
   ```bash
   git commit -m "Added a new automation script"
   git push origin feature-new-script
   ```
5. **Submit a Pull Request** (PR) for review.

---

## 🔥 Future Enhancements

- [ ] Add more automation scripts (e.g., Slack bot, Google Sheets API)
- [ ] Implement logging & error handling best practices
- [ ] Optimize performance for large datasets

---

## 📜 License

This repository is licensed under the **MIT License**.

---

## 📩 Contact & Support

For issues, open a GitHub **issue** or reach out via email: `brian.a.jacobe@gmail.com`.
