# print("Hello, World!")
# name = input("What is your name?")
# print("Hello {}!\nWelcome to the snake pit".format(name))

from dis import disco
from distutils.command.build_scripts import first_line_re


def main():
  i = 1
  max = 10
  while (i <= max):
    print(i)
    i = i + 1

# main()

def quickMathWithDocString():
  """ this function does quick math """
  num1 = input("First number to be added:")
  num1 = int(num1)
  num2 = input("Second number to be added:")
  num2 = int(num2)
  result = num1 + num2
  print(f"These numbers add up to {result}")

# print(quickMathWithDocString.__doc__)
# quickMathWithDocString()

def fizzbuzz():
  i = 1
  max = 100
  while (i <= max):
    if i % 15 == 0:
      print('fizzbuzz')
    elif i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')
    else:
      print(i)
    i = i + 1



alphabetToJ = 'abcdefghij'
alphaNumeraMinusFirstFour = '123456789' + alphabetToJ[4:]
# print(alphaNumeraMinusFirstFour)



def rangeSelectForLoop():
  selectedRange = input('How many numbers junior?')
  for i in range(int(selectedRange)):
    print(f'Now the index is {i + 1}')



def forLoopWithStepValue():
  for i in range(1,27, 5):
    print(i)



# sum = 0
# for num in range(101):
#   sum += num
#   print(sum)

# n = 100
# sum = n * (n+1)/2
# print(sum)


# for x in range(10):
#   for y in range(10):
#     for z in range(10):
#       print(f'({x}),({y}),({z})')
#       if z == 10:
#         break


#sum of numbers from 1-100 with for loop
def sumLoop(cap):
  start = time.monotonic()
  sum = 0
  for i in range(0, cap):
    sum = sum + i
  print(sum)
  end = time.monotonic()
  print('Time elapsed', end - start)


#sum of numbers from 1-100 using recursion
def sumRecursion(n):
  if n > 0:
    return n + sumRecursion(n-1)
  return 0

# result = sumRecursion(100)
# print(result)


import time
#sum of numbers from 1-100 with sum of natural numbers equation
def sumOfNaturalNumbers(n):
  start = time.monotonic()
  sum = n * (n + 1) / 2
  print(sum)
  end = time.monotonic()
  print('Time elapsed', end - start)


def sum(num1, num2):
  start = time.monotonic()
  total = num1 + num2
  print(total)
  end = time.monotonic()
  print(end - start)

# sum(1_000_000,1_000_000_000_000_000)


# sumLoop(1_000_000_000)
# sumRecursion(1_000_000)
# sumOfNaturalNumbers(1_000_000_000)

# value = sumOfNaturalNumbers.monotonic()
# print(value)




companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

def sort_key(company):
  return company[2]

companies.sort(key=sort_key, reverse=True)

companies.sort(key=lambda company: company[2], reverse=True)

# print(companies)



# appliances = ['washer', 'dryer', 'refrigerator', 'lamp']

# applianceIter = iter(appliances)
# print(applianceIter)

# appSingle = next(applianceIter)
# print(appSingle)

# appSingle = next(applianceIter)
# print(appSingle)

# appSingle = next(applianceIter)
# print(appSingle)

# appSingle = next(applianceIter)
# print(appSingle)

# print(appliances)


person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 34,
  'favorite_colors': ['green', 'blue'],
  'active': False
}

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

modStocks = {a: b * 1.02 for (a, b) in stocks.items()}

# mod_stocks = {}
# for symbol, price in stocks.items():
#   mod_stocks[symbol] = price*1.02

#for i in modStocks:
#   print(f'{i}, {modStocks[i]}')


from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import nltk
# nltk.download('vader_lexicon')

# user_input = input("Please Rate Our Services >>: ")
# sid = SentimentIntensityAnalyzer()
# score = sid.polarity_scores(user_input)
# print(score)

user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
if score["neg"] != 0:
      print("Negative")
else:
        print("Positive")


# import math
# pi = math.pi

# def leibniz(n):
#     t_sum = 0
#     for i in range(n):
#         term = (-1) ** i / (2*i+1)
#         t_sum = t_sum + term

#     return [t_sum * 4, n]


#terms = int(input("Enter number of terms: "))

#pi = leibniz(terms)

#print('Pi = ', pi)



#epsilon = float(input('Enter precision of choice: '))

#def iter_pi(eps):
#    numOfIterations = 0
#    piWithinTen = 0
    
#    while piWithinTen < pi - eps:
#        pyWithinTen = piWithinTen + eps
    
#   print(piWithinTen)



#result = iter_pi(epsilon)

#print(result)


























