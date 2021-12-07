file = open('input.txt', 'r')
masses = file.readlines()
fuel = 0
for i in masses:
    fuel += int(int(i)/3)-2
print(fuel)