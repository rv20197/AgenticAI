import sys
from fractions import Fraction
from decimal import Decimal
# Real Numbers or Floating Point Numbers
# A real number is a number that can be represented on the number line. It includes both rational and irrational numbers. 
# In Python, real numbers are represented using the float data type.

ideal_temp = 85.5
print(f"The ideal temperature for brewing tea is {ideal_temp} degrees Celsius.")

current_temp = 80.49
print(f"The current temperature of the tea is {current_temp} degrees Celsius.")

temp_difference = ideal_temp - current_temp
print(f"The temperature difference is {temp_difference} degrees Celsius.")

# print(sys.float_info)

# Fraction
# A fraction is a way to represent a part of a whole. It consists of a numerator and a denominator. 
# In Python, you can use the Fraction class from the fractions module to represent fractions.

half_cup = Fraction(1, 2)
print(f"Half a cup of tea is represented as: {half_cup}.")

# Decimal
# A decimal is a way to represent real numbers using a decimal point. It is often used for financial calculations where precision is important.
# In Python, you can use the Decimal class from the decimal module to represent decimal numbers.
precise_temp = Decimal('85.5')
print(f"The precise temperature for brewing tea is: {precise_temp}.")