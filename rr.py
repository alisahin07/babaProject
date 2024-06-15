import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:")

# Excel dosyasını yükleyin
file_path = 'Kitap1.xlsx'
df = pd.read_excel(file_path)

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the BANKA:",
    options=df["BANKA"].unique(),
    default=df["BANKA"].unique()
)

# Filtreleme işlemi
df_selection = df[df["BANKA"].isin(city)]


# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI's
total_sales = int(df_selection["TUTAR"].sum())
average_sale_by_transaction = round(df_selection["TUTAR"].mean(), 2)
left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Toplam Tutar:")
    st.subheader(f"TL ₺ {total_sales:,}")

with right_column:
    st.subheader("Bankaların Ortalama TuTarı")
    st.subheader(f"₺ {average_sale_by_transaction:,.2f}")

st.markdown("---")

# Filtrelenmiş DataFrame'i göster


# Bankalara göre tutar
bankalara_gore_tutar = (
    df_selection.groupby(by=["BANKA"])[["TUTAR"]].sum().sort_values(by="TUTAR")
)

fig_product_sales = px.bar(
    bankalara_gore_tutar,
    x="TUTAR",
    y=bankalara_gore_tutar.index,
    orientation="h",
    title="<b>Sales by Bank</b>",
    color_discrete_sequence=["#0083B8"] * len(bankalara_gore_tutar),
    template="plotly_white",
)






st.markdown("##")

# TOP KPI's

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Banka Grafikler:")
    st.plotly_chart(fig_product_sales)

with right_column:
    st.subheader("Excell Verisi")
    st.dataframe(df_selection)

st.markdown("---")

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)
