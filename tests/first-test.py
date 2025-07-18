# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# import time

# def test_page_title():
    
#     options = Options()
#     # El siguiente comando es opcional, pero puede ser útil si no quieres abrir una ventana del navegador
#     # options.add_argument("--headless")
    
#     # no-sandbox es útil en entornos como Docker
#     # pero puede ser necesario en otros entornos también.
#     options.add_argument("--no-sandbox")
    
#     # Descomenta la siguiente línea si estás en un entorno sin acceso a /dev/shm
#     #  (como algunos contenedores Docker)
#     # options.add_argument("--disable-dev-shm-usage")
    
#     driver = webdriver.Chrome(options=options)
#     driver.get("https://duckduckgo.com/")
    
#     browser = driver.find_element(By.NAME, "q")
#     browser.send_keys("Selenium Python")
    
#     time.sleep(2)  # Espera para ver el resultado
    
#     results = driver.find_elements(By.CSS_SELECTOR, "h2")
    
#     assert len(results) > 0, "No se encontraron resultados"
    
#     driver.quit()