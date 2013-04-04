#Initialize number as 3 because it is the first natural number divisible by 3 or 5
num=3
#Initialize sum to 0
Sum=0

#Run loop while num is less than 1000, add 1 to num each run through the loop
while(num<1000):
    #Add num to Sum if num is evenly divisible by 3 or 5
    if(num%3==0 or num%5==0):
        Sum=Sum+num
    num=num+1

#Print Sum
print Sum
