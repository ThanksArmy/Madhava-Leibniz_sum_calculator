# Define a function to calculate the sum of the Madhava-Leibniz series up to a given number of terms
def madhava_leibniz_series(num_terms):
    sum = 0
    for n in range(num_terms):
        term = ((-1) ** n) * (4 / (2 * n + 1))
        sum += term
    return sum

# Input: Number of terms
num_terms = int(input("Enter the number of terms: "))

# Calculate and print the result
result = madhava_leibniz_series(num_terms)
print(f"The sum of the first {num_terms} terms of the Madhava-Leibniz series is: {result}")
