def parse_line(line):
    string_split=line.split(" ", 3)  #ALSO string_split=line.split(" ")
    level=string_split[2]
    message=string_split[3]  #ALSO     message=string_split[3:]
    return (level,message)


def read_logs(path):
    entries=[]
    with open(path,"r") as file:
        for line in file:
            line=line.strip()
            if line:
                entries.append(parse_line(line))
    return entries



            
            


