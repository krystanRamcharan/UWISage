from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fetch_past_paper(coursename):
    driver = webdriver.Chrome()
    driver.get("https://uwin-primo.hosted.exlibrisgroup.com/primo-explore/search?vid=MON&lang=en_US&fromRedirectFilter=true")

    # Wait for page to load
    time.sleep(5)

   
    search_box = driver.find_element(By.NAME, "query")  # Adjust selector as needed
    search_box.send_keys(paper_title)
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)  # wait for results
    results = driver.find_elements(By.CLASS_NAME, "result-title")  # Refine selectors

    links = [r.get_attribute("href") for r in results[:5]]  # Get top 5 links
    driver.quit()
    return links
