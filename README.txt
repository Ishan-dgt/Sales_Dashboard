📊 Advanced Sales Dashboard (CSV-Based, Python)
📌 Project Overview

The Advanced Sales Dashboard is a Python-based analytics project that visualizes sales performance using data stored in a CSV file.
It calculates key business metrics such as revenue, profit, and best-selling products, and presents them through advanced charts and a dashboard-style interface.

This project does not use any database (SQL / NoSQL), making it lightweight, portable, and easy to deploy.

🎯 Objectives

Analyze sales data without using a database

Calculate revenue and profit dynamically

Create business-ready visual dashboards

Perform exploratory data analysis using Jupyter Notebook

Demonstrate real-world data analytics skills

🛠️ Technologies Used

Python 3

Pandas – Data processing

Matplotlib – Data visualization

Tkinter – GUI dashboard

Jupyter Notebook – Exploratory analysis

CSV – Data storage

📁 Project Structure
Advanced_CSV_Sales_Dashboard/
│
├── sales.csv                         # Sales dataset
├── advanced_sales_dashboard_csv.py   # Python dashboard (GUI)
├── advanced_sales_dashboard.ipynb    # Jupyter Notebook (EDA & charts)
├── README.md / README.txt             # Project documentation

📄 Dataset Description (sales.csv)
Column Name	Description
Product	Product name
Price	Selling price per unit
Cost	Cost price per unit
Quantity	Number of units sold
Date	Date of transaction
🔢 Calculations Used

Revenue = Price × Quantity

Profit = (Price − Cost) × Quantity

📊 Dashboard Features
✅ KPI Metrics

Total Revenue

Total Profit

Best-Selling Product

📈 Advanced Charts

Revenue by Product (Bar Chart)

Profit by Product (Bar Chart)

Monthly Revenue Trend (Line Chart)

Revenue Distribution (Pie Chart)

▶️ How to Run the Project
1️⃣ Install Required Libraries
pip install pandas matplotlib

2️⃣ Run Python Dashboard
python advanced_sales_dashboard_csv.py

3️⃣ Open Jupyter Notebook
jupyter notebook


Then open:

advanced_sales_dashboard.ipynb

🧪 Jupyter Notebook Purpose

The notebook is used for:

Exploratory Data Analysis (EDA)

KPI calculation

Chart experimentation

Data validation before dashboard integration

🎓 Use Cases

Final-year academic project

Internship portfolio

Data analytics practice

Business sales reporting

Python visualization demo

🗣️ Viva / Interview Explanation

“This project is a CSV-based sales analytics dashboard built using Python, Pandas, Matplotlib, and Tkinter. It computes revenue and profit and visualizes trends using advanced charts without relying on any database.”

🚀 Future Enhancements

Interactive filters (month, product)

Export charts as PDF

Predictive sales forecasting

Streamlit / Power BI version

Automated CSV updates

👨‍💻 Author

Name: (Your Name)
Domain: Data Analytics / Python
Level: Academic & Industry Ready

✅ Conclusion

This project demonstrates how Python can be used for end-to-end sales analytics using simple CSV data while still delivering professional-grade dashboards and insights.
