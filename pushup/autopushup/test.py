starting_point = 1
ending_point = 224.2296679816934
num_divisions = 225

step = (30 - starting_point) / (num_divisions - 1)
array = [starting_point + step * i for i in range(num_divisions)]

print(array)
print(len(array))

for i in range(255):
    print(-array[i])