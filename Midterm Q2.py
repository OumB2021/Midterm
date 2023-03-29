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

# def question2answer(s):
#   if len(s) <= 2 :
#     return s[::-1] 

#   else :
#     newStr = "".join(s)
#     space = " "
#     reversedStr = newStr.split()[::-1]
#     new_arr = []
#     for i in range(len(reversedStr)):
#       if (reversedStr[i].isdigit()):
#         new_arr.append(reversedStr[i])
#       else:
#         for j in range(len(reversedStr[i])):
#           word = reversedStr[i]
#           new_arr.append(word[j])
#       if i < len(reversedStr) - 1:
#         new_arr.append(space)

#   return new_arr

def question2answer(s):
  stack = []
  result = []
  final = []
  newStr = "".join(s)
  result = newStr.split()

  if len(s) <= 2 :
    return s[::-1] 
    
  for i in range(len(result)):
    stack.append(result[i])
  
  for i in range(len(result)):
    word = stack.pop()
    if (word.isdigit()):
      final.append(word)
    else:
      for j in range(len(word)):
        final.append(word[j])
    final.append(" ")

  final.pop()
  return final

s= ["t"," "]

print(question2answer(s))

