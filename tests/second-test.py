import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

class DuckDuckGoTest(unittest.TestCase):
    def test_search(self):
        driver = webdriver.Edge()
        driver.get("https://duckduckgo.com/")
        
        browser = driver.find_element(By.NAME, "q")
        browser.send_keys("Selenium Python")
        browser.submit()
        
        time.sleep(2)
        
        results = driver.find_elements(By.CSS_SELECTOR, "h2")
        self.assertTrue(len(results) > 0, "No se encontraron resultados")
        driver.quit()

if __name__ == "__main__":
    unittest.main()