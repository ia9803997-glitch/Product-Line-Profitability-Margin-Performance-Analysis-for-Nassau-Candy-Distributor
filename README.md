Product Line Profitability & Margin Performance Analysis for Nassau Candy Distributor

📌 Project Overview

This project focuses on analyzing product-line profitability and margin performance for Nassau Candy Distributor. It uses Python-based data analysis to evaluate sales, costs, gross profit, product margins, division performance, regional performance, and profit concentration.

The objective is to identify profitable products, detect margin risks, understand cost structures, and provide data-driven recommendations to support business decisions.

🎯 Project Objectives

* Analyze total sales, total costs, and gross profit.
* Calculate gross margin percentage and profit per unit.
* Evaluate product-level profitability.
* Compare sales and profitability across divisions.
* Analyze regional sales and gross profit performance.
* Identify low-margin products and potential pricing issues.
* Perform profit concentration analysis using the Pareto approach.
* Examine the relationship between sales and costs.
* Analyze monthly sales and profit trends.
* Identify data-quality issues that may affect business analysis.

🛠️ Tools and Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Google Colab
* Jupyter Notebook
* Streamlit for interactive dashboard development

📂 Dataset Information

The dataset contains order, customer, product, geographical, sales, cost, units, and gross profit information.

The original dataset includes the following fields:

* Order ID
* Order Date
* Ship Date
* Customer ID
* City
* State/Province
* Division
* Region
* Product ID
* Product Name
* Sales
* Units
* Gross Profit
* Cost

📊 Key Performance Indicators (KPIs)

The following KPIs are used to evaluate business performance:

* Total Sales: Total revenue generated from product sales.
* Total Cost: Total recorded product cost.
* Gross Profit: Sales minus cost.
* Gross Margin (%): Gross profit divided by sales, multiplied by 100.
* Profit per Unit: Gross profit divided by units sold.
* Revenue Contribution (%): A product’s share of total sales.
* Profit Contribution (%): A product’s share of total gross profit.
* Margin Volatility: Variation in transaction-level gross margins.

💰 Overall Business Performance

Metric	Result
Total Sales	$141,783.63
Total Cost	$48,340.83
Total Gross Profit	$93,442.80
Total Units Sold	38,654
Overall Gross Margin	65.91%

These metrics provide an overview of the distributor’s financial performance in the analyzed dataset.

🔍 Product Profitability Analysis

Product-level analysis was performed to identify the products contributing the most gross profit and those requiring margin improvement.

Highest Gross Profit Product

Wonka Bar - Scrumdiddlyumptious

* Total Sales: $27,874.80
* Total Gross Profit: $19,357.50
* Gross Margin: 69.44%

Lowest Gross Margin Product

Kazookles

* Total Sales: $1,205.75
* Total Gross Profit: $92.75
* Gross Margin: 7.69%

Kazookles should be reviewed for potential pricing inefficiencies or cost-related issues before making any decisions about its future.

🏢 Division Performance Analysis

Division-level analysis compares sales, costs, gross profit, and gross margin.

Division	Total Sales	Total Gross Profit	Gross Margin
Chocolate	$131,692.90	$88,824.62	67.45%
Other	$9,663.25	$4,333.45	44.84%
Sugar	$427.48	$284.73	66.61%

Key Findings

* Chocolate generated the highest sales and gross profit.
* The Chocolate division contributed approximately 92.9% of total sales.
* Other had the lowest gross margin at 44.84%.
* The Other division should be investigated to understand its comparatively lower margin.

🌎 Regional Performance Analysis

Regional analysis was conducted to compare sales and gross profit across the distributor’s regions.

Region	Total Sales	Total Gross Profit	Gross Margin
Pacific	$46,301.53	$30,485.94	65.84%
Atlantic	$41,197.24	$26,973.70	65.47%
Interior	$32,037.60	$21,282.49	66.43%
Gulf	$22,247.26	$14,700.67	66.08%

Key Findings

* Pacific generated the highest sales and gross profit.
* Gulf generated the lowest sales and gross profit among the four regions.
* Gross margins were relatively similar across the regions.

📈 Profit Concentration Analysis

Pareto-style analysis was performed to understand how much of total gross profit comes from the highest-profit products.

Key Finding

The five highest-profit products contributed approximately 95.06% of total gross profit in the analyzed dataset.

This indicates a high concentration of recorded gross profit among a small number of products. The business should monitor these products while also evaluating opportunities to diversify its profit contribution.

⚠️ Margin Risk Analysis

Products were classified using analytical gross-margin thresholds:

* High Risk: Gross margin below 20%.
* Medium Risk: Gross margin from 20% to below 50%.
* Low Risk: Gross margin of 50% or higher.

Products Requiring Review

* Kazookles: Gross margin of 7.69%.
* Fun Dip: Gross margin of 40.00%.
* Nerds: Gross margin of 46.67%.
* SweeTARTS: Gross margin of 46.67%.

These classifications are analytical indicators, not official company risk categories. Low-margin products should be investigated before taking pricing, cost-reduction, or discontinuation decisions.

🧾 Cost vs. Sales Analysis

A scatter plot was created to examine the relationship between sales and cost at the transaction level.

This analysis helps explore:

* The relationship between sales and recorded costs.
* Transactions with relatively high costs compared with sales.
* Potential areas for further pricing and cost investigation.

Additional product-level investigation is required before confirming the causes of any margin issues.

📅 Monthly Sales and Profit Trend

Monthly sales and gross profit were analyzed using the Order Date field.

The monthly trend helps examine changes in sales and gross profit over the analysis period and provides a basis for further investigation of business performance over time.

🧹 Data Quality Checks

Data-quality checks were performed to examine:

* Missing values.
* Duplicate records.
* Zero or negative sales.
* Negative costs and gross profit.
* Invalid or non-positive units.
* Missing or invalid dates.
* Unusually long intervals between order and shipping dates.

Important Data Quality Finding

The recorded Ship Date values occur substantially later than their corresponding Order Date values. This issue requires verification against the original data source.

The original date values have not been assumed to be correct or silently changed. Shipping-time conclusions should not be relied upon until the issue is investigated.

💡 Business Recommendations

1. Review the pricing and cost structure of Kazookles because of its low gross margin.
2. Investigate the Other division’s comparatively low gross margin.
3. Monitor the five highest-profit products because they account for most recorded gross profit.
4. Evaluate product-level revenue and profit contributions before making inventory or pricing decisions.
5. Investigate potential cost inefficiencies using transaction and product-level data.
6. Validate shipping-date records before performing delivery-performance analysis.
7. Use an interactive dashboard to monitor key sales and profitability indicators.

📁 Project Structure

The repository is intended to contain the following files:

Product-Line-Profitability-Margin-Analysis/
│
├── README.md
├── Nassau_Candy_Analysis.ipynb
├── app.py
├── requirements.txt
├── Nassau_Candy_Executive_Summary.pdf
└── Nassau_Candy_Research_Report.pdf

The dashboard application, dependency file, and PDF reports should be added when they have been created.

🚀 Future Enhancements

* Develop an interactive Streamlit dashboard.
* Add product search and division filters.
* Add a date-range selector and gross-margin threshold control.
* Visualize product profitability rankings.
* Add division and regional performance charts.
* Include interactive cost-versus-margin diagnostics.
* Present profit concentration and margin-risk indicators.

👤 Project Author

Business Analyst Portfolio Project

⚠️ Disclaimer

This project is intended for educational, analytical, and portfolio purposes. Findings and recommendations are based on the available dataset and should be validated before being used for actual business decisions.
