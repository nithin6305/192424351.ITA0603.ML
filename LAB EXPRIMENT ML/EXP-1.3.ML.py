# FIND-S Algorithm using Student Placement Dataset

# Training dataset
data = [
    ["High", "Good", "Yes", "Good", "High", "Yes"],
    ["High", "Excellent", "Yes", "Good", "High", "Yes"],
    ["Medium", "Average", "No", "Average", "Medium", "No"],
    ["High", "Good", "Yes", "Excellent", "High", "Yes"],
    ["Low", "Poor", "No", "Average", "Low", "No"],
    ["High", "Good", "Yes", "Good", "Medium", "Yes"]
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
