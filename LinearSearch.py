#Importing Modules
import random
import matplotlib.pyplot as graph

#fillArray method fills array with random values and returns it
def fillArray(nums):
  arr = []
  while len(arr) < nums:
    randomNum = random.randint(1, nums)
    if randomNum in arr:
      continue
    else:
      arr.append(randomNum)
  return arr

#Linear Search function
def linear_searcher(var, aList, nums):
  i = 0 #This counts how many comparisons we do
  while i < nums and var != aList[i]: #This steps through and compares each value
    i+=1 #If they are not equal then our comparison number increments and return it
  return i

#Defines our 'n' array, 'N' array and an average array to store our averages.
N = []
average = []
n = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Here is the List of the Numbers Comparisons ('N') Followed By Averages of Each when:\n")
#This double for-loop loops through the range of each iteration and generates a new array and new 'x' value each time.
for index in n:
  for iter in range(100): #We go up to 100 iterations
   arr = fillArray(index) #Generate a random array each iteration
   x = random.randint(1, 2 + index) #Generates a random x value 1 to 2 + n
   N.append(linear_searcher(x, arr, index)) #We call linear_searcher here to find the value and append it to N

  #We print our N value and use the N values by sum(N) to calculate our average
  print("\nn = ", index, ":\n", N)
  avg = sum(N) / 100
  average.append(avg)

  #Print our average and clears our 'N' for the next iteration
  print("Avg = ", avg)
  N.clear()
  
#This is used to present and print our graph out neatly
print("\nThe Graph is Plotted in a seperate window!")
graph.title("Linear Search Alogorithm")
graph.xlabel("n")
graph.ylabel("Aₙ = Average of Comparisons")
graph.plot(n, average, label = "Our Calculated Line")
graph.plot(n, n, label = "O(n)")
graph.legend()
graph.show()