# Design a data structure that supports following behaviors

# Implement the NumberProcess class:

# NumberProcess() Initializes the object.

# addNum(number) Adds number to the data structure,

# dropLastAddingNum() remove last adding number if there is any number, otherwise return "no numbers inside"

# search(number) Returns true if there is any number in the data structure that matches number or false otherwise.

# maxNumber(number) Returns max number if there is any number in the data structure, otherwise return "no numbers inside"

# minNumber(number) Returns max number if there is any number in the data structure, otherwise return "no numbers inside"

# measureAverage() return the average result of all the number in your data structure, the data type should be float

class NumberProcess:

  def __init__(self):
    self.numbers = []
        
  def addNum(self, number):
    self.numbers.append(number) 

  def search(self, number):
    for i in range(0, len(self.numbers)):
      if (self.numbers[i] == number):
        return True
    
    return False
        
  def dropLastAddingNum(self):
    if (self.numbers == []):
      return "no numbers inside"
    else:
      self.numbers.pop(len(self.numbers) - 1)
        
  def maxNumber(self):
    max = self.numbers[0]
    for i in range(1, len(self.numbers)):
      if (max < self.numbers[i]):
        max = self.numbers[i]
    
    return max
           
  def minNumber(self):
    min = self.numbers[0]
    for i in range(1, len(self.numbers)):
      if (min > self.numbers[i]):
        min = self.numbers[i]
    
    return min
        
  def measureAverage(self):
    average = 0
    for i in range(0, len(self.numbers)):
      average = average + self.numbers[i]
    
    return float(average / len(self.numbers))
        
            
  
numberprocess = NumberProcess() #no exception /error
numberprocess.addNum(100000) #no exception /error
numberprocess.addNum(100001) #no exception /error
numberprocess.addNum(10001) #no exception /error
print('average is: ', numberprocess.measureAverage())
print(numberprocess.search(100000))
numberprocess.dropLastAddingNum() #no exception /error
print('average is: ', numberprocess.measureAverage())
print(numberprocess.maxNumber())
print(numberprocess.minNumber())
    
