# utils/auth.py
import time, logging
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger("appium-test")

def login_with_email(driver, email, password, timeout=10):
    wait = WebDriverWait(driver, timeout)

    # Экран выбора языка
    try:
        logger.info("Проверяем, открыт ли экран выбора языка.")
        lang_ru = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '//*[@resource-id="com.unico.android:id/ru_button" or @text="Русский"]'
        )))
        logger.info("Найден экран выбора языка. Выбираем 'Русский'.")
        lang_ru.click()
        time.sleep(1)

        cont_lang = driver.find_elements(
            AppiumBy.XPATH,
            '//*[@resource-id="com.unico.android:id/main_button" or @text="Продолжить"]'
        )
        if cont_lang:
            logger.info("Найдена кнопка 'Продолжить' после выбора языка. Нажимаем её.")
            cont_lang[0].click()
            time.sleep(1)
        logger.info("✅ Язык выбран успешно.")
    except Exception:
        logger.info("Экран выбора языка не отображается. Продолжаем.")

    # Открытие экрана логина
    logger.info("Ищем кнопку 'Вход | Регистрация'.")
    try:
        btn_enter = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((
            AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.unico.android:id/btn_ent_register"]'
        )))
        logger.info("Кнопка 'Вход | Регистрация' найдена.")
    except Exception:
        logger.info("Кнопка 'Вход | Регистрация' не найдена. Переходим в раздел 'Настройки'.")
        settings_btn = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH,
            '(//android.widget.ImageView[@resource-id="com.unico.android:id/navigation_bar_item_icon_view"])[5]'
        )))
        settings_btn.click()
        logger.info("Открыт раздел 'Настройки'. Повторяем поиск кнопки 'Вход | Регистрация'.")
        btn_enter = wait.until(EC.element_to_be_clickable((
            AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.unico.android:id/btn_ent_register"]'
        )))
        logger.info("Кнопка 'Вход | Регистрация' найдена после перехода в настройки.")
    btn_enter.click()
    logger.info("✅ Переход к экрану авторизации выполнен.")
    time.sleep(1)

    # Вкладка "Почта"
    logger.info("Переключаемся на вкладку 'Почта'.")
    tab_email = wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.widget.FrameLayout[@content-desc="sign_by_email_btn" or @resource-id="com.unico.android:id/btn_reg_login"]'
    )))
    tab_email.click()
    logger.info("✅ Вкладка 'Почта' выбрана.")
    time.sleep(1)

    # Ввод e-mail
    logger.info("Ищем поле ввода почты.")
    field = wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
    )))
    field.click()
    logger.info(f"Вводим почту: {email}")
    field.send_keys(email)
    logger.info("✅ Почта успешно введена.")
    time.sleep(1)

    # Нажатие "Продолжить"
    logger.info("Ищем и нажимаем кнопку 'Продолжить' после ввода почты.")
    cont = wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.unico.android:id/main_button"]'
    )))
    cont.click()
    logger.info("✅ Кнопка 'Продолжить' нажата (после почты).")
    time.sleep(1)

    # Ввод пароля
    logger.info("Ищем поле ввода пароля.")
    field = wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.unico.android:id/edit_view"]'
    )))
    field.click()
    logger.info("Вводим пароль.")
    field.send_keys(password)
    logger.info("✅ Пароль успешно введён.")
    time.sleep(1)

    # Нажатие "Продолжить" после пароля
    logger.info("Ищем и нажимаем кнопку 'Продолжить' для входа.")
    cont = wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.unico.android:id/main_button"]'
    )))
    cont.click()
    logger.info("✅ Авторизация завершена. Пользователь вошёл в систему.")
    time.sleep(2)
