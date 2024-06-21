import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def search_medicine_supertails(medicine_name):
    url = f'https://supertails.com/search?q={medicine_name}&page=1'
    
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load completely

        # Get the page source and parse it with BeautifulSoup
        page_source = driver.page_source
        soup_obj = BeautifulSoup(page_source, 'html.parser')

        # Find all product elements
        products = soup_obj.find_all('li', class_='findify-components-common--grid__column findify-components-common--grid__column-3 product-item')

        product_name = []
        product_price = []
        product_link = []

        for product in products:
            # Find the first <a> tag directly after the <li> tag
            link_tag = product.find_next('a', href=True)
            if link_tag:
                product_link.append('https://supertails.com' + link_tag['href'])
            else:
                product_link.append('N/A')  # Append placeholder if link is missing

            name_tag = product.find('h2', class_='findify-components--cards--product__title')
            if name_tag:
                product_name.append(name_tag.text.strip())
            else:
                product_name.append('N/A')  # Append placeholder if name is missing

            price_tag = product.find('div', class_='findify-components--cards--product--price__price findify-components--cards--product--price__sale-price')
            if price_tag:
                product_price.append(price_tag.text.strip())
            else:
                product_price.append('N/A')  # Append placeholder if price is missing

        df = pd.DataFrame({
            'Product Name': product_name,
            'Price': product_price,
            'Link': product_link
        })

        return df

    except Exception as e:
        st.error(f'Error occurred: {e}')
        return None
    finally:
        driver.quit()

def main():
    st.title('Medicine Finder')

    # Input field for medicine name
    medicine_name = st.text_input('Enter the name of the medicine:')

    if st.button('Search'):
        # Call the scraper function
        results_df = search_medicine_supertails(medicine_name)

        # Display results
        if results_df is not None and not results_df.empty:
            st.dataframe(results_df)
        elif results_df is not None:
            st.write("No results found")
            
if __name__ == '__main__':
    main()
