from selenium_tests.pages.search_page import SearchPage

import time

def test_busqueda_pokemon_valido(driver):
    page = SearchPage(driver)
    page.open()
    page.buscar_pokemon("pikachu")
    time.sleep(3)  # permite que la API cargue

    nombre_resultado = page.obtener_nombre_resultado().lower()
    assert "pikachu" in nombre_resultado, f"Se esperaba 'pikachu', pero se obtuvo '{nombre_resultado}'"
