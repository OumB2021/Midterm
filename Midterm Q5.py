def question5answer(s):
  vowels = ['a', 'o', 'i', 'u', 'e']
  for i in range(0, len(vowels)):
    s = s.replace(vowels[i], '')
    s = s.replace(vowels[i].capitalize(), '')
  return s

s1 = "OIKOw CwiOImWE ooioIQuCdcMDsKmslD kOKPKp"
print(question5answer(s1))
