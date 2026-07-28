import pandas as pd

# Read dataset
data = pd.read_csv("email spam.csv")

# Convert dataframe to list
dataset = data.values.tolist()

# Initialize Specific and General hypotheses
S = dataset[0][:-1]
G = ['?'] * len(S)

print("Initial S =", S)
print("Initial G =", G)
print()

# Candidate Elimination
for x in dataset:
    if x[-1] == "Yes":
        # Generalize S
        for i in range(len(S)):
            if S[i] != x[i]:
                S[i] = "?"
    else:
        # Specialize G
        for i in range(len(S)):
            if S[i] != x[i]:
                G[i] = S[i]

    print("S =", S, "G =", G)

print("\nFinal Specific Hypothesis (S):", S)
print("Final General Hypothesis (G):", G)