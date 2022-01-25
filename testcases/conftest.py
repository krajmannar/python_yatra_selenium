import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(autouse=True)
def setup(request, browser, url):
    if browser == "chrome":
        # print("launch chrome")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        # print("Launch Firefox")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "edge":
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())

    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    # request.cls.wait = wait
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")



