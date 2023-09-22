import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 6  # Number of trials
p = 0.4  # Probability of success in a single trial

# Parameters for the corresponding normal distribution
mu = n * p
sigma = np.sqrt(n * p * (1 - p))

# Values for x-axis (number of successes)
x = np.arange(0, n+1)

# Calculate binomial PMF
binom_pmf = binom.pmf(x, n, p)

# Calculate normal PDF
x_norm = np.linspace(0, n, 100)
norm_pdf = norm.pdf(x_norm, loc=mu, scale=sigma)

# Plot both distributions
plt.bar(x, binom_pmf, label='Binomial PMF', alpha=0.5)
plt.plot(x_norm, norm_pdf, label='Normal PDF', color='red')

plt.xlabel('Number of Successes')
plt.ylabel('Probability / Density')
plt.legend()
plt.title('Binomial PMF and Normal PDF')
plt.grid(True)

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 6  # Number of trials (6 balls drawn)
p_y = 15 / 25  # Probability of drawing Y-marked ball

# Values for the x-axis (number of Y-marked balls, not more than 2)
x_values = np.arange(0, 3)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_y)

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_y
sigma = np.sqrt(n * p_y * (1 - p_y))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, 2, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the PMF of the binomial distribution
ax.bar(x_values - 0.2, binomial_pmf, width=0.4, label='Binomial PMF', alpha=0.5)

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of Y-marked balls (Not more than 2)')
ax.set_ylabel('Probability')
ax.set_title('PMF of Binomial vs. PDF of Gaussian (Not more than 2 Y-marked balls)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 6  # Number of trials (6 balls drawn)
p_y = 15 / 25  # Probability of drawing Y-marked ball

# Values for the x-axis (number of Y-marked balls, at least one)
x_values = np.arange(1, n + 1)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_y)

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_y
sigma = np.sqrt(n * p_y * (1 - p_y))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, n, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the PMF of the binomial distribution
ax.bar(x_values - 0.2, binomial_pmf, width=0.4, label='Binomial PMF', alpha=0.5)

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of Y-marked balls (At least one)')
ax.set_ylabel('Probability')
ax.set_title('PMF of Binomial vs. PDF of Gaussian (At least one Y-marked ball)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, norm

# Parameters for the binomial distribution
n = 6  # Number of trials (6 balls drawn)
p_x = 10 / 25  # Probability of drawing X-marked ball
p_y = 15 / 25  # Probability of drawing Y-marked ball

# Values for the x-axis (number of X-marked balls)
x_values = np.arange(0, n + 1)

# Calculate the PMF of the binomial distribution for each x
binomial_pmf = binom.pmf(x_values, n, p_x)

# Parameters for the Gaussian distribution (normal approximation)
mu = n * p_x
sigma = np.sqrt(n * p_x * (1 - p_x))

# Values for the x-axis for the Gaussian distribution
x_gaussian = np.linspace(0, n, 1000)
pdf_gaussian = norm.pdf(x_gaussian, loc=mu, scale=sigma)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 5))

# Plot the PMF of the binomial distribution
ax.bar(x_values - 0.2, binomial_pmf, width=0.4, label='Binomial PMF', alpha=0.5)

# Plot the PDF of the Gaussian distribution (normal approximation)
ax.plot(x_gaussian, pdf_gaussian, label='Gaussian PDF', color='red')

# Set labels and title
ax.set_xlabel('Number of X-marked balls (Equal X and Y)')
ax.set_ylabel('Probability')
ax.set_title('PMF of Binomial vs. PDF of Gaussian (Equal X and Y)')

# Add a legend
ax.legend()

# Show the plot
plt.grid(True)
plt.show()



