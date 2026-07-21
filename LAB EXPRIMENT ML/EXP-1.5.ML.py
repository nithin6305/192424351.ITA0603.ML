# FIND-S Algorithm using Email Spam Detection Dataset

# Training dataset
data = [
    ["Yes", "Yes", "Yes", "No", "Yes", "Yes"],
    ["Yes", "Yes", "Yes", "Yes", "Yes", "Yes"],
    ["No", "No", "No", "No", "No", "No"],
    ["Yes", "No", "Yes", "No", "Yes", "Yes"],
    ["No", "Yes", "No", "Yes", "No", "No"],
    ["Yes", "Yes", "Yes", "No", "No", "Yes"]
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
