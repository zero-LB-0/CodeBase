from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

"""
Personalization: Define six class methods (including initialization methods)

1.  Start the page
2.  The method is to define the default
3.  The method is defined as no trace
4.  The method is to define takeover
5.  Exit the driver
"""


class TakeoverChrome:
    def __init__(self, TakeoverMode, chooseTraceless, maxWindow, killDriver):
        # Defines whether the browser opens the takeover mode
        self.TakeoverMode = TakeoverMode
        # Defines whether the browser opens the privacy window
        self.chooseTraceless = chooseTraceless
        # Defines the browser window size
        self.maxWindow = maxWindow
        # Define manual shutdown of driver background residue
        self.killDriver = killDriver

    # Functional interface
    def chrome_Takeover_auto(self):
        print("""
        ----------------------个性化设定项(Personalization Settings)-----------------------------------------------
                            示例(example):
        TakeoverChrome(TakeoverMode='y', chooseTraceless='y', maxWindow='y', killDriver='n')
            CH:接管开启,无痕开启,最大化窗口开启,自动清理驱动后台
            EN:Take over open, no trace open, maximization window open, automatic cleaning driver background
            CH:y为开启,非y为不启用(其他值默认为不启用)
            EN:The y is open, non-y is not enabled (other values are not enabled by default)
            CH:TakeoverMode='y'时需要调用opinion_Takeover()方法
            EN:The opinion_Takeover() method needs to be called when TakeoverMode='y'
            CH:chooseTraceless='y'时需要调用opinion_traceless()方法
            EN:ChooseTraceless ='y' requires calling the opinion_traceless() method
            
        ---------------------------------------------------------------------------------------------------------       
        """)

    # *********************************Judgment area**************************************

    # Define default mode functionality (maximization and default window size)
    def opinion_default(self):

        if self.maxWindow.upper() == 'Y' and self.chooseTraceless.upper() != 'Y' \
                and self.TakeoverMode.upper() != 'Y':
            driver = webdriver.Chrome()
            # Maximum window
            largestWindow = driver.maximize_window()
            print('Window maximization succeeded')
        else:
            driver = webdriver.Chrome()
            largestWindow = ''
            print('Incorrect input window maximization failed')
        return driver

    # Define privacy patterns (including maximum Windows and default window sizes)
    def opinion_traceless(self):
        # Maximize privacy window
        if self.chooseTraceless.upper() == 'Y' and self.maxWindow.upper() == 'Y'\
                and self.TakeoverMode.upper() != 'Y':
            options = webdriver.ChromeOptions()
            options.add_argument('--incognito')
            driver = webdriver.Chrome(options=options)
            largestWindow = driver.maximize_window()
            print('Windows open in privacy mode and maximize the window')

        # Default size privacy window
        elif self.chooseTraceless.upper() == 'Y' and self.maxWindow.upper() != 'Y'\
                and self.TakeoverMode.upper() != 'Y':
            options = webdriver.ChromeOptions()
            options.add_argument('--incognito')
            driver = webdriver.Chrome(options=options)
            print('The window is open in privacy mode, and the window size is the default')

        # Default Window default size
        else:
            driver = webdriver.Chrome()
            print('The input is incorrect and the browser opens in default mode')
        return driver

    # Define takeover mode capabilities
    def opinion_Takeover(self):
        # Maximizes traceless window takeover mode
        if self.chooseTraceless.upper() == 'Y' \
                and self.maxWindow.upper() == 'Y' \
                and self.TakeoverMode.upper() == 'Y':
            options = webdriver.ChromeOptions()
            # You need to start the debug mode command in the CMD: chrome url -remote-debugging-port=9515 --incognito
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")
            options.add_argument('--incognito')
            driver = webdriver.Chrome(options=options)
            largestWindow = driver.maximize_window()
            print('The window opens with the automatic mode of privacy takeover and the window is maximized')
            return driver
        # The default window size of the privacy window
        elif self.chooseTraceless.upper() == 'Y' and self.TakeoverMode.upper() == 'Y' \
                and self.maxWindow.upper() != 'Y':
            options = webdriver.ChromeOptions()
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")
            options.add_argument('--incognito')
            driver = webdriver.Chrome(options=options)
            print('The window opens with the automatic mode of privacy takeover and the window size is the default')
            return driver
        # Maximize window takeover automation mode
        elif self.maxWindow.upper() == 'Y' and self.TakeoverMode.upper() == 'Y' \
                and self.chooseTraceless.upper() != 'Y':
            options = webdriver.ChromeOptions()
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")
            driver = webdriver.Chrome(options=options)
            largestWindow = driver.maximize_window()
            print('The automation mode of the maximum window takeover is opened and the window is maximized')
            return driver
        # Automatic mode of non-privacy takeover by default window size
        elif self.TakeoverMode.upper() == 'Y' and self.maxWindow.upper() != 'Y' \
                and self.chooseTraceless.upper() != 'Y':
            options = webdriver.ChromeOptions()
            # You need to start the debug mode command in the CMD: chrome -remote-debugging-port=9515
            options.add_experimental_option("debuggerAddress", "127.0.0.1:9515")
            driver = webdriver.Chrome(options=options)
            print('The automatic mode of the default window size takeover opens, the window size is the default')
            return driver
        # Default window
        else:
            driver = webdriver.Chrome()
            largestWindow = ''
            print('The input error maximizes failure and opens in default mode')
            return driver

    # Define the code input control drive exit function
    def opinion_quit(self, driver):
        # Confirm manual shutdown drive or automatic shutdown drive
        print("You have just entered the cleanup driver residue by command")
        if self.killDriver.upper() == 'Y':
            print("You have selected to manually exit the driver. Please manually end the WebDriver "
                  "driver through the task manager")
            # Definition shutdown drive
            exitDriver = driver.quit()
            print('The residual background WebDriver driver has been stopped')
        else:
            print('Auto Shutdown is selected after 5S delay')
            sleep(5)
            exitDriver = driver.quit()
            print('The WebDriver driver is shut down')


