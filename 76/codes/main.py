# Define the probabilities of hitting the target for A, B, and C
prob_A = 0.4
prob_B = 0.3
prob_C = 0.2

# Calculate the probabilities of missing the target for A, B, and C
prob_A_complement = 1 - prob_A
prob_B_complement = 1 - prob_B
prob_C_complement = 1 - prob_C

# Calculate the probability of two hits
probability_two_hits = (
    prob_A * prob_B * prob_C_complement +
    prob_A * prob_B_complement * prob_C +
    prob_A_complement * prob_B * prob_C
)

print("The probability of two hits is:", probability_two_hits)

