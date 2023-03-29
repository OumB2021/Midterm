# Question 5
# Given a string s, remove the vowels 'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U' from it, and return the new string.

# Example 1:
# Input: s = "LeetcOdeIsACommunityforCODerS"
# Output: "LtcdsCmmntyfrCDrS"
# Example 2:
# Input: s = "aeiou"
# Output: ""

def question5answer(s):
  vowels = ['a', 'o', 'i', 'u', 'e']
  for i in range(0, len(vowels)):
    s = s.replace(vowels[i], '')
    s = s.replace(vowels[i].capitalize(), '')
  return s

s1 = "OIKOw CwiOImWE ooioIQuCdcMDsKmslD kOKPKp"
print(question5answer(s1))
