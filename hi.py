import time
import sys

#gets from the user what to do either "start" or "stop" or "sta" or "sto"
arg = sys.argv[1:]
try:
    instruction = arg[0]
except:
    instruction = None
    # mode can either be "b" or "r" for for which it desides wether to keep runnign or not
try:
    mode = arg[1]
except:
    mode = "b"

#opens or creates a new csv file
file = open("output.csv","r")

# gets the current index
try:
    index = open("index.txt","r")
    ind = None
except:
    index = open("index.txt","w")
    ind = 2
if ind == None:
    for i in index.readlines():
        i = i.strip()
        try:
            if i[0] != "#":
                ind = int(i)
                break
        except:
            pass
index.close()

timern = time.localtime(time.time())

print(f"the current index of the csv file is: {ind}")

# prosessing the current data in output.csv
file_text = file.read()
file.close()
file = open("output.csv","w")
file_line_by = file_text.strip()
file_line_by = file_line_by.split("\n")
file_line_by_line = []
for i in range(len(file_line_by)):
    file_line_by_line.append( file_line_by[i].split(","))
print(file_line_by)

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




if is_good:
    for i in range(len(file_line_by)):
        if i < len(file_line_by) - 1:
            print(file_line_by[i],file= file)
        else:
            print(file_line_by[i],file= file,end = "")

file.close()