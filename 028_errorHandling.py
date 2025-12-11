# error handling using try and except:

def divis(a, b):
    try:
        result = a/b
        print("result: ", result)
        return result
    except ZeroDivisionError:
        print("denominator cannot be zero!")
    except Exception as e:
        print(f"another error in returning, e = {e}")
        return 0
    
def getNums():
    try:
        a = int(input("please enter the numerator:"))
        b = int(input("please enter the denominator:"))
        return a, b
    except:
        print("numerator and denominator should be numbers!")
        return None, None

def main():
    while 1:
        n , d = getNums()
        if n == None:
            continue
        
        divis(n , d)

    return 0
main()