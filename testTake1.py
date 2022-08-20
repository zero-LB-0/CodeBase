from TakeoverModeAuto import TakeoverMode_ChromeAuto as TmCa
from TakeoverModeAuto.TakeoverMode_ChromeAuto import TakeoverChrome

# This is an example of calling a procedure
"""
TakeoverChrome(TakeoverMode='y', chooseTraceless='y', maxWindow='y', killDriver='n')
Open takeover mode set TakeoverMode='y',No trace mode on set chooseTraceless='y'
open Maximize window set maxWindow='y'
Automatically delay the closure of the Selenium process set killDriver='n'
"""
setting = TakeoverChrome(TakeoverMode='y', chooseTraceless='y', maxWindow='y', killDriver='n')
# Invokes the plug-in launch screen
setting.chrome_Takeover_auto()
# Call the takeover mode to execute the driver
driver = setting.opinion_Takeover()
"""Send the test's url. if this is the case where the connection is required, 
the url is in line with the input in the browser"""
driver.get('https://www.baidu.com/')
# The use of the takeover mode requires selenium4.1 and  version above selenium4.1
driver.find_element(TmCa.By.ID, 'kw').send_keys('123')
driver.find_element(TmCa.By.ID, 'su').click()
driver.close()
# Use the auto-exit process function (not needed here, written to avoid missing driver.quit)
setting.opinion_quit(driver)
