import time
import sys

#gets from the user what to do either "start" or "stop" or "sta" or "sto"
arg = sys.argv[1:]
try:
    instruction = arg[0]
except:
    instruction = "help"
    # mode can either be "b" or "r" for for which it desides wether to keep runnign or not
try:
    mode = arg[1]
except:
    mode = "b"

#opens or creates a new csv file
try:
    file = open("output.csv","r")
    file_text = file.read()
    file.close()
    file_line_by = file_text.strip()
    file_line_by = file_line_by.split("\n")
    file_line_by_line = []
    for i in range(len(file_line_by)):
        file_line_by_line.append( file_line_by[i].split(","))
except:
    file_line_by = " "
    file_text = ""

file = open("output.csv","w")


timern = time.localtime(time.time())


text = "Start_min,Start_hr,Start_date,Index,Stop_min,Stop_hr,Stop_date,Time_Elapsed_min,Time_Elapsed_hr,Total_Today_min"

#making sure that the titles are correct
if file_line_by[0] != text:
    print(text,file = file)
    print("Error occured, heading dosn't match the reqierd heading, moving old content to output(1).csv and replasing")
    f = open("output(1).csv","w")
    print(file_text,file = f)
    f.close()
    sys.exit()
else:
    is_good = True

if instruction.lower() in ["start","sta"]:
    file_line_by.append(f"{timern.tm_min},{timern.tm_hour},{timern.tm_mday}-{timern.tm_mon}-{timern.tm_year},{pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year)}")
    print(f"Started at: {timern.tm_hour}:{timern.tm_min:0>2}\nDate: {timern.tm_mday}-{timern.tm_mon}-{timern.tm_year}\nID_date = {pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year)}")
if instruction.lower() in ["stop","sto"] and len(file_line_by_line[-1]) != len(file_line_by_line[0]):
    delta_t = timern.tm_min -int(file_line_by_line[-1][0]) + 60*(timern.tm_hour - int(file_line_by_line[-1][1]))
    file_line_by[-1] = file_line_by[-1]+ f",{timern.tm_min},{timern.tm_hour},{timern.tm_mday}-{timern.tm_mon}-{timern.tm_year},{delta_t},{delta_t/60}"
    time_tody = []
    tot_time = 0
    for i in file_line_by_line:
        if i[2] == f"{timern.tm_mday}-{timern.tm_mon}-{timern.tm_year}":
            time_tody.append(i)
    for i in time_tody:
        try:
            tot_time += int(i[7])
        except:
            pass
    tot_time += float(file_line_by[-1].split(",")[-2])
    file_line_by[-1] = file_line_by[-1] + f",{tot_time}"
    print(f'''Started at: {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2}
Date: {timern.tm_mday}-{timern.tm_mon}-{timern.tm_year}
ID_date = {pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year)}
Finished at: {timern.tm_hour}:{timern.tm_min:0>2}
Time Studied: {delta_t} min
Total Studied today: {tot_time} min
''')
if instruction.lower() in ["time", "time studied", "t"]:
    if len(file_line_by_line[-1]) != len(file_line_by_line[0]):
        delta_t = timern.tm_min -int(file_line_by_line[-1][0]) + 60*(timern.tm_hour - int(file_line_by_line[-1][1]))
        print(f"Studuing Right now\nTimes studed: {delta_t} min")
    else:
        time_tody = []
        tot_time = 0
        for i in file_line_by_line:
            if i[2] == f"{timern.tm_mday}-{timern.tm_mon}-{timern.tm_year}":
                time_tody.append(i)
        for i in time_tody:
            try:
                tot_time += int(i[7])
            except:
                pass
        tot_time += float(file_line_by[-1].split(",")[-2])
        print(f"Finished studieng,\nLast Study Sesion was at {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2} to {file_line_by_line[-1][5]}:{file_line_by_line[-1][4]:0>2}\nStudied for {file_line_by_line[-1][7]} min\nCumulative Time: {file_line_by_line[-1][9]} min")
if instruction.lower() in ["sum", "summary", "s"]:
    if len(file_line_by_line[-1]) != len(file_line_by_line[0]):
        delta_t = timern.tm_min -int(file_line_by_line[-1][0]) + 60*(timern.tm_hour - int(file_line_by_line[-1][1]))
        print(f"Currently studieng,\nLast Study Sesion was at {file_line_by_line[-2][1]}:{file_line_by_line[-2][0]:0>2} to {file_line_by_line[-2][5]}:{file_line_by_line[-2][4]:0>2}\nThis session stated at: {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2}\nStuding for {delta_t} min\nCumulative Time: {file_line_by_line[-2][9]} min")
    else:
        print(f"Finished studieng,\nLast Study Sesion was at {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2} to {file_line_by_line[-1][5]}:{file_line_by_line[-1][4]:0>2}\nStudied for {file_line_by_line[-1][7]} min\nCumulative Time: {file_line_by_line[-1][9]} min")
if instruction.lower() in ["help", "?"]:
    print("Either the the user did not imput a extra charicter or the user typed in \"help\" or \"?\"")
    print('''Command | What it dose
--------|------------------------------------------------------------------------------
start   |Begins a new timer
stop    | Ends the currently running timer
?       | Help, dyspalys the helps screan
summary | Summerises the current and/or last timer
data    | Dysplayes all the users previousely stored data in output.csv
time    | Displayes the current study timer, if not studing, will produce same as sum
''')
if instruction.lower() in ["data"]:
    length_needed = []
    for i in file_line_by_line[0]:
        length_needed.append(len(i))
    length_needed[8] += 6
    for i in file_line_by_line:
        for n in range(len(i)):
            print(str(i[n])+" "*(length_needed[n]-len(str(i[n]))),"|",end = "")       
        print()


if is_good:
    for i in range(len(file_line_by)):
        if i < len(file_line_by) - 1:
            print(file_line_by[i],file= file)
        else:
            print(file_line_by[i],file= file,end = "")

file.close()