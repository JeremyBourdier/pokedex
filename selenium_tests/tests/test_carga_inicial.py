from selenium_tests.pages.search_page import SearchPage
import time
import pytest

def test_carga_inicial_pokemones(driver):
    page = SearchPage(driver)
    page.open()
    time.sleep(4)  


    screenshot_path = "results/carga_inicial.png"
    driver.save_screenshot(screenshot_path)

   
    pokemones = driver.find_elements("class name", "pokemon")
    assert len(pokemones) >= 10, f"Se esperaban al menos 10 pokemones, pero se encontraron {len(pokemones)}"
