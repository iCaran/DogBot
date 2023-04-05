import math

A = 210.66798510366596
B = 200.0
C = 316.02286728831905

cos_A = (B**2 + C**2 - A**2) / (2 * B * C)
cos_B = (A**2 + C**2 - B**2) / (2 * A * C)
cos_C = (A**2 + B**2 - C**2) / (2 * A * B)

A = math.degrees(math.acos(cos_A))
B = math.degrees(math.acos(cos_B))
C = math.degrees(math.acos(cos_C))

print("Angle A:", A)
print("Angle B:", B)
print("Angle C:", C)
