def adventHash(step) :
    currentValue = 0
    for ch in step:
        currentValue = ((currentValue + ord(ch)) * 17) % 256
    return currentValue


matrice = []
with open("day15/input.txt", 'r') as file:
    data = file.read().replace('\n', '')
steps = data.split(',')
# print(steps)

output = 0
for step in steps:
    output += adventHash(step)
print(output)
# 505379