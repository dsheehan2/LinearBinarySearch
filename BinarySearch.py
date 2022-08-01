#Importing Modules
import math
import random
import matplotlib.pyplot as graph

#fillandSort method fills array with random values and sorts them
def fillandSort(nums):
  #Declares a new array
  arr = []
  #Loops through array
  while len(arr) < nums:
    #Checks for duplicate values and doesn't add the value if it is duplicated
    randomNum = random.randint(1, nums)
    if randomNum in arr:
      continue
    else:
      arr.append(randomNum)
  #Sorts the final array and then returns it
  arr.sort()
  return arr

#Binary Search function
def binary_searcher(var, aList, nums):
  #Normal values initialized to check at the beginning and end
  count = 0
  beg = 0
  end = nums - 1

  #Checks to make sure that the element to be found is not at the beginning and returns it
  if var == aList[beg]:
    count+=1
    return count

  #Steps through the array of values and ends when its found or if it can't find value.
  while (beg <= end):
    #mid finds the middle of the list through each iteration
    mid = math.floor((beg + end) / 2)
    #if it is less than the mid value it resets the end backward by 1 index value
    if var < aList[mid]:
      count+=1
      end = mid - 1
    #if not then we check to see if it is greater than mid, if it is, we cut the first part of the list out
    elif var > aList[mid]:
      count+=1
      beg = mid + 1
    #else it has to be the middle value so it will break and return it
    else:
      count+=1
      break
  return count

#Defines our 'n' array, 'N' array and an average array to store our averages.
n = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
N = []
average = []
print("Here is the List of the Numbers Comparisons ('N') Followed By Averages of Each when:\n")
#This double for-loop loops through the range of each iteration and generates a new array and new 'x' value each time.
for index in n:
  for iter in range(100): #We go up to 100 iterations
   arr = fillandSort(index) #Generate a random array each iteration
   x = random.randint(1, 2 + index) #Generates a random x value 1 to 2 + n
   N.append(binary_searcher(x, arr, index)) #We call binary_searcher here to find the value and append it to N

  #We print our N value and use the N values by sum(N) to calculate our average
  print("\nn = ", index, ":\n", N) 
  avg = sum(N) / 100
  average.append(avg)

  #Print our average and clears our 'N' for the next iteration
  print("Avg = ", avg) 
  N.clear()

#Defines our 'y' value which holds the log2n of the 'n' values using the math module
y = []
for i in n:
  y.append(math.log2(i))

#This is used to present and print our graph out neatly
print("\nThe Graph is Plotted in a seperate window!")
graph.title("Binary Search Alogorithm")
graph.xlabel("n")
graph.ylabel("Aₙ = Average of Comparisons")
graph.plot(n, average, label = "Our Calculated Line")
graph.plot(n, y, label = "O(log₂n)")
graph.legend()
graph.show()