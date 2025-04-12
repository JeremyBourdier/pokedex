from selenium.webdriver.common.by import By
import time
import pytest

def test_vista_detallada_pokemon(driver):
    driver.get("http://127.0.0.1:8080/")  
    time.sleep(3)  

    primer_pokemon = driver.find_elements(By.CLASS_NAME, "pokemon")[0]
    nombre = primer_pokemon.find_element(By.CLASS_NAME, "pokemon-nombre").text
    primer_pokemon.click()
    time.sleep(2)

  
    detalle_nombre = driver.find_element(By.TAG_NAME, "h2").text.lower()
    assert nombre.lower() in detalle_nombre, f"Se esperaba ver '{nombre}' en los detalles, pero se encontró '{detalle_nombre}'"

  
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "altura" in body_text.lower() or "altura:" in body_text.lower(), "No se encontró el campo altura"
    assert "peso" in body_text.lower() or "peso:" in body_text.lower(), "No se encontró el campo peso"


    screenshot_path = f"results/detalle_{nombre.lower()}.png"
    driver.save_screenshot(screenshot_path)
