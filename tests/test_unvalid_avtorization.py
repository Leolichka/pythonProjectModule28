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

def test_unvalid_mail_pass():
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-mail')))
   # Нажимаем на кнопку "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
   # Вводим почту
   pytest.driver.find_element(By.ID, 'username').send_keys('leolichka@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем, какая ошибка выводится"
   if pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверная электронная почта или пароль":
       print('Тест пройден.')
   else:
       print('Bug. Неверный текст ошибки')


def test_unvalid_phone_pass():
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-phone')))
   # Нажимаем на кнопку "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
   # Вводим почту
   pytest.driver.find_element(By.ID, 'username').send_keys('71234567890')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем, какая ошибка выводится"
   if pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный номер телефона или пароль":
       print('Тест пройден.')
   else:
       print('Bug. Неверный текст ошибки')


def test_unvalid_lc_pass():
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-ls')))
   # Нажимаем на кнопку "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
   # Вводим почту
   pytest.driver.find_element(By.ID, 'username').send_keys('123456789012')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем, какая ошибка выводится"
   if pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный лицевой счет или пароль":
       print('Тест пройден.')
   else:
       print('Bug. Неверный текст ошибки')


def test_unvalid_login_pass():
   # Ждем загрузки страницы
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 't-btn-tab-login')))
   # Нажимаем на кнопку "Почта"
   pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
   # Ждем загрузки полей для ввода данных
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'username')))
   # Вводим почту
   pytest.driver.find_element(By.ID, 'username').send_keys('логин')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('123456')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.ID, 'kc-login').click()

   # Проверяем, какая ошибка выводится"
   if pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль":
       print('Тест пройден.')
   # Если срабатывает капча
   # if pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль" or pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверно введен текст с картинки":
   #     print('Тест пройден.')
   else:
       print('Bug. Неверный текст ошибки')