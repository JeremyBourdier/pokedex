from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:8080/"
        self.search_input = (By.ID, "search")
        self.search_button = (By.ID, "searchButton")
        self.result = (By.CLASS_NAME, "pokemon-nombre")

    def open(self):
        self.driver.get(self.url)

    def buscar_pokemon(self, nombre):
        self.driver.find_element(*self.search_input).clear()
        self.driver.find_element(*self.search_input).send_keys(nombre)
        self.driver.find_element(*self.search_button).click()

    def obtener_nombre_resultado(self):
        return self.driver.find_element(*self.result).text
