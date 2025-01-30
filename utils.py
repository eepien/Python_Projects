def find_max(num_list):
    max_num = num_list[0]  # max_num = 0 or any number will work as well.
    for number in num_list:
         if number > max_num:
             max_num = number
    return max_num
