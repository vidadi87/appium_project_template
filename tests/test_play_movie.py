# tests/test_play_movie.py
import logging, time, pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.auth import login_with_email

logger = logging.getLogger("appium-test")

# ---------- helpers ----------
def click_safely(driver, el):
    """Пробуем .click(), если не сработал — жмём в центр через clickGesture."""
    try:
        el.click()
    except Exception:
        r = el.rect
        cx, cy = r["x"] + r["width"] // 2, r["y"] + r["height"] // 2
        driver.execute_script("mobile: clickGesture", {"x": cx, "y": cy})

def click_xpath(driver, xp: str, timeout: int = 12, clickable: bool = True):
    wait = WebDriverWait(driver, timeout)
    cond = EC.element_to_be_clickable if clickable else EC.presence_of_element_located
    el = wait.until(cond((AppiumBy.XPATH, xp)))
    click_safely(driver, el)
    return el

def scroll_down(driver, duration_ms: int = 600):
    """UiScrollable → fallback через adb swipe."""
    try:
        driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollForward()'
        )
        return
    except Exception:
        pass
    size = driver.get_window_size()
    x  = int(size["width"]  * 0.5)
    y1 = int(size["height"] * 0.78)
    y2 = int(size["height"] * 0.30)
    driver.execute_script("mobile: shell", {
        "command": "input",
        "args": ["swipe", str(x), str(y1), str(x), str(y2), str(duration_ms)],
        "includeStderr": True,
        "timeout": 5000
    })

def click_text(driver, text: str, timeout: int = 10):
    """Поиск нативным UiSelector по точному тексту и клик по центру."""
    el = WebDriverWait(driver, timeout).until(lambda d: d.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")'
    ))
    click_safely(driver, el)
    return el

# ---------- test ----------
@pytest.mark.usefixtures("driver")
def test_play_flow(driver):
    wait = WebDriverWait(driver, 12)

    # 1) Авторизация
    login_with_email(driver, "vidadi.87@gmail.com", "123456")

    # 2) Один скролл вниз (если нужно подсветить ленту/добросить секцию)
    logger.info("Один скролл вниз для подгрузки ленты.")
    scroll_down(driver)

    # 3) Открыть секцию по тексту
    logger.info("Тап по 'Unico Play Originals'.")
    click_text(driver, "Unico Play Originals")


    time.sleep(3)


