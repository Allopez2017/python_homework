from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options)


try:
    driver.get("https://owasp.org/www-project-top-ten/")

    results = driver.find_element(By.XPATH, '//h2[@id="top-10-web-application-security-risks"]')
    ul = results.find_element(By.XPATH, './following: :ul[1]')
    list = ul.find_element(By.TAG_NAME, 'li')

    vulnerabilities = []

    for li in list:
        a_link = li.find_element(By.TAG_NAME, 'a')
        title = a_link.text.strip()
        href = a_link.get_attribute('href')
        vulnerabilities.append({"Title": title, "url": href})

    if len(vulnerabilities) > 0:
        df = pd.DataFrame(vulnerabilities)
        print(df)
        
        df.to_csv('owasp_top_10.csv', index=False)
        
except Exception as e:
    print(f"An error occured: {e}")
finally:
    driver.quit

