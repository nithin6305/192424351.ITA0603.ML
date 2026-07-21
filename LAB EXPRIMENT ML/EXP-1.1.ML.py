# FIND-S Algorithm using Play Tennis Dataset

# Training dataset
data = [
    ["Sunny", "Warm", "Normal", "Strong", "Warm", "Same", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Warm", "Same", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "Warm", "Change", "No"],
    ["Sunny", "Warm", "High", "Strong", "Cool", "Same", "Yes"],
    ["Rainy", "Warm", "Normal", "Weak", "Warm", "Same", "No"],
    ["Sunny", "Warm", "Normal", "Weak", "Warm", "Same", "Yes"]
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
