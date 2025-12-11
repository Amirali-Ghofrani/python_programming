def hoopGame(x, y):  
    x, y = int(x), int(y)       # gets 2 parameters and returns a list of hoop game!
    nums = []
    for i in range (1, x + 1):
        if i % y == 0:
            nums.append("hoop!")
        else:
            nums.append(i)
    return nums

if __name__ == "__main__":
    print("testing the package module...!")
