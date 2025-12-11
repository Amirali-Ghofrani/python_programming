# error handling using try and except:

# gets 2 arguments as numerator and denominator and returns a/b
def divis(a, b):
    try:                                 # it's better to have a smaller try block to be more percise in error detection
        result = a/b
    except ZeroDivisionError:
        print("denominator cannot be zero!")
        return 0
    except Exception as e:
        print(f"another error in returning, e = {e}")
        return 0
    else:                               # the else block runs in case that no exception occurs(follows the try block)
        print("result: ", result)
        return result
    finally:                                # the finally block runs anyway, even if there is a return value in above lines!
        print("this block runs anyway!!")   # finally block is run andd then the return value is returned 
    
    
# gets 2 numbers to be used as numerator and denominator 
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

# more built-in errors can be found in python.org 