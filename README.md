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
























                            Author: Once script kid (zero-LB-0)
