
from collections import Counter

input_string = input("Please Enter a string : ")

frequency_per_char = Counter(input_string)


print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequency_per_char)))
