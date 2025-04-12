from selenium_tests.pages.search_page import SearchPage
import time
import pytest
from selenium.webdriver.common.by import By

def test_busqueda_pokemon_invalido(driver):
    page = SearchPage(driver)
    page.open()
    time.sleep(1)

    nombre_invalido = "noexiste"
    page.buscar_pokemon(nombre_invalido)
    time.sleep(2)


    screenshot_path = f"results/busqueda_invalida_{nombre_invalido}.png"
    driver.save_screenshot(screenshot_path)


    pokemones = driver.find_elements(By.CLASS_NAME, "pokemon")
    assert len(pokemones) == 0, f"Se esperaban 0 tarjetas de Pokémon, pero se encontraron {len(pokemones)}"
