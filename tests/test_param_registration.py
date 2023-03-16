from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/Users/Olga/Documents/Test/chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru')

   yield

   pytest.driver.quit()

def generate_string(num):
   return "ю" * num
def latin_chars():
   return 'qwertyuiopasdfghjklzxcvbnm'
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'
def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

@pytest.mark.parametrize("firstName"
   , [generate_string(1), generate_string(31), latin_chars(), latin_chars().upper(), chinese_chars(),
      special_chars(), '123']
   , ids=['1 symbols', '31 symbols', 'latin', 'LATIN', 'chinese', 'specials', 'digit'])


def test_registration_unvalid_param_name(firstName):
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.find_element(By.ID, 'kc-register').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
   # Вводим Имя
   pytest.driver.find_element(By.NAME, 'firstName').send_keys(firstName)
   # Переходим на ввод Фамилии
   pytest.driver.find_element(By.NAME, 'lastName').click()
   # Ждем сообщения об ошибке
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')))
   # Проверяем, что выводится сообщение об ошибке"
   assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."



@pytest.mark.parametrize("firstName"
   , [generate_string(2), generate_string(30)]
   , ids=['2 symbols', '30 symbols'])
@pytest.mark.parametrize("lastName"
   , [generate_string(1), generate_string(31), latin_chars(), latin_chars().upper(), chinese_chars(),
      special_chars(), '123']
   , ids=['1 symbols', '31 symbols', 'latin', 'LATIN', 'chinese', 'specials', 'digit'])


def test_registration_valid_param_name_unvalid_lastName(firstName, lastName):
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'kc-register')))
   # Нажимаем на кнопку "Зарегистрироваться"
   pytest.driver.find_element(By.ID, 'kc-register').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.NAME, 'firstName')))
      # Вводим Имя
   pytest.driver.find_element(By.NAME, 'firstName').send_keys(firstName)
      # # Переходим на ввод Фамилии
   pytest.driver.find_element(By.NAME, 'lastName').click()
   pytest.driver.find_element(By.NAME, 'lastName').send_keys(lastName)
   # Переходим на ввод адреса
   pytest.driver.find_element(By.ID, 'address').click()
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')))
   # Проверяем, что выводится сообщение об ошибке"
   assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

