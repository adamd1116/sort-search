#Maybe a binary search I have no idea
#Took me 30 minutes to realise the algorithm was attempting to search through an unsorted list even though it was designed for a sorted list
import random

#variables for search and sort
found = False
l = [9, 5, 4, 15, 2, 2246, 53 ,87, 13, 59, 12 ,69, 1039 ,5929, 235, 6837, 29]
t  = random.choice(l)
le = 0 #index of left value
r = len(l)-1 #index of right value
m = round((le+r)/2) #index of middle value
ll = len(l)-1 #These two variables are for the sorting algorithm, so it can be used on different lengths of lists
ll2 = len(l)
search = False #for search

#bubble sort, compares 2 values, swaps them if needed then moves to the next value in the list
for j in range(0,ll2): #This extra for loop prevents the loop from executing after the list has been sorted. Saving memory and time
    check_for_swap = False
    for i in range(0,ll):
        if l[i] > l[i + 1]:
            swap = l[i]
            l[i] = l[i + 1]
            l[i + 1] = swap
            check_for_swap = True
    if check_for_swap == False:
        if i==ll-1:
            search=True #This means the searching algorithm only starts once the list is sorted
        break

print(f'\nSorted: ',l,'\n')

#binary search, starts from middle value, determines if target is < or > or ==, then halves values and continues till target is found
if search == True: #prevents the search from happening before the list is fully sorted
    while found == False:
        if t <= l[m]:
            if t < l[m]:
                print(f"\tTarget is less than middle")
                r = m #changing right value as it can't be any value right from middle
                m = (le+r)//2 #halving the middle value to search again
                if t < le:
                    le-=1 #incase of an error with the halving, this reduces left value to prevent the loop from looping over and over again
                else:
                    pass
            elif t == l[m]:
                print(f"\n\tTarget found: {t}\n")
                found = True
                break
        if t >= l[m]:
            if t > l[m]:
                print(f"\tTarget is larger than middle")
                le = m
                m = (le+r)//2 #same stuff as before
                if t > r:
                    r+=1
                else:
                    pass
            elif t == l[m]:
                print(f"\n\tTarget found: {t}\n")
                found = True
                break
