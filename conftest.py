import pytest
import os
import subprocess
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    # Поднимаем окно эмулятора на передний план
    os.system('osascript -e \'tell application "System Events" to set frontmost of the first process whose name is "qemu-system-aarch64" to true\'')

    # Получаем имя активного устройства через adb
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    device_line = next((line for line in lines if "device" in line and not line.startswith("List")), None)
    if not device_line:
        raise RuntimeError("Не найдено активных устройств в adb devices")
    device_name = device_line.split()[0]

    options = UiAutomator2Options()
    options.platform_name = "Android"
    # options.platform_version = "16"
    options.device_name = device_name
    options.automation_name = "UiAutomator2"
    options.app = "/Users/vidadi/autotest_apk/1.8.0_mobile.apk"

    driver = webdriver.Remote(command_executor="http://localhost:4723", options=options)
    yield driver
    driver.quit()



# Инструкция:
# 0. Перейти в виртуалку:
# source .venv/bin/activate
# 1. Посмотреть список доступных AVD-эмуляторов:
# ~/Library/Android/sdk/emulator/emulator -list-avds
# 2. Запустить нужный эмулятор вручную через терминал:
# ~/Library/Android/sdk/emulator/emulator -avd Pixel_9a
# 3. Убедиться, что эмулятор работает (опционально):
# adb devices
# 4. В отдельном терминале запустить Appium сервер:
# appium
# 5. Запустить тест:
# pytest tests/test_login.py
# pytest tests/test_play_movie.py