import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Nassau Candy | Business Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("Product Line Profitability & Margin Performance Analysis")
st.subheader("Nassau Candy Distributor")

st.markdown(
    "Analyze product profitability, gross margins, division performance, "
    "regional sales, and cost efficiency."
)

# Load dataset
@st.cache_data
def load_data(file):
    data = pd.read_csv(file)
    data["Order Date"] = pd.to_datetime(
        data["Order Date"], dayfirst=True, errors="coerce"
    )
    data["Ship Date"] = pd.to_datetime(
        data["Ship Date"], dayfirst=True, errors="coerce"
    )
    return data

uploaded_file = st.sidebar.file_uploader(
    "Upload Nassau Candy CSV Dataset",
    type=["csv"]
)

if uploaded_file is None:
    st.info("Upload your Nassau Candy CSV file from the sidebar to view the dashboard.")
    st.stop()

df = load_data(uploaded_file)

required_columns = [
    "Order Date", "Division", "Region", "Product Name",
    "Sales", "Cost", "Gross Profit", "Units"
]

missing_columns = [col for col in required_columns if col not in df.columns]

if missing_columns:
    st.error("Required columns missing: " + ", ".join(missing_columns))
    st.stop()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

divisions = sorted(df["Division"].dropna().unique().tolist())
selected_divisions = st.sidebar.multiselect(
    "Select Division",
    divisions,
    default=divisions
)

regions = sorted(df["Region"].dropna().unique().tolist())
selected_regions = st.sidebar.multiselect(
    "Select Region",
    regions,
    default=regions
)

products = sorted(df["Product Name"].dropna().unique().tolist())
product_search = st.sidebar.text_input("Search Product")

margin_threshold = st.sidebar.slider(
    "Minimum Gross Margin (%)",
    min_value=0,
    max_value=100,
    value=0
)

filtered = df[
    df["Division"].isin(selected_divisions)
    & df["Region"].isin(selected_regions)
].copy()

if product_search:
    filtered = filtered[
        filtered["Product Name"].str.contains(
            product_search, case=False, na=False
        )
    ]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# KPI calculations
total_sales = filtered["Sales"].sum()
total_cost = filtered["Cost"].sum()
total_profit = filtered["Gross Profit"].sum()
total_units = filtered["Units"].sum()

gross_margin = (
    total_profit / total_sales * 100
    if total_sales != 0 else 0
)

# KPI cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"${total_sales:,.2f}")
c2.metric("Total Cost", f"${total_cost:,.2f}")
c3.metric("Gross Profit", f"${total_profit:,.2f}")
c4.metric("Gross Margin", f"{gross_margin:.2f}%")

st.caption(f"Total units sold: {total_units:,.0f}")

# Product-level analysis
st.header("Product Profitability")

product_analysis = (
    filtered.groupby("Product Name", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Cost=("Cost", "sum"),
        Total_Profit=("Gross Profit", "sum"),
        Total_Units=("Units", "sum")
    )
)

product_analysis["Gross_Margin_%"] = (
    product_analysis["Total_Profit"]
    / product_analysis["Total_Sales"].replace(0, pd.NA)
    * 100
).fillna(0)

product_analysis["Profit_Per_Unit"] = (
    product_analysis["Total_Profit"]
    / product_analysis["Total_Units"].replace(0, pd.NA)
).fillna(0)

product_view = product_analysis[
    product_analysis["Gross_Margin_%"] >= margin_threshold
].sort_values("Total_Profit", ascending=False)

st.dataframe(
    product_view.round(2),
    use_container_width=True,
    hide_index=True
)

# Top products chart
st.subheader("Top 10 Products by Gross Profit")

top_products = product_analysis.nlargest(10, "Total_Profit")

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(top_products["Product Name"], top_products["Total_Profit"])
ax.set_xlabel("Gross Profit ($)")
ax.set_ylabel("Product")
ax.invert_yaxis()
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Division performance
st.header("Division Performance")

division_analysis = (
    filtered.groupby("Division", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Gross Profit", "sum")
    )
)

division_analysis["Gross_Margin_%"] = (
    division_analysis["Total_Profit"]
    / division_analysis["Total_Sales"].replace(0, pd.NA)
    * 100
).fillna(0)

st.dataframe(
    division_analysis.round(2),
    use_container_width=True,
    hide_index=True
)

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(division_analysis["Division"], division_analysis["Total_Sales"], label="Sales")
ax.bar(division_analysis["Division"], division_analysis["Total_Profit"], label="Gross Profit")
ax.set_title("Sales vs Gross Profit by Division")
ax.set_ylabel("Amount ($)")
ax.legend()
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Regional performance
st.header("Regional Performance")

region_analysis = (
    filtered.groupby("Region", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Gross Profit", "sum")
    )
)

region_analysis["Gross_Margin_%"] = (
    region_analysis["Total_Profit"]
    / region_analysis["Total_Sales"].replace(0, pd.NA)
    * 100
).fillna(0)

st.dataframe(
    region_analysis.round(2),
    use_container_width=True,
    hide_index=True
)

# Cost vs sales
st.header("Cost vs Sales Diagnostics")

fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(filtered["Sales"], filtered["Cost"], alpha=0.6)
ax.set_xlabel("Sales ($)")
ax.set_ylabel("Cost ($)")
ax.set_title("Transaction-Level Cost vs Sales")
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Monthly profit trend
st.header("Monthly Sales and Profit Trend")

monthly = (
    filtered.dropna(subset=["Order Date"])
    .assign(Order_Month=lambda x: x["Order Date"].dt.to_period("M").astype(str))
    .groupby("Order_Month", as_index=False)
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Gross Profit", "sum")
    )
)

fig, ax = plt.subplots(figsize=(11, 4))
ax.plot(monthly["Order_Month"], monthly["Total_Profit"], marker="o")
ax.set_title("Monthly Gross Profit Trend")
ax.set_xlabel("Order Month")
ax.set_ylabel("Gross Profit ($)")
plt.xticks(rotation=75)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# Data quality note
st.header("Data Quality Notice")

shipping_delay = (
    filtered["Ship Date"] - filtered["Order Date"]
).dt.days

long_delays = (shipping_delay > 30).sum()

st.write(f"Records with shipping delays over 30 days: {long_delays}")
st.warning(
    "Verify the original shipping dates before using this dataset "
    "for delivery-performance analysis."
)

# Download filtered data
st.header("Download Analysis Data")

csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv_data,
    file_name="nassau_candy_filtered_data.csv",
    mime="text/csv"
)

st.success("Dashboard analysis completed.")
