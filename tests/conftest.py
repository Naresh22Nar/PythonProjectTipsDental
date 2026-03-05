import pytest
from playwright.sync_api import Playwright
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--url_name", action="store", default="https://rahulshettyacademy.com/client/"
    )

@pytest.fixture()
def User_Credentials(request):
    return request.param
@pytest.fixture()
def browser_Instance(playwright,request):
    browser_name= request.config.getoption("--browser_name")
    #url_name = request.config.getoption("url_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False, args=["--start-maximized"])
    elif browser_name == "chrome":
        browser = playwright.firefox.launch(headless=False, args=["--start-maximized"])
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()





