# Given probabilities
P_A_union_B = 0.6  # Probability that at least one of A and B occurs
P_A_intersection_B = 0.2  # Probability that both A and B occur simultaneously

# Calculate P(A) and P(B) using the inclusion-exclusion principle
P_A = P_A_union_B - P_A_intersection_B
P_B = P_A_union_B - P_A_intersection_B

# Calculate P(A) + P(B)
P_A_plus_P_B = P_A_union_B + P_A_intersection_B
# Calculate P(complement A) + P(complement B)
P_complement_A_plus_P_complement_B = 2 - P_A_plus_P_B
# Check if the result matches any of the provided options
if P_complement_A_plus_P_complement_B == 0.4:
    print("The answer is (A) 0.4")
elif P_complement_A_plus_P_complement_B == 0.8:
    print("The answer is (B) 0.8")
elif P_complement_A_plus_P_complement_B == 1.2:
    print("The answer is (C) 1.2")
elif P_complement_A_plus_P_complement_B == 1.6:
    print("The answer is (D) 1.6")
else:
    print("The result does not match any of the provided options.")

