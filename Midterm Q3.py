# Question3
# Given an integer n, return true if and only if it is an Armstrong number.
# The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.

# sample 1
# Input: n = 153
# Output: true
# Explanation: 153 is a 3-digit number, and 153 = 13 + 53 + 33.
# sample 2
# Input: n = 123
# Output: false
# Explanation: 123 is a 3-digit number, and 123 != 13 + 23 + 33 = 36.
# sample 3
# Input: n = 9
# Output: True
# Explanation: 9 is a 1-digit number, and 9 ==  91  = 9.

def question3answer(n):
  # Convert the input to an array of digits
  digits = [int(d) for d in str(n)]

  # Calculate the sum of each digit raised to the power of the number of digits
  digit_sum = 0
  for digit in digits:
      digit_sum += digit ** len(digits)

  # Check if the input is equal to the digit sum
  return n == digit_sum

print(question3answer(153))