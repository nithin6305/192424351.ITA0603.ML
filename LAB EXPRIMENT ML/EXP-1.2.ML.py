# FIND-S Algorithm using Loan Approval Dataset

# Training dataset
data = [
    ["High", "Good", "Permanent", "Yes", "Young", "Yes"],
    ["High", "Good", "Permanent", "No", "Middle", "Yes"],
    ["Low", "Poor", "Temporary", "No", "Young", "No"],
    ["Medium", "Good", "Permanent", "Yes", "Middle", "Yes"],
    ["High", "Average", "Temporary", "Yes", "Old", "No"],
    ["High", "Good", "Permanent", "Yes", "Middle", "Yes"]
]

# Initialize hypothesis with the most specific values
hypothesis = None

print("Training Examples:\n")
for row in data:
    print(row)

# Apply FIND-S Algorithm
for row in data:
    attributes = row[:-1]
    target = row[-1]

    # Consider only positive examples
    if target == "Yes":
        if hypothesis is None:
            hypothesis = attributes.copy()
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"

# Display final hypothesis
print("\nFinal Hypothesis:")
print(hypothesis)
