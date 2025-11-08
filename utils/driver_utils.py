from selenium.webdriver.chrome import webdriver

from config.config import *

#创建哪种浏览器对象 使用哪种驱动模式 是否开启无头模式


def get_driver():
    #初始化driver
    driver = None

    #判断浏览器类型
    if BROWSER_TYPE == "chrome":
        driver = get_chrome_driver()
    if BROWSER_TYPE == "edge":
        driver = get_edge_driver()

    return driver

def get_chrome_driver():
    #不论什么浏览器驱动，都先设置浏览器参数,并判断是否开启无头模式
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--headless") if HEADLESS else None

    #判断使用那种驱动
    if DRIVER_TYPE == "local":
        driver = webdriver.Chrome()

def get_edge_driver():
    pass