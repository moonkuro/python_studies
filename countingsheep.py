def count_sheeps(sheep):
    sheepTrue = 0
    for n in sheep:
        if n == True:
            sheepTrue += n
    return sheepTrue
        
sheep = [True, True, True, False, False, True]
print(count_sheeps(sheep))