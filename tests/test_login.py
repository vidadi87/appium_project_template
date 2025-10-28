import time
import random
import pytest
import logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка логирования
logger = logging.getLogger("appium-test")
logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(name)s:%(filename)s:%(lineno)d %(message)s')

@pytest.mark.usefixtures("driver")
def test_click_russian_and_wait(driver):
    wait = WebDriverWait(driver, 10)

    logger.info("Ищем кнопку 'Русский' для выбора русской локализации.")
    russian_btn = wait.until(
        EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.unico.android:id/ru_button"]')
        )
    )
    logger.info("Найдена кнопка с текстом: Русский. Тапаем по ней.")
    russian_btn.click()
    logger.info("✅ Тест успешно завершён.")
    time.sleep(2)

    # logger.info("Ищем кнопку 'Понятно' на экране онбординга.")
    # understood_btn = wait.until(
    #     EC.presence_of_element_located(
    #         (AppiumBy.XPATH, '//android.widget.TextView[@text="Понятно"]')
    #     )
    # )
    # logger.info("Найдена кнопка с текстом: Понятно. Тапаем по ней.")
    # understood_btn.click()
    # logger.info("✅ Тест успешно завершён.")
    # time.sleep(2)


    logger.info("Ищем кнопку 'Настройки' в нижнем меню.")
    settings_button = driver.find_element(
        AppiumBy.XPATH,
        '(//android.widget.ImageView[@resource-id="com.unico.android:id/navigation_bar_item_icon_view"])[5]'
    )
    logger.info("Найдена кнопка 'Настройки'. Тапаем по ней.")
    settings_button.click()
    logger.info("✅ Тест успешно завершён.")
    time.sleep(2)

    logger.info("Ищем кнопку 'Вход | Регистрация' для начала авторизации.")
    enter_register_btn = wait.until(
        EC.presence_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="com.unico.android:id/btn_ent_register"]'
        ))
    )
    logger.info("Найдена кнопка с текстом: 'Вход | Регистрация'. Тапаем по ней.")
    enter_register_btn.click()
    logger.info("✅ Переход к окну входа/регистрации выполнен.")
    time.sleep(2)

    # logger.info("Ищем поле ввода телефона.")
    # input_field = wait.until(
    #     EC.presence_of_element_located((
    #         AppiumBy.XPATH,
    #         '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
    #     ))
    # )
    # logger.info("Найдено поле ввода телефона. Тапаем по нему.")
    # input_field.click()
    # logger.info("✅ Тест успешно завершён.")
    # time.sleep(1)

    # # Генерация и ввод номера
    # random_phone = ''.join([str(random.randint(0, 9)) for _ in range(10)])
    # logger.info(f"Вводим сгенерированный номер телефона: {random_phone}")
    # input_field.send_keys(random_phone)
    # logger.info("✅ Номер телефона успешно введён.")
    # time.sleep(3)


    logger.info("Ищем кнопку входа по почте.")
    btn_email = wait.until(
        EC.presence_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@content-desc="sign_by_email_btn" or @resource-id="com.unico.android:id/btn_reg_login"]'
        ))
    )
    logger.info("Найдена кнопка входа по почте. Тапаем по ней.")
    btn_email.click()
    logger.info("✅ Кнопка 'Вход по почте' успешно нажата.")
    time.sleep(1)


    logger.info("Ищем поле ввода почты.")
    input_email = wait.until(
        EC.presence_of_element_located((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
        ))
    )
    logger.info("Найдено поле ввода почты. Тапаем по нему.")
    input_email.click()
    logger.info("✅ Поле ввода почты успешно найдено и активировано.")


    logger.info("Тапаем в поле ввода почты.")
    input_email = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
        ))
    )
    input_email.click()
    logger.info("✅ Тап по полю ввода почты выполнен.")


    logger.info("Вводим почту в поле ввода.")
    input_email = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
        ))
    )
    input_email.click()
    input_email.send_keys("vidadi.87@gmail.com")
    logger.info("✅ Почта 'vidadi.87@gmail.com' успешно введена.")
    time.sleep(1)

    logger.info("Ищем кнопку 'Продолжить'.")
    continue_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="com.unico.android:id/main_button"]'
        ))
    )
    logger.info("Найдена кнопка 'Продолжить'. Тапаем по ней.")
    continue_btn.click()
    logger.info("✅ Кнопка 'Продолжить' успешно нажата.")
    time.sleep(1)

    logger.info("Ищем поле ввода пароля.")
    password_field = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
        ))
    )
    logger.info("Найдено поле ввода пароля. Тапаем по нему.")
    password_field.click()
    logger.info("✅ Поле ввода пароля успешно активировано.")

    logger.info("Тапаем по полю ввода пароля и вводим пароль.")
    password_field = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
        ))
    )
    password_field.click()
    password_field.send_keys("123456")
    logger.info("✅ Пароль успешно введён.")
    time.sleep(1)

    logger.info("Ищем кнопку 'Продолжить' на экране ввода пароля.")
    continue_btn = wait.until(
        EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//android.widget.FrameLayout[@resource-id="com.unico.android:id/main_button"]'
        ))
    )
    logger.info("Найдена кнопка 'Продолжить'. Тапаем по ней.")
    continue_btn.click()
    logger.info("✅ Кнопка 'Продолжить' успешно нажата.")
    time.sleep(5)
