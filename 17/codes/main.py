import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the problem
total_balls = 25
balls_X = 10
balls_Y = 15
draws = 6

# Probability of drawing X or Y
p_X = balls_X / total_balls
p_Y = balls_Y / total_balls

# Calculate the probabilities for each scenario
# 1. All will bear X mark
prob_all_X = p_X ** draws

# 2. Not more than 2 will bear Y mark
prob_not_more_than_2_Y = sum([norm.pdf(i, loc=draws * p_Y, scale=np.sqrt(draws * p_Y * (1 - p_Y))) for i in range(3)])

# 3. At least one ball will bear Y mark
prob_at_least_one_Y = 1 - (p_X ** draws)

# 4. The number of balls with X mark and Y mark will be equal
mean_XY_equal = draws * (p_X + p_Y) / 2
std_dev_XY_equal = np.sqrt(draws * p_X * p_Y)
prob_XY_equal = norm.cdf(mean_XY_equal, loc=draws * (p_X + p_Y) / 2, scale=std_dev_XY_equal)

# Create a CDF chart for the Standard Normal Distribution
x = np.linspace(-3, 3, 1000)
cdf = norm.cdf(x, loc=0, scale=1)

plt.figure(figsize=(10, 6))
plt.plot(x, cdf, label='CDF of Standard Normal Distribution')
plt.xlabel('Z (Standard Score)')
plt.ylabel('Cumulative Probability')
plt.title('CDF of the Standard Normal Distribution')
plt.axvline(0, color='red', linestyle='--', label='Mean (0)')
plt.grid(True)
plt.legend()
plt.show()

# Print the probabilities for the given scenarios
print("1. Probability that all will bear X mark:", prob_all_X)
print("2. Probability that not more than 2 will bear Y mark:", prob_not_more_than_2_Y)
print("3. Probability that at least one ball will bear Y mark:", prob_at_least_one_Y)
print("4. Probability that the number of balls with X mark and Y mark will be equal:", prob_XY_equal)

