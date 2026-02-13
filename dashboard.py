import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Nigerian Energy Payment Analysis",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Nigerian Energy Payment Analysis Dashboard")
st.markdown("### Electricity Consumption, Billing & Payment Behaviour Analysis (2024)")

# ==============================
# LOAD DATA
# ==============================
@st.cache_data
def load_data():
    df = pd.read_csv("dataset.csv")
    df["billing_month"] = pd.to_datetime(df["billing_month"])

    # Create payment ratio
    df["payment_ratio"] = df["amount_paid_ngn"] / df["amount_billed_ngn"]

    # Avoid division errors (if any)
    df["payment_ratio"] = df["payment_ratio"].fillna(0)

    # Create owes_money flag
    df["owes_money"] = df["arrears_ngn"] > 0

    return df


df = load_data()

# ==============================
# SIDEBAR FILTERS
# ==============================
st.sidebar.header("🔎 Filters")

selected_disco = st.sidebar.multiselect(
    "Select Distribution Company",
    options=df["disco"].unique(),
    default=df["disco"].unique()
)

selected_band = st.sidebar.multiselect(
    "Select Tariff Band",
    options=df["tariff_band"].unique(),
    default=df["tariff_band"].unique()
)

date_range = st.sidebar.date_input(
    "Select Billing Period",
    [df["billing_month"].min(), df["billing_month"].max()]
)

# Apply Filters
filtered_df = df[
    (df["disco"].isin(selected_disco)) &
    (df["tariff_band"].isin(selected_band)) &
    (df["billing_month"] >= pd.to_datetime(date_range[0])) &
    (df["billing_month"] <= pd.to_datetime(date_range[1]))
]

# ==============================
# KPI SECTION
# ==============================
st.markdown("## 📌 Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Customers", f"{filtered_df['customer_id'].nunique():,}")
col2.metric("Total Energy (kWh)", f"{filtered_df['kwh'].sum():,.0f}")
col3.metric("Total Billed (NGN)", f"{filtered_df['amount_billed_ngn'].sum():,.0f}")
col4.metric("Total Arrears (NGN)", f"{filtered_df['arrears_ngn'].sum():,.0f}")

st.markdown("---")

# ==============================
# TABS
# ==============================
tab1, tab2, tab3, tab4 = st.tabs([
    "⚡ Consumption Pattern",
    "💳 Billing & Payments",
    "🚨 Tariff Risk Analysis",
    "📊 Insights"
])

# ==============================
# TAB 1 — CONSUMPTION
# ==============================
with tab1:

    st.subheader("Electricity Consumption Distribution")

    fig = px.histogram(
        filtered_df,
        x="kwh",
        nbins=60,
        title="Distribution of Electricity Consumption (kWh)",
    )

    fig.update_layout(
        xaxis_title="kWh",
        yaxis_title="Number of Customers",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Monthly Consumption Trend")

    monthly_consumption = (
        filtered_df
        .groupby("billing_month")["kwh"]
        .sum()
        .reset_index()
    )

    fig2 = px.line(
        monthly_consumption,
        x="billing_month",
        y="kwh",
        markers=True,
        title="Total Monthly Energy Consumption"
    )

    fig2.update_layout(
        xaxis_title="Month",
        yaxis_title="Total kWh",
        template="plotly_white"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ==============================
# TAB 2 — BILLING & PAYMENTS
# ==============================
with tab2:

    st.subheader("Billing vs Payment by Distribution Company")

    billing_summary = (
        filtered_df
        .groupby("disco")[["amount_billed_ngn", "amount_paid_ngn"]]
        .sum()
        .reset_index()
    )

    fig3 = go.Figure()

    fig3.add_trace(go.Bar(
        x=billing_summary["disco"],
        y=billing_summary["amount_billed_ngn"],
        name="Total Billed"
    ))

    fig3.add_trace(go.Bar(
        x=billing_summary["disco"],
        y=billing_summary["amount_paid_ngn"],
        name="Total Paid"
    ))

    fig3.update_layout(
        barmode='group',
        template="plotly_white",
        xaxis_title="Disco",
        yaxis_title="Amount (NGN)"
    )

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("### Payment Ratio by Disco")

    payment_ratio = (
        filtered_df
        .groupby("disco")["payment_ratio"]
        .mean()
        .reset_index()
    )

    fig4 = px.bar(
        payment_ratio,
        x="disco",
        y="payment_ratio",
        title="Average Payment Ratio by Disco",
    )

    fig4.update_layout(
        yaxis_title="Average Payment Ratio",
        template="plotly_white"
    )

    st.plotly_chart(fig4, use_container_width=True)

# ==============================
# TAB 3 — TARIFF RISK
# ==============================
with tab3:

    st.subheader("Total Arrears by Tariff Band")

    arrears_summary = (
        filtered_df
        .groupby("tariff_band")["arrears_ngn"]
        .sum()
        .reset_index()
    )

    fig5 = px.bar(
        arrears_summary,
        x="tariff_band",
        y="arrears_ngn",
        title="Total Arrears by Tariff Band"
    )

    fig5.update_layout(
        xaxis_title="Tariff Band",
        yaxis_title="Total Arrears (NGN)",
        template="plotly_white"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### Average Arrears per Customer")

    avg_arrears = (
        filtered_df
        .groupby("tariff_band")["arrears_ngn"]
        .mean()
        .reset_index()
    )

    fig6 = px.bar(
        avg_arrears,
        x="tariff_band",
        y="arrears_ngn",
        title="Average Arrears by Tariff Band"
    )

    fig6.update_layout(
        xaxis_title="Tariff Band",
        yaxis_title="Average Arrears (NGN)",
        template="plotly_white"
    )

    st.plotly_chart(fig6, use_container_width=True)

# ==============================
# TAB 4 — KEY INSIGHTS
# ==============================
with tab4:

    st.markdown("## 📊 Key Insights")

    st.info("""
    • Electricity consumption is right-skewed — few customers consume significantly more power.  
    • Billing amounts are relatively consistent across distribution companies.  
    • Tariff Band C contributes the largest share of total arrears.  
    • Payment behaviour varies more strongly by tariff band than by consumption level.  
    • Energy usage alone does not explain outstanding arrears risk.
    """)

    st.success("This dashboard supports data-driven tariff risk monitoring and payment compliance tracking.")
