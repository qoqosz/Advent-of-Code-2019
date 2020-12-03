# Problem 1
sum = 0

with open('day1-input.txt') as f:
    for line in f.readlines():
        num = int(line.strip())
        mass = int(num / 3) - 2
        sum = sum + mass
        
print(sum)

# Problem 2
sum = 0

with open('day1-input.txt') as f:
    for line in f.readlines():
        module_mass = int(line.strip())
        fuel_mass = module_mass
        
        while True:
            fuel_mass = fuel_mass // 3 - 2
            if fuel_mass <= 0:
                break
            sum += fuel_mass
            
print(sum)