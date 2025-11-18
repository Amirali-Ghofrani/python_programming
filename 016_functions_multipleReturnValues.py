# the below function gets a list of numbers, and returns a list of odd numbers,
# the count of odd numbers and the count of total numbers all 3 as a tuple:

def myOdds(nums):
    odds_count = 0
    total_count = 0
    odd_nums = [] 
    for i in nums:
        if i % 2 == 1:
            odd_nums.append(i)
            odds_count += 1
        total_count += 1
    return  total_count, odds_count, odd_nums

def main():
    my_list = [0, 1, 6, 8, 10, 5, 7, 13, 15]

    total_count, odds_count, odds_list = myOdds(my_list)

    print(f"total count is: {total_count}\n"
          f"odds count is:{odds_count}\n"
          f"odd numbers are: {odds_list}")

main()