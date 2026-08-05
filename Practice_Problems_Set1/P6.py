scores=[("Brazil", 2, 0, 0), ("Japan", 3, 2,0), ("Spain", 5, 0, 1), ("Ghana", 3, 1,2)]

groups=filter(lambda score:score[1]*3>=6 and score[3] <=1,scores)
group=list(groups)
print(f"Advancing to Knockouts:")
for teams,points,_,_ in group:
    print(" ",end=" ")
    print(f"{teams} - {points*3} pts")