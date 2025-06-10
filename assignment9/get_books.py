#<li "row cp-search-result-item">
#<span "title-content">
#<a "author-link">
#<span "display-info-primary"
#<div "cp-format-info"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options)

results = []

try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

    search_results = driver.find_elements(By.CSS_SELECTOR, 'row cp-search-result-item')
    print(len(search_results))

    for result in search_results:
        book_dict = {}

    try:
        title = result.find_element(By.CSS_SELECTOR, 'span.title-content')
        book_dict['Title'] = title.text.strip()
    except Exception:
        book_dict['Title'] = 'empty title'

    try:
        authors = result.find_elements(By.CSS_SELECTOR, 'a.author-link')
        if authors:
            book_dict['Author'] = ';'.join([author.text.strip() for author in authors])
        else:
            book_dict['Author'] = 'empty author'
    except Exception:
        book_dict['Author'] = 'empty author'

    try:
        format_year_div = result.find_element(By.CSS_SELECTOR, 'div.cp-format-info')
        format_year = format_year_div.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
        book_dict['Format-Year'] = format_year.text.strip()
    except Exception:
        book_dict['Format-Year'] = 'no format or year'
        results.append(book_dict)

    df = pd.DataFrame(results)
    print(df)

    df.to_csv('./get_books.csv')

    with open('./get_books.json', 'w') as json_file:
        json.dump(results, json_file)

except Exception as e:
    print(f"An error has occured: {e}")
finally:
    driver.quit()