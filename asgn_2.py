#Task 1
user=int(input("Enter a number:"))

if user % 2 == 0:
    print(f"{user} is an even number.")

else:
    print(f"{user} is an odd number.")

#Task 2
#sum of 1 to 50
sum=0
for i in range(1,51):
    sum = i + sum

print(f"The sum of numbers from 1 to 50 is: {sum}")