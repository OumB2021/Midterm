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
  #converts n to array of int 
  arr = [int(i) for i in str(n)]
  result = 0
  for i in range (0, len(arr)):
    result += arr[i] ** len(arr)
  
  if (n == result):
    return True
  else:
    return False

print(question3answer(152))