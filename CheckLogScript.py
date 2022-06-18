count_dict = {'U-Boot': 0,
              '[ERROR ] 416,gsensor.c :gsensor get data failed!': 0,
              'Audio chan 9 play, uAudioID = [33], volume = [8]': 0,
              'Audio chan 9 play, uAudioID = [34], volume = [8]': 0,
              'Audio chan 9 play, uAudioID = [40], volume = [8]': 0,
              'Audio chan 9 play, uAudioID = [41], volume = [8]': 0,
              'Media 0 ok!': 0,
              'upgrading... -1%': 0,
              'upgrading... 0%': 0,
              'upgrading... 100%': 0,
              'Starting kernel ...': 0,

              }
count_dict_keysList = ['U-Boot',
                       'Audio chan 9 play, uAudioID = [33], volume = [8]',
                       'Audio chan 9 play, uAudioID = [34], volume = [8]',
                       'Audio chan 9 play, uAudioID = [40], volume = [8]',
                       'Audio chan 9 play, uAudioID = [41], volume = [8]',
                       'Media 0 ok!',
                       'upgrading... -1%',
                       'upgrading... 0%',
                       'upgrading... 100%',
                       'Starting kernel ...'

                       ]
directory = input("Enter the folder path, for example: C:\\Users\\Desktop\\9\\29\\")
port_input = input("Enter the port name for easy identification, for example: 8")
join_filename = "port" + str(port_input) + "-"
# Define a file suffix
file_Suffix = input("Enter the path file name suffix:.txt or .log")
# Define the number of times a file is opened traversal open file (interval determined by start and end date)
inputStartDay = int(input("Enter the number 1-31 based on the date of the month:"))
inputEndDay = int(input("Enter the number 1-31 based on the date of the month:"))
# Define the log name date part of the field
inputLogDate = input("Input date and month, such as 2022-06 or 202206':")
for number in range(inputStartDay, inputEndDay + 1):
    filePath_LT10 = directory + join_filename + str(inputLogDate) + "-0" + str(number) + str(file_Suffix)
    filePath_GT10 = directory + join_filename + str(inputLogDate) + "-" + str(number) + str(file_Suffix)
    filePath_Txt = directory + join_filename + str(inputLogDate) + "-" + str(number) + ".txt"
    filePath_Log = directory + join_filename + str(inputLogDate) + "-" + str(number) + ".log"

    if number < 10:
        if file_Suffix in filePath_LT10:
            f = open(file=filePath_LT10, mode='rb')
            f_str = f.read()
            # Cast encoding format
            shiftCode = f_str.decode(encoding='utf-8', errors='ignore')
            for i in count_dict.keys():
                count_dict[i] = shiftCode.count(i)

            # Closing log files
            f.close()
            print("File location: {}, check statistics {} :".format(filePath_LT10, count_dict))
            ii = 0
            for i in range(0, 11):
                if i == 0:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("Restart without exception [u-boot]")
                    else:
                        print("There is abnormal restart {} [U-boot], and the log part appears :{}"
                              .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i]))
                elif i < 5:
                    ii += 1
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("No fatigue driving trigger type{}".format(ii))
                    else:
                        print("Fatigue driving triggers {} times, and the log part appears:\t{}\t"
                              .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i]))
                elif i == 5:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("The storage media is properly mounted")
                    else:
                        print(
                            "Storage media mount exception {} times, log part appears :{}"
                            .format(
                                count_dict[count_dict_keysList[i]], count_dict_keysList[i])
                        )
                elif i < 9:
                    if count_dict[count_dict_keysList[6]] == 0 \
                            and count_dict[count_dict_keysList[7]] == count_dict[count_dict_keysList[8]]:
                        print("no\t'{}'\tis displayed, the upgrade is successful\t".format(count_dict_keysList[i]))
                    else:
                        print("'{}'\tThe upgrade failed {} times \t Log part appears:{} \t"
                              .format(count_dict_keysList[i], count_dict[count_dict_keysList[i]] - 1,
                                      count_dict_keysList[i])
                              )
                elif i == 9:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("The new GB device does not restart abnormally")
                    else:
                        print(
                            "The new GB device abnormally restarts {} times, and the log part appears :{}"
                            .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i]))
                else:
                    pass
        else:
            pass

    else:
        if file_Suffix in filePath_GT10:
            f1 = open(file=filePath_GT10, mode='rb')
            f_str1 = f1.read()
            # Cast encoding format
            shiftCode = f_str1.decode(encoding='utf-8', errors='ignore')
            for i in count_dict.keys():
                count_dict[i] = shiftCode.count(i)
            # Closing log files
            f1.close()
            print("File location: {}, check statistics {} :".format(filePath_GT10, count_dict))
            ii = 0
            for i in range(0, 11):
                if i == 0:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("Restart without exception [u-boot]")
                    else:
                        print("There is abnormal restart {} [U-boot], and the log part appears :{}"
                              .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i])
                              )
                elif i < 5:
                    ii += 1
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("No fatigue driving trigger type{}".format(ii))
                    else:
                        print("Fatigue driving triggers {} times, and the log part appears:\t{}\t"
                              .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i]))
                elif i == 5:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("The storage media is properly mounted")
                    else:
                        print(
                            "Storage media mount exception {} times, log part appears :{}"
                            .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i]))
                elif i < 9:
                    if count_dict[count_dict_keysList[6]] == 0 \
                            and count_dict[count_dict_keysList[7]] == count_dict[count_dict_keysList[8]]:
                        print("no\t'{}'\tis displayed, the upgrade is successful\t".format(count_dict_keysList[i]))
                    else:
                        print("'{}'\tThe upgrade failed {} times \t Log part appears:{} \t"
                              .format(count_dict_keysList[i], count_dict[count_dict_keysList[i]] - 1,
                                      count_dict_keysList[i])
                              )
                elif i == 9:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("The new GB device does not restart abnormally")
                    else:
                        print(
                            "The new GB device abnormally restarts {} times, and the log part appears :{}"
                            .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i])
                        )
                else:
                    pass
        elif file_Suffix in filePath_Log:
            f2 = open(file=filePath_Log, mode='rb')
            f_str2 = f2.read()
            # Cast encoding format
            shiftCode = f_str2.decode(encoding='utf-8', errors='ignore')
            for i in count_dict.keys():
                count_dict[i] = shiftCode.count(i)
            # Closing log files
            f2.close()
            print("File location: {}, check statistics {} :".format(filePath_Log, count_dict))
            ii = 0
            for i in range(0, 11):
                if i == 0:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("Restart without exception [u-boot]")
                    else:
                        print("There is abnormal restart {} [U-boot], and the log part appears :{}"
                              .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i])
                              )
                elif i < 5:
                    ii += 1
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("No fatigue driving trigger type{}".format(ii))
                    else:
                        print("Fatigue driving triggers {} times, and the log part appears:\t{}\t"
                              .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i]))
                elif i == 5:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("The storage media is properly mounted")
                    else:
                        print(
                            "Storage media mount exception {} times, log part appears :{}"
                            .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i])
                        )
                elif i < 9:
                    if count_dict[count_dict_keysList[6]] == 0 \
                            and count_dict[count_dict_keysList[7]] == count_dict[count_dict_keysList[8]]:
                        print("no\t'{}'\tis displayed, the upgrade is successful\t".format(count_dict_keysList[i]))
                    else:
                        print("'{}'\tThe upgrade failed {} times \t Log part appears:{} \t".format(
                            count_dict_keysList[i], count_dict[count_dict_keysList[i]] - 1, count_dict_keysList[i]
                        )
                        )
                elif i == 9:
                    if count_dict[count_dict_keysList[i]] == 0:
                        print("The new GB device does not restart abnormally")
                    else:
                        print(
                            "The new GB device abnormally restarts {} times, and the log part appears :{}"
                            .format(count_dict[count_dict_keysList[i]], count_dict_keysList[i])
                        )
                else:
                    pass
        else:
            print("The log file format suffix must be log or TXT.")
