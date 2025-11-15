import math

r = 2.5
circumference = 2 * math.pi * r
rounded_up = math.ceil(circumference)
accurate_sum = math.fsum([0.00014324235]*5) 


print(circumference)
print(rounded_up)
print(accurate_sum)
