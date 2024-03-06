import pandas as pd 
import plotly.express as px
import streamlit as st


st.set_page_config(page_title= "Super Store Dashboard",
                   page_icon="bar_chart:",
                   layout="wide"                   
                   )

df = pd.read_excel(
        io = r'C:\Users\samit\VSCode Projects\Python Steamlit Dashboard\superstoresales.xlsx',
        engine = 'openpyxl',
        sheet_name = 'Orders',
        usecols ='A:U',
        nrows= 10000,

)



# ---- SIDEBAR ---

st.sidebar.header("Please Filter Here: ")
region = st.sidebar.multiselect(
    "Select the Region:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

segment = st.sidebar.multiselect(
    "Select the Segment:",
    options=df["Segment"].unique(),
    default=df["Segment"].unique()
)

category = st.sidebar.multiselect(
    "Select the Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

ship_mode = st.sidebar.multiselect(
    "Select the Ship Mode:",
    options=df["Ship Mode"].unique(),
    default=df["Ship Mode"].unique()
)

# Use boolean indexing directly in st.dataframe
df_selection = df.loc[
    (df["Region"].isin(region)) &
    (df["Segment"].isin(segment)) &
    (df["Category"].isin(category)) &
    (df["Ship Mode"].isin(ship_mode))
]


#----MAIN PAGE ----
st.title(":bar_chart: Super Store Dashboard")
st.markdown("##")


# TOP KPI'S
total_sales = int(df_selection["Sales"].sum())
total_profit = int(df_selection["Profit"].sum())
average_sales_by_transaction = round(df_selection["Sales"].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales}")
with middle_column:
    st.subheader("Total Profit:")
    st.subheader(f"US $ {total_profit}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sales_by_transaction}")

st.markdown("---")


# SALES BY CATEGORY [BAR CHART]
sales_by_category = df_selection.groupby(by=["Category"]).agg({'Sales': 'sum'}).sort_values(by="Sales")


fig_category_sales = px.bar(
    sales_by_category,
    x="Sales",
    y= sales_by_category.index,
    orientation="h",
    title="<b> Sales by Category</b>",
    color_discrete_sequence=["#708090"]*len(sales_by_category),
    template="plotly_white",

)

fig_category_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# SALES BY SEGMENT [BAR CHART]
sales_by_segment = df_selection.groupby(by=["Segment"]).agg({'Sales': 'sum'}).sort_values(by="Sales")


fig_segment_sales = px.bar(
    sales_by_segment,
    x=sales_by_segment.index,
    y= "Sales",
    title="<b> Sales by Segment</b>",
    color_discrete_sequence=["#708090"]*len(sales_by_segment),
    template="plotly_white",

)

fig_segment_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
)
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_category_sales,use_container_width=True)
right_column.plotly_chart(fig_segment_sales,use_container_width=True)

# PROFIT BY CATEGORY [BAR CHART]
profit_by_category = df_selection.groupby(by=["Category"]).agg({'Profit': 'sum'}).sort_values(by="Profit")


fig_category_profit = px.bar(
    profit_by_category,
    x="Profit",
    y= profit_by_category.index,
    orientation="h",
    title="<b> Profit by Category</b>",
    color_discrete_sequence=["#708090"]*len(profit_by_category),
    template="plotly_white",

)

fig_category_profit.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)


# PROFIT BY SEGMENT [BAR CHART]
profit_by_segment = df_selection.groupby(by=["Segment"]).agg({'Profit': 'sum'}).sort_values(by="Profit")


fig_segment_profit = px.bar(
    profit_by_segment,
    x=profit_by_segment.index,
    y= "Profit",
    title="<b> Profit by Segment</b>",
    color_discrete_sequence=["#708090"]*len(sales_by_segment),
    template="plotly_white",

)

fig_segment_profit.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False))
)
left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_category_profit,use_container_width=True)
right_column.plotly_chart(fig_segment_profit,use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)