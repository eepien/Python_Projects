# Create a function called find_max: finds the max from a list of numbers
# Post the function in a converter called utils
# Use the converter to find the max of numbers from a list.

#import utils               #looks like this line is optional if we are using from
from utils import find_max
numbers = [10, 35, 6, 8, 100,201, 11, 32, 4, 1, 5]
max_numb = find_max(numbers)  # max is a build in maximum function, so we avoid over-writing it.
print(max_numb)