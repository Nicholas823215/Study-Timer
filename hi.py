import time
import sys
import math
import help

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

try:
    var = arg[2]
except:
    var = 4

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
    help.help(mode)
        

if instruction.lower() in ["data", "d"]:
    print()
    lines = []
    if mode == None:
        lines = [i for i in file_line_by_line if i != file_line_by_line[0] ]
        mode = "None"
    if mode.lower() in ["t", "today"]:
        for i in file_line_by_line:
            try:
                if int(i[3]) == pow(2, timern.tm_mday)*pow(3, timern.tm_mon)&pow(5, timern.tm_year):
                    lines.append(i)
            except:
                pass
    if mode.lower() in ["c", "cummilative"]:
        n = None
        for i in [i for i in file_line_by_line if i != file_line_by_line[0] ]:
            if n == None:
                n = i
            if n[3] != i[3]:
                lines.append(n)
                n = i
            if float(n[-1]) < float(i[-1]):
                n = i
        lines.append(n)
    if mode.lower() in ["max"] or mode in ["M"]:
        n = None
        for i in [i for i in file_line_by_line if i != file_line_by_line[0] ]:
            if n == None:
                n = i
            if n[3] != i[3]:
                lines.append(n)
                n = i
            if float(n[7]) < float(i[7]):
                n = i
        lines.append(n)
    if mode.lower() in ["min"] or mode in ["m"]:
        n = None
        for i in [i for i in file_line_by_line if i != file_line_by_line[0] ]:
            if n == None:
                n = i
            if n[3] != i[3]:
                lines.append(n)
                n = i
            if float(n[7]) > float(i[7]):
                n = i
        lines.append(n)
            
            

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


if instruction.lower() in ["dis", "display"]:
    plot = []
    if mode in [None, "n", "None", "none", "Normal", "normal" ]:
        cutoff_time_ = time.time() - 604800 #604800 is sec in a week
    if mode.lower in ["a", "all"]:
        cutoff_time_ = 0
    cutoff_time = time.localtime(cutoff_time_) 
    
    date = [h[2].split("-") for h in file_line_by_line.copy()]
    date.pop(0)
    data = []
    for i in range(len(date)):
        if int(date[i][2]) > cutoff_time.tm_year:
            data.append(file_line_by_line[i+1])
        elif int(date[i][2]) < cutoff_time.tm_year:
            pass
        elif int(date[i][1]) > cutoff_time.tm_mon:
            data.append(file_line_by_line[i+1])
        elif int(date[i][1]) < cutoff_time.tm_mon:
            pass
        elif int(date[i][0]) >= cutoff_time.tm_mday:
            data.append(file_line_by_line[i+1])
    
    if len(file_line_by_line[-1]) != len(file_line_by_line[0]):
        data[-1].append(str(timern.tm_min))
        data[-1].append(str(timern.tm_hour))
        data[-1].append(f"{timern.tm_mday}-{timern.tm_mon}-{timern.tm_year}" )

    dates = [[],[],[],[],[],[],[],[]]
    dates_ = [(time.localtime(cutoff_time_ + 86400*i).tm_mday,time.localtime(cutoff_time_ + 86400*i).tm_mon, time.localtime(cutoff_time_ + 86400*i).tm_year)  for i in range(0,8)]
    
    n = 0
    for i in range(len(dates_)):
        while data[n][2].split("-") == [str(dates_[i][0]),str(dates_[i][1]),str(dates_[i][2])]:
            dates[i].append([int(data[n][1]) + int(data[n][0])/60,int(data[n][5]) + int(data[n][4])/60])
            if n < len(data)-1:
                n += 1
            else:
                break
    
    padding = int(var)
    print(" "*10,end="")
    for i in range(25):
        print( str(i)+ " "*(-len(str(i)) + padding+1),end="")
    print("\n"+"-"*9,end="")
    for i in range(25):
        if i == 0:
            print("||" + "-"*padding ,end="")
        elif i != 24:
            print("|" + "-"*padding ,end="")
        else:
            print("|")

    for i in range(len(dates)):
        for n in range(len(dates[i])):
            dates[i][n] = [round(dates[i][n][0]*(padding+1)), round(dates[i][n][1]*(padding+1))]

    for i in range(len(dates_)):
        print(f"{dates_[i][0]}-{dates_[i][1]}-{dates_[i][2]}"+" "*(9 - len(f"{dates_[i][0]}-{dates_[i][1]}-{dates_[i][2]}"))+"|",end = "")
        diff = []
        for n in range(len(dates[i])):
            if len(dates[i][n]) == 0:
                break
            elif len(dates[i][n]) == 1:
                diff = [dates[i][n][0]]
                break
            if n == 0:
                diff.append(dates[i][0][0])
            if n != 0:
                diff.append(dates[i][n][0] - dates[i][n-1][1])
            
        if diff != []:
            for n in range(len(diff)):
                print(" "*diff[n]+ "-"*(dates[i][n][1]- dates[i][n][0]), end = "")
        print("\n"+"-"*(9) + "|")
        diff = []

if is_good:
    for i in range(len(file_line_by)):
        if i < len(file_line_by) - 1:
            print(file_line_by[i],file= file)
        else:
            print(file_line_by[i],file= file,end = "")

file.close()