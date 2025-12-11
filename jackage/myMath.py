def isEven(x):              # chacks if a number is even or odd
    return x % 2 == 0


def cir(r, pi):           # gets redius and pi number and returns circle circumference
    cir = 2 * pi * r
    return r

def cirArea(r, pi):        # gets redius and pi number and returns circle area
    area = pi * r * r
    return area

if __name__ == "__main__":
    print("testing the package module...!")