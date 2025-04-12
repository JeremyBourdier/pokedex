from selenium_tests.pages.search_page import SearchPage
import time
import pytest

def test_busqueda_pokemon_valido(driver):
    page = SearchPage(driver)
    page.open()
    time.sleep(1)  

    page.buscar_pokemon("pikachu")
    time.sleep(5)  

    nombre_resultado = page.obtener_nombre_resultado().lower()
    print(f"Nombre obtenido: {nombre_resultado}")  # Diagnóstico si falla

    assert "pikachu" in nombre_resultado, f"Se esperaba 'pikachu', pero se obtuvo '{nombre_resultado}'"

    screenshot_path = "results/busqueda_pikachu.png"
    driver.save_screenshot(screenshot_path)
