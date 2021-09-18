divisive = []
for num in range(0, 100):
    if num % 5 == 0:
        divisive.append(num)
cube = []
for number in divisive:
    cube.append(number**3)
print(divisive)
print(cube)
