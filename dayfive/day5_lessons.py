'''
for loop and while loop

'''

names =["gaya", "saya","liya","raya","jaya","piya","kaya"]

'''for name in names:
    print(name)
for i in range(0, len(names),3):
    print(names[i])'''
#heights =[5.10,5.25,5.15,5.30,5.5,5.65,5.70,5.8]
'''heights = input("Enter student heights: \n")
heights = heights.split(",")
sum =0
count =0
for height in heights:
    sum+= float(height)
    count+=1
avg =sum/count
print("The average height is: ",round(avg,2))'''

#calculate high score

student_score = [78,65,89,55,91,64,89,96,50,99,34]
max_score = student_score[0]
min_score =student_score[0]
'''for score in student_score:

    if(score>max_score):
        max_score =score
    if(score<min_score):
        min_score =score
for i in range(0,len(student_score)):
    if (student_score[i] > max_score):
        max_score = student_score[i]
    if (student_score[i] < min_score):
        min_score = student_score[i]
print("The highest score is: ",max_score)
print("The smallest score is: ",min_score)
even_list =[]
sum =0
for i in range(1,101):
    if(i%2==0):
        sum+=i
        even_list.append(i)
print(even_list)
print("Sum of the even numbers is: ",sum)
'''
# FizzBuzz game
# print out integers from 1 to 100
# if the # is divisible by 3 then print "Fizz" instead of that #
# if the # is divisible by 5 then print "Buzz" instead of that #
# if the # is divisible by 3 and 5 then print "FizzBuzz" instead of that #

for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz",end =" ")
    elif(i%3==0):
        print("Fizz",end =" "),
    elif(i%5==0):
        print("Buzz",end =" "),

    else:
        print(i,end =" "),