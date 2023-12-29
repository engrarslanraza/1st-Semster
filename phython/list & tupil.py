"""import numpy as np
import matplotlib.pyplot as plt
# Create current array "I"
I = np.array([1, 3, 5, 7])
# Define load resistance
R = 5
# Calculate voltage array "V"
V = R * I
# Find maximum, minimum, and average values for "I" and "V" arrays
I_max = np.max(I)
I_min = np.min(I)
I_avg = np.mean(I)
V_max = np.max(V)
V_min = np.min(V)
V_avg = np.mean(V)
# Print the results
print("Current array I:", I)
print("Voltage array V:", V)
print("Maximum current:", I_max)
print("Minimum current:", I_min)
print("Average current:", I_avg)
print("Maximum voltage:", V_max)
print("Minimum voltage:", V_min)
print("Average voltage:", V_avg)
# Plot the line graph of voltage vs current
plt.plot(I, V)
plt.title("Voltage vs Current")
plt.xlabel("Current (A)")
plt.ylabel("Voltage (V)")
plt.show()
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
p = Point(2, 3)
c = Circle(5, 6, 4)
print("Point p is at ({}, {})".format(p.x, p.y))
print("Circle c has center at ({}, {}) and radius {}".format(c.x, c.y, c.radius))
print("Area of circle c is:", c.area())


