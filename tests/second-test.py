from selenium import webdriver
from selenium.webdriver.common.by import By

def test_search():
    driver = webdriver.Edge()
    driver.get("https://github.com")
    
    titleElement = driver.find_element(By.ID, "hero-section-brand-heading")

    assert titleElement.text == "Build and ship software on a single, collaborative platform"
    
    driver.quit()