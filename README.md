# CodeBase
## CheckLogScript V1.0.0

### Script statement

1. Please do not make the input field of the dead verification script, because the author is too lazy to write the check

2. This is just a common log check script, test  small white writing do not spray, there are big guys can help improve

3. This time uses a process-oriented script without encapsulation

4. Running the script will convert the file encoding to 'UTF-8' format for checking

5. The script can batch query logs of only one month, for example, January in the logs of January and February

### Script Instructions

#### Input module

1. 'directory' is the identifier entered in the path of the receiving folder

2. 'port_input' is the name of the receiving port, which is an optional identifier depending on the format of the log file name

3. 'join_filename' indicates the identifier of the splicing filename. You need to change it according to the log name

4. 'file_Suffix' is used to receive identifiers with file names such as. TXT

5. 'inputStartDay 'The identifier used to receive the date and the input of this unit of number

6. 'inputEndDay 'is the identifier used to receive the date and the input of this unit number

7. The identifiers 'inputStartDay 'and 'inputEndDay' should be entered with caution that 'inputStartDay' is less than 'inputEndDay'.

8. 'inputLogDate' indicates the id of the received date. Enter the date in the log name

#### Statistics data access module

1. 'count_dict' stores data in a dictionary format, that is, the keyword to be queried in the log. The number of occurrences of the keyword is compared

2. 'count_dict_keysList' is used to access key word entries in the dictionary in list format, which must correspond to the entries in the dictionary

## TakeOverTheAutoPluginInChrome V1.0

### Plugin function:



1. When using Selenium in Chrome, open the privacy window



2. Chrome browser is opened using Selenium takeover mode (no display is being performed through automation)



3. Open the default Selenium window in Chrome



4. Initial beautification of the startup interface



5. Automatically exit the driver after a delay



6. No need to guide Selenium packages







### Instructions:



#### Mode Selection



Ex. :



- TakeoverChrome(TakeoverMode='y', chooseTraceless='y', maxWindow='y', killDriver='n')



- y indicates on,n indicates off, and all other character types are off




- TakeoverMode indicates whether the TakeoverMode option is enabled



- chooseTraceless indicates whether the traceless mode option is enabled



- maxWindow Indicates whether the maximization window option is enabled



- killDriver Indicates whether to manually shut down the device. Y indicates manual shutdown. N indicates automatic shutdown (5s delay).



- The sequence of use is startup interface, takeover/no trace, automatic exit from the driver



- Code sequence can be found in testtake1.py



- Code writing order



1. chrome_Takeover_auto()



2. Opinion_traceless () or opinion_Takeover ()



3. opinion_quit(driver)



Note :opinion_Takeover() is in takeover mode



Opinion_traceless () is the private mode, which does not take over the automated operation mode











#### Startup interface



To use the startup screen, call chrome_Takeover_auto()







#### Privacy Mode



1. Opinion_Takeover () is required to use takeover mode.

2. In takeover mode, run the CMD command to enable the debug mode

3. Take over the traceless start

- chrome url -remote-debugging-port=9515 --incognito
  - Port number Enter Chromedriver in CMD to view the port number

  - URL must also be the same as the URL in driver.get(URL)


4. Take over the non-private startup

- chrome url -remote-debugging-port=9515
  - Port number Enter Chromedriver in CMD to view the port number

  - URL must also be the same as the URL in driver.get(URL)


5. The takeover mode requires Selenium4. 4.4.0 is recommended







#### No trace mode



1. Opinion_traceless () is required to use the traceless mode.

2. This is compatible with Selenium3 and Selenium4

3. You do not need to enter the URL manually







#### Automatically exits the driver



1. Using the automatic exit driver is optional

2. Run the opinion_quit(driver) command



Note :TakeoverModeAuto package is under the plug-in






















                            Author: Once script kid (zero-LB-0)
