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
   return "x" * num
def russian_chars():
   return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
def chinese_chars():
   return '的一是不了人我在有他这为之大来以个中上们'
def special_chars():
   return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'

@pytest.mark.parametrize("username"
   , [generate_string(255), generate_string(1001), russian_chars(), russian_chars().upper(), chinese_chars(),
      special_chars(), '123']
   , ids=['255 symbols', 'more than 1000 symbols', 'russian', 'RUSSIAN', 'chinese', 'specials', 'digit'])


def test_unvalid_mail_pass(username):
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
   # Нажимаем на кнопку "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
   # Вводим почту
   pytest.driver.find_element(By.ID, 'username').send_keys(username)
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('123')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем, что выводится сообщение об ошибке"
   # assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
   # Если срабатывает капча
   # assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверно введен текст с картинки"


   # Проверяем, какая ошибка выводится"
   if pytest.driver.find_element(By.ID, 'form-error-message').text == "Введите корректные данные":
       print('Тест пройден.')
   # Если срабатывает капча
   # if pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль" or pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверно введен текст с картинки":
   #     print('Тест пройден.')
   else:
       print('Bug. Неверный текст ошибки')


