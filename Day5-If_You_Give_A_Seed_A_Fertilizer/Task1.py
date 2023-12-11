

def Map(val, array):
    for option in array:
        if option[0][0] <= val <= option[0][1]:
            return option[1] + (val - option[0][0])
    return val


seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
minRes = 1000000000000


f = open("./input.txt")
seeds = tuple([int(x) for x in f.readline()[7:].split()])
f.readline()
f.readline()

line = f.readline().split()
while len(line) > 0:
    seed_to_soil_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()
    
f.readline()
line = f.readline().split()
while len(line) > 0:
    soil_to_fertilizer_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()

f.readline()
line = f.readline().split()
while len(line) > 0:
    fertilizer_to_water_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()

f.readline()
line = f.readline().split()
while len(line) > 0:
    water_to_light_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()

f.readline()
line = f.readline().split()
while len(line) > 0:
    light_to_temperature_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()

f.readline()
line = f.readline().split()
while len(line) > 0:
    temperature_to_humidity_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()

f.readline()
line = f.readline().split()
while len(line) > 0:
    humidity_to_location_map.append([(int(line[1]), int(line[1]) + int(line[2]) - 1), 
                            int(line[0])])
    line = f.readline().split()

print(seed_to_soil_map)
print(soil_to_fertilizer_map)
print(fertilizer_to_water_map)
print(water_to_light_map)
print(light_to_temperature_map)
print(temperature_to_humidity_map)
print(humidity_to_location_map)

for seed in seeds:
    v = seed
    print(v)
    v = Map(v, seed_to_soil_map)
    print("soil: ", v)
    v = Map(v, soil_to_fertilizer_map)
    print("fertilizer: ", v)
    v = Map(v, fertilizer_to_water_map)
    print("water: ", v)
    v = Map(v, water_to_light_map)
    print("light: ", v)
    v = Map(v, light_to_temperature_map)
    print("temperature: ", v)
    v = Map(v, temperature_to_humidity_map)
    print("humidity: ", v)
    v = Map(v, humidity_to_location_map)
    print("location: ", v)
    if v < minRes:
        minRes = v

print(minRes)
