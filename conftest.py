import pytest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
from pathlib import Path
import json
import allure
from allure_commons.types import AttachmentType


BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    global driver
    # Create a Service instance
    service = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    # Pass the Service instance to webdriver.Chrome()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    request.cls.driver = driver
    request.cls.driver.maximize_window()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(),name="failed_test",attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item,"rep_"+rep.when,rep)
    return rep

#html report
@pytest.hookimpl(tryfirst = True)
def  pytest_configure(config) :
    today = datetime.now()
    report_dir = Path("orangehrmreports",today.strftime('%Y%m%d'))
    report_dir.mkdir(parents= True,exist_ok= True)
    pytest_html = report_dir / f"Report_{today.strftime('%Y%m%d%H%M')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True

def pytest_html_report_title(report):
    report.title = "OrangeHrm Test Report"

@pytest.fixture
def user_data():
    with open('data/orangehrmdata.json',"r") as file :
        data = json.load(file)
    return data