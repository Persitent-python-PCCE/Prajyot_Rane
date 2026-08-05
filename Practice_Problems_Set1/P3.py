goblin=["Queens", "Manhattan","Brooklyn", "Bronx"]
octopus= ["Manhattan", "Brooklyn","Harlem"]
vulture=["Manhattan", "Bronx","Harlem"]

g=set(goblin)
o=set(octopus)
v=set(vulture)
combine_to_find_Common=g & o & v
combine_to_find_Common2=g | o | v
count=len(combine_to_find_Common2)
inter=set.intersection(combine_to_find_Common)
exactly_one=(g-o-v) | (o-g-v) | (v-g-o)
print(inter)
print(exactly_one)
print(count)

