file = open('input.txt', 'r')
masses = file.readlines()
fuel = 0
add_fuel = 0
for i in masses:
    value = int(int(i)/3)-2
    fuel += value
    while value > 0:
        add_fuel += value
        value = int(int(value)/3)-2
print(add_fuel)