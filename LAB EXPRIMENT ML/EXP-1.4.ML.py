# FIND-S Algorithm using Disease Diagnosis Dataset

# Training dataset
data = [
    ["Yes", "Yes", "Yes", "Yes", "Yes", "Positive"],
    ["Yes", "Yes", "No", "Yes", "Yes", "Positive"],
    ["No", "Yes", "Yes", "No", "No", "Negative"],
    ["Yes", "Yes", "Yes", "No", "Yes", "Positive"],
    ["No", "No", "Yes", "Yes", "No", "Negative"],
    ["Yes", "Yes", "No", "No", "Yes", "Positive"]
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
    if target == "Positive":
        if hypothesis is None:
            hypothesis = attributes.copy()
        else:
            for i in range(len(hypothesis)):
                if hypothesis[i] != attributes[i]:
                    hypothesis[i] = "?"

# Display final hypothesis
print("\nFinal Hypothesis:")
print(hypothesis)
