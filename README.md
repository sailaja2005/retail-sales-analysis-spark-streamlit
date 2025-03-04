Retail Sales Analysis Dashboard

This project analyzes retail sales data using PySpark for efficient processing and Streamlit for interactive visualization. It provides key metrics and insights into sales performance, including:

* Total sales, profit, and customer counts
* Top-performing countries, products, and customers
* Sales distribution across categories
How to Run

1.Clone the repository:
   ```bash
   git clone [https://github.com/sailaja2005/retail-sales-analysis-spark-streamlit.git](https://github.com/sailaja2005/retail-sales-analysis-spark-streamlit.git)
Navigate to the project directory:

2.Bash

cd retail-sales-analysis-spark-streamlit
Create a conda environment (recommended):

3.Bash

conda create --name retail_env python=3.9
conda activate retail_env
Install dependencies:

4.Bash

pip install -r requirements.txt
Run the Streamlit app:

5.Bash

streamlit run main.py  # Or your script name (app.py, retail_dashboard.py)
Data
The project uses the superstore.csv dataset, which is included in the repository.

6.Dashboard Features
Key Metrics: Displays total customers, orders, sales, and profit.
Top Sales by Country: Shows a bar chart of sales by country.
Most Ordered Products: Lists the top 10 most ordered products.
Top Customers: Shows the top 10 customers based on sales.
Sales by Category: Presents a bar chart of sales by category.

7.Technologies Used
PySpark
Streamlit
Pandas
