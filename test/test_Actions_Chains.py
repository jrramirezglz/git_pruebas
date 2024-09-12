import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://thefreerangetester.github.io/sandbox-automation-testing/')
    yield driver
    driver.quit()

def test_hover_over_enviar(browser):
    #localizar boton por texto usando xpath
    boton =WebDriverWait(browser, 2).until(
        EC.presence_of_element_located((By.XPATH,"//button[contains(text(),'Enviar')]")
        )
     )

    #obtenemos el color antes de seleccionar
    color_before_hover =boton.value_of_css_property('background-color')
    #usamos action chains para simular el hover
    ActionChains(browser).move_to_element(boton).perform()
    #esperamos que cambie el color
    WebDriverWait(browser,2).until(
        lambda d:boton.value_of_css_property('background-color')!=color_before_hover
    )

    #obtener el color post hover
    color_after_hover =boton.value_of_css_property('background-color')

    #validar con un assertion si es diferente el color
    assert color_after_hover!=color_before_hover
