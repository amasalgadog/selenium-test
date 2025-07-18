import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

class DuckDuckGoTest(unittest.TestCase):
    def test_search(self):
        driver = webdriver.Edge(service=Service("C:\\selenium-driver\\edgedriver_win64\\bin\\msedgedriver.exe"))
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