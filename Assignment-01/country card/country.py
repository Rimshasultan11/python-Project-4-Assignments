import streamlit as st
import requests
import pandas as pd

# Fetch country data
def fetch_country_data():
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    data = response.json()
    countries = []

    for country in data:
        currencies = country.get('currencies', {})
        currency_name = "N/A"
        if currencies:
            first_currency = list(currencies.values())[0]
            currency_name = first_currency.get('name', 'N/A')

        countries.append({
            'Name': country.get('name', {}).get('common', 'N/A'),
            'Capital': country.get('capital', ['N/A'])[0],
            'Region': country.get('region', 'N/A'),
            'Population': country.get('population', 'N/A'),
            'Flag': country.get('flags', {}).get('png', 'N/A'),
            'Currency': currency_name,
        })

    return pd.DataFrame(countries)

# Streamlit config
st.set_page_config(page_title="Country Info", layout="wide")
st.title("🌍 Country Information Cards")

# Search bar
search_query = st.text_input("🔍 Search for a country...", "")

# Get country data
country_data = fetch_country_data()

# Filter based on search
if search_query:
    country_data = country_data[country_data['Name'].str.contains(search_query, case=False, na=False)]

# No result
if country_data.empty:
    st.warning("No country found with that name.")
else:
    # Display 2 cards per row
    for i in range(0, len(country_data), 2):
        col1, col2 = st.columns(2)
        for j, col in enumerate([col1, col2]):
            if i + j < len(country_data):
                row = country_data.iloc[i + j]
                with col:
                    st.markdown(
                        f"""
                        <div style="
                            background-color: white;
                            padding: 20px;
                            border-left: 8px solid purple;
                            border-radius: 15px;
                            box-shadow: 2px 2px 12px rgba(128, 0, 128, 0.1);
                            margin-bottom: 20px;
                            height: 100%;
                        ">
                            <div style="display: flex; align-items: center;">
                                <img src="{row['Flag']}" style="width: 80px; border-radius: 10px; margin-right: 20px;" />
                                <div>
                                    <h3 style="color: purple; margin-bottom: 10px;">{row['Name']}</h3>
                                    <p>🏙️ <strong>Capital:</strong> {row['Capital']}</p>
                                    <p>🌐 <strong>Region:</strong> {row['Region']}</p>
                                    <p>👥 <strong>Population:</strong> {row['Population']:,}</p>
                                    <p>💰 <strong>Currency:</strong> {row['Currency']}</p>
                                </div>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
