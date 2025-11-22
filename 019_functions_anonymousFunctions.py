# mapping concept:

def multiply2 (x):                          # gets a parameter and multiplies it by 2
    return x * 2

my_list = [0, 1, 2, 3, 4, 5, 6]
multiplied_2 = map(multiply2, my_list)      # runs 'multiply2' function on every element of my_list


# naonymous functions('lambda' functions in python)
multiplied_3 = map(lambda x: x * 3, my_list)    # runs the lambda function on every element of my_list
                                                # (gets x and returns x * 3)

 