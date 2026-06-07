import time
import sys
import math

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
    mode = None

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
text = "Start_min,Start_hr,Start_date,Index,Stop_min,Stop_hr,Stop_date,Delta_min,Delta_hr,Total_day_min"
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


if instruction.lower() in ["start","sta"] and len(file_line_by_line[-1]) == len(file_line_by_line[0]):
    file_line_by.append(f"{timern.tm_min},{timern.tm_hour},{timern.tm_mday}-{timern.tm_mon}-{timern.tm_year},{pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year)}")
    print(f'''Started at: {timern.tm_hour}:{timern.tm_min:0>2}
Date: {timern.tm_mday}-{timern.tm_mon}-{timern.tm_year}
ID_date = {pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year)}''')
    

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
Time Studied: {math.floor(delta_t/60)}:{delta_t%60:0>2}
Total Studied today: {math.floor(tot_time/60)}:{tot_time%60:0>2}
''')
    

if instruction.lower() in ["time", "time studied", "t"]:
    if len(file_line_by_line[-1]) != len(file_line_by_line[0]):
        delta_t = timern.tm_min -int(file_line_by_line[-1][0]) + 60*(timern.tm_hour - int(file_line_by_line[-1][1]))
        print(f'''Studuing Right now,
Times studed: {timern.tm_hour - int(file_line_by_line[-1][1])}:{timern.tm_min -int(file_line_by_line[-1][0]):0>2} ''')
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
        delta_t = (int(file_line_by_line[-1][5]) - int(file_line_by_line[-1][1]))*60 + int(file_line_by_line[-1][4]) -int(file_line_by_line[-1][0])
        print(f'''Finished studieng,
Last Study Sesion was at {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2} to {file_line_by_line[-1][5]}:{file_line_by_line[-1][4]:0>2}
Studied for {math.floor(delta_t/60)}:{delta_t%60:0>2} 
Cumulative Time: {math.floor(float(file_line_by_line[-1][9])/60)}:{float(file_line_by_line[-1][9])%60:0>2} 
''')
if instruction.lower() in ["sum", "summary", "s"]:
    if len(file_line_by_line[-1]) != len(file_line_by_line[0]):
        delta_t = timern.tm_min -int(file_line_by_line[-1][0]) + 60*(timern.tm_hour - int(file_line_by_line[-1][1]))
        print(f'''Currently studieng,
Last Study Sesion was at {file_line_by_line[-2][1]}:{file_line_by_line[-2][0]:0>2} to {file_line_by_line[-2][5]}:{file_line_by_line[-2][4]:0>2}
This session stated at: {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2}
Studing for {math.floor(delta_t/60)}:{delta_t%60:0>2}
Cumulative Time: {math.floor((float(file_line_by_line[-2][9]) + delta_t)/60)}:{(float(file_line_by_line[-2][9]) + delta_t)%60:0>2} ''')
    else:
        delta_t = (int(file_line_by_line[-1][5]) - int(file_line_by_line[-1][1]))*60 + int(file_line_by_line[-1][4]) -int(file_line_by_line[-1][0])
        print(f'''Finished studieng,
Last Study Sesion was at {file_line_by_line[-1][1]}:{file_line_by_line[-1][0]:0>2} to {file_line_by_line[-1][5]}:{file_line_by_line[-1][4]:0>2}
Studied for : {math.floor(delta_t/60)}:{delta_t%60}
Cumulative Time: {math.floor(float(file_line_by_line[-1][9])/60)}:{float(file_line_by_line[-1][9])%60:0>2}
''')
        

if instruction.lower() in ["help", "?"]:
    print()
    print("     HELLO AND WELLCOME TO THE STUDING THING!!!\n")
    print("The following is a list of command arguments that can be added to the end of the \n\"python3 hi.py\" call that can be used to make this program do spesific things")
    print('''\nArgument |Short Cut | What it dose
---------|----------|------------------------------------------------------------------------------
start    |sta       | Begins a new timer
stop     |sto       | Ends the currently running timer
help     |?         | Help, dyspalys the helps screan
summary  |s         | Summerises the current and/or last timer
data     |d         | Dysplayes all the users previousely stored data in output.csv
time     |t         | Displayes the current study timer, if not studing, will produce same as sum
''')
    

if instruction.lower() in ["data", "d"]:
    print()
    lines = []
    if mode == None:
        lines = [i for i in file_line_by_line if i != file_line_by_line[0] ]
    if mode in ["t", "today"]:
        for i in file_line_by_line:
            try:
                if int(i[3]) == pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year):
                    lines.append(i)
            except:
                pass

    length_needed = []
    for i in file_line_by_line[0]:
        length_needed.append(len(i))
    spasing = []
    length_needed[8] += 11
    for i in length_needed:
        try:
            spasing.append(spasing[-1] + i + 2)
        except:
            spasing.append( i + 1)
    for n in range(len(file_line_by_line[0])):
        print(str(file_line_by_line[0][n])+" "*(length_needed[n]-len(str(file_line_by_line[0][n]))),"|",end = "")
    print()
    for h in range(spasing[-1]+1):
        if h in spasing:
            print("|",end = "")
        else:
            print("-",end = "")
    print()

    for i in lines:
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