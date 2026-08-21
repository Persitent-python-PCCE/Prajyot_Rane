targets=[("Falcon", 34.05, -118.24), ("Ghost",99.9, 12.0), ("Condor", 40.71, -74.00)]

valid_targets=[]
print("Invalid targets:")
for i in range(len(targets)):
        if targets[i][1]>90 or targets[i][2]>180:
             print(f"{targets[i]},")
        else:
               valid_targets.append(targets[i])
print("Briefing:(N->S):")
for i in range(len(valid_targets)):
       print(f"Lat:",valid_targets[i][0],"-->",valid_targets[i][1],"Lon:",valid_targets[i][2])

         


    
