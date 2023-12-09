def prossimoNumero ( history):
    prossimaRiga = []
    fine = True
    for n in range (len(history)-1):
        prossimaRiga.append(history[n+1] - history[n])
        if history[n+1] - history[n] != 0:   
            fine = False
    if fine :
        return history[-1] + 0
    else :
        return history[-1] + prossimoNumero(prossimaRiga)


file = "day9/input.txt"
output = 0
with open(file, 'r+') as f:
    for idx, line in enumerate (f):
        history = [int(num) for num in line.split()]
        output += prossimoNumero(history)
print(output)
# 2105961943




