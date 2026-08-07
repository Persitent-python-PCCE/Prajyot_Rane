from log_utils import read_logs
from collections import Counter

entries=read_logs("app.log")
levels=[i[0] for i in entries]    
count=Counter(levels)
with open("log_summary.txt",'w') as file:
    print("=== Log Summary ===",file=file)
    print("INFO:    ",count["INFO"],",",file=file)
    print("WARNING:    ",count["WARNING"],",",file=file)
    print("ERROR:    ",count["ERROR"],",",file=file)
    print("DEBUG:    ",count["DEBUG"],",",file=file)

    print("Error Found:",file=file)
    for i in entries:
        if i[0]=="ERROR":
            print(i[1],file=file)




    



