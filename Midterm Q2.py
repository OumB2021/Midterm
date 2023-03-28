# Given a character array s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
# sample 1
# Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]. 
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"].
# sample 2
# Input: s = ["a"]
# Output: ["a"]
# Constraints:
# 1 <= s.length <= 105
# s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
# There is at least one word in s.
# s does not contain leading or trailing spaces.
# All the words in s are guaranteed to be separated by a single space.

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
space = ' '
reversedOrder = (space.join(s[::-1]))
print(reversedOrder.split())