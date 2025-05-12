from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import re
from selenium.common.exceptions import StaleElementReferenceException

def fetch_uwilinc_results(query, max_results=5):
    try:
        driver = webdriver.Chrome()
        driver.get("https://uwin-primo.hosted.exlibrisgroup.com/primo-explore/search?vid=MON&lang=en_US")
        
        
        wait= WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.ID, "searchBar")))
        search_box = driver.find_element(By.ID, "searchBar")
        search_box.clear()
        try:
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
        except StaleElementReferenceException:
            # Re-locate if stale
            search_box = driver.find_element(By.ID, "searchBar")
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

        docs = []

        wait= WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='fulldisplay?docid=']")))
        driver.get(driver.current_url)

        
        #link= driver.find_elements(By.CLASS_NAME,"md-primoExplore-theme")
        #print(link)
        links = driver.find_elements(By.CSS_SELECTOR, "a[href*='fulldisplay?docid=']")
        
    
    # Extract hrefs
        hrefs = [link.get_attribute("href") for link in links]
    
    # Print them
        for href in hrefs:
            print(href)
            driver.get(href)
            break

        
        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.arrow-link[href$='.pdf']")))
        pdf_links = driver.find_elements(By.CSS_SELECTOR, "a.arrow-link[href$='.pdf']")
    
    # Extract hrefs
        hrefs = [link.get_attribute("href") for link in pdf_links]
    
    # Print them
        for href in hrefs:
         print(href)
        driver.quit()
        return hrefs
    
    except TimeoutException:
       driver.quit()
       return []