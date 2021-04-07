import json

active = dict()

with open("./cogs/cmds/cmd_utils/sgp4/active_elements.txt", "r") as file:
    counter = 0
    current = ""
    for line in file:
        if counter == 0:
            current = line.strip()
            active[current] = {}            
        elif counter == 1:
            active[current]["s"] = line.strip()
        elif counter == 2:
            active[current]["t"] = line.strip()
        counter += 1
        if counter > 2:
            counter = 0
        print(counter)

with open("./cogs/cmds/cmd_utils/sgp4/active_satellites.json", "w") as file:
    json.dump(active, file)

print("Done")
        
