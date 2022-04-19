from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException,UnexpectedAlertPresentException,WebDriverException

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("--disable-setuid-sandbox")

chromeOptions.add_argument("--remote-debugging-port=9222")  # this

chromeOptions.add_argument("--disable-dev-shm-using")
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-gpu")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
#chromeOptions.add_argument(r"user-data-dir=.\cookies\\test")
path="Driver/chromedriver.exe"

driver= webdriver.Chrome(ChromeDriverManager().install(),options=chromeOptions)

driver.get("https://www.vmedulife.com/public/auth/#/login/pict-pune")
driver.maximize_window()
    #driver.implicitly_wait(9)
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[2]/div[1]/div/input").clear()
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[2]/div[1]/div/input").send_keys('ccpawar@pict.edu')
driver.find_element_by_xpath("//*[@id='passwordValue']").send_keys('Tulja@123')
driver.find_element_by_xpath("//*[@id='root']/div/div[1]/div/div[2]/div[4]/button").click()
