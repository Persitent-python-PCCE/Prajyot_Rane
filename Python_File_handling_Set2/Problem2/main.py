from redaction_config import SENSITIVE
import re

with open("report.txt","r") as file:
    replace_per_item={}
    text=file.read()
    for i in SENSITIVE:
        text,count = re.subn(i,"[REDACTED]",text,flags=re.IGNORECASE)
        replace_per_item[i]=count

print("-- report_redacted.txt --")
print(text)

print("-- console --")
print("Redaction complete.")
for key,value in replace_per_item.items():
    print(f"{key} -->{value} occurrences redacted")
print("Output saved to report_redacted.txt")

with open("report_redacted.txt","w") as file:
    file.write(text)
    for key,value in replace_per_item.items():
        file.write(f"{key} -->{value} occurrences redacted")
