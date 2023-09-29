import random
from coordination_system import create_coordination_system

n = 10000
counter1, counter2 = 0, 0  # counters for both regions
area = 1  # total area of square unit

# dots for creation and display of slopes in two regions
x1_slope, y1_slope = [], []
x2_slope, y2_slope = [], []

for i in range(n):
    x1 = random.uniform(0, 1)
    y1 = random.uniform(0, 1)
    if x1**2 < y1 < x1:
        counter1 += 1
        x1_slope.append(x1)
        y1_slope.append(y1)

    x2 = random.uniform(-1, 0)
    y2 = random.uniform(0, 1)
    if x2**2 < y2 < -x2:
        counter2 += 1
        x2_slope.append(x2)
        y2_slope.append(y2)

area1 = area * counter1 / n
area2 = area * counter2 / n
areas_sum = area1 + area2
areas = [area1, area2, areas_sum]

slope = [(x1_slope, y1_slope, "Region 1"), (x2_slope, y2_slope, "Region 2")]
create_coordination_system((-2, 2), (-2, 2), title="Monte Carlo Simulation", slope=slope, areas=areas)