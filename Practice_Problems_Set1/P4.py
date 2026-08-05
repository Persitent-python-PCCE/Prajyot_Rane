targets=[["Falcon", 34.05, -118.24],["Falcon", 99.9, 12.0],["Condor", 40.71, -74.00]]
valid_targets=[]
print("Invalid targets:")
for i in range(len(targets)):
        if targets[i][1]>90 or targets[i][2]>180:
            valid_targets.append(targets[i])
        else:
              print(f"{targets[i]},")
print("valid targets")
print(valid_targets)            


    
