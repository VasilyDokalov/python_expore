total=0
for x in range(1, 10):
    for y in range(1, 20):
        for z in range(1, 200):
            if 10 * x + 5 * y + 0.5 * z == 100 and x + y + z == 100:
                total+=1
                print(x, y, z)
print(total)               
