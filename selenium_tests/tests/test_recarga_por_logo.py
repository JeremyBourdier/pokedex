from selenium_tests.pages.search_page import SearchPage
import time
import pytest
from selenium.webdriver.common.by import By

def test_recarga_por_logo(driver):
    page = SearchPage(driver)
    page.open()
    time.sleep(2)


    page.buscar_pokemon("pikachu")
    time.sleep(2)

 
    driver.find_element(By.CLASS_NAME, "nav").click()
    time.sleep(3)


    pokemones = driver.find_elements(By.CLASS_NAME, "pokemon")
    assert len(pokemones) >= 10, f"Se esperaban al menos 10 pokemones tras recarga, se encontraron {len(pokemones)}"


    driver.save_screenshot("results/recarga_por_logo.png")
