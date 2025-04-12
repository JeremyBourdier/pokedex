from selenium_tests.pages.search_page import SearchPage
import time
import pytest

def test_busqueda_pokemon_invalido(driver):
    page = SearchPage(driver)
    page.open()
    time.sleep(1)

    nombre_invalido = "noexiste"
    page.buscar_pokemon(nombre_invalido)
    time.sleep(2)

    # Captura de la pantalla con el resultado
    screenshot_path = f"results/busqueda_invalida_{nombre_invalido}.png"
    driver.save_screenshot(screenshot_path)

   
    body_text = driver.find_element("tag name", "body").text.lower()
    assert "noexiste" not in body_text, "Se esperaba que no apareciera el texto 'noexiste'"
    assert "error" in body_text or "no" in body_text or "not" in body_text or len(body_text.strip()) < 200, "No se detectó un mensaje claro de error o la página quedó igual"
