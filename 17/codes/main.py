import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 6  # Number of trials (6 balls drawn)
p_x = 10 / 25  # Probability of drawing X-marked ball
p_y = 15 / 25
# Values for the x-axis (number of X-marked balls)
x_values = np.arange(0, n + 1)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_x)

# Calculate the probability that all drawn balls will bear the X mark
probability_all_X = binomial_pmf[n]

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_x
sigma = np.sqrt(n * p_x * (1 - p_x))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, n, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Stem plot for the PMF of the binomial distribution
ax.stem(x_values, binomial_pmf, basefmt=' ', linefmt='b-', markerfmt='bo', label='Binomial PMF')

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of X-marked balls (All X)')
ax.set_ylabel('Probability')
ax.set_title('Stem Plot of Binomial PMF vs. PDF of Gaussian (All X-marked balls)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()

# Print the probability that all drawn balls will bear the X mark
print(f"Probability that all balls drawn will bear the X mark: {probability_all_X:.4f}")


# Values for the x-axis (number of Y-marked balls, not more than 2)
x_values = np.arange(0, 3)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_y)

# Calculate the probability that not more than 2 balls will bear the Y mark
probability_not_more_than_2_Y = np.sum(binomial_pmf)

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_y
sigma = np.sqrt(n * p_y * (1 - p_y))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, 2, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Stem plot for the PMF of the binomial distribution
ax.stem(x_values, binomial_pmf, basefmt=' ', linefmt='b-', markerfmt='bo', label='Binomial PMF')

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of Y-marked balls (Not more than 2)')
ax.set_ylabel('Probability')
ax.set_title('Stem Plot of Binomial PMF vs. PDF of Gaussian (Not more than 2 Y-marked balls)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()

# Print the probability that not more than 2 balls will bear the Y mark
print(f"Probability that not more than 2 balls will bear the Y mark: {probability_not_more_than_2_Y:.4f}")


# Values for the x-axis (number of Y-marked balls, at least one)
x_values = np.arange(1, n + 1)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_y)

# Calculate the probability that at least one ball will bear the Y mark
probability_at_least_one_Y = 1 - binomial_pmf[0]  # 1 minus the probability of 0 Y-marked balls

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_y
sigma = np.sqrt(n * p_y * (1 - p_y))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, n, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Stem plot for the PMF of the binomial distribution
ax.stem(x_values, binomial_pmf, basefmt=' ', linefmt='b-', markerfmt='bo', label='Binomial PMF')

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of Y-marked balls (At least one)')
ax.set_ylabel('Probability')
ax.set_title('Stem Plot of Binomial PMF vs. PDF of Gaussian (At least one Y-marked ball)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()

# Print the probability that at least one ball will bear the Y mark
print(f"Probability that at least one ball will bear the Y mark: {probability_at_least_one_Y:.4f}")


# Values for the x-axis (number of X-marked balls)
x_values = np.arange(0, n + 1)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_x)

# Calculate the probability that the number of X-marked balls equals the number of Y-marked balls
probability_equal_X_and_Y = binomial_pmf[int(n / 2)]  # Probability at the midpoint

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_x
sigma = np.sqrt(n * p_x * (1 - p_x))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, n, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Stem plot for the PMF of the binomial distribution
ax.stem(x_values, binomial_pmf, basefmt=' ', linefmt='b-', markerfmt='bo', label='Binomial PMF')

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of X-marked balls (Equal X and Y)')
ax.set_ylabel('Probability')
ax.set_title('Stem Plot of Binomial PMF vs. PDF of Gaussian (Equal X and Y)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()

print(f"Probability that the number of X-marked balls equals the number of Y-marked balls: {probability_equal_X_and_Y:.4f}")

