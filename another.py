# ##Weight converter 

# Weight = float(input("Weight = "))
# Conversion = (input("Choose k for Kilos and p for pounds: "))

# # if (Conversion  == "K" or Conversion == "k"):
# #     print("Your weight in pounds will be : ", Weight/0.45)
# # elif(Conversion == "P" or Conversion == "p"):
# #     print("Your weight in kgs will be : ", Weight*0.45)

# if Conversion.upper() == 'P':
#     converted = Weight * 0.45
#     print(f"You are {converted} kgs")
# else: 
#     converted = Weight /0.45
#     print(f"You are {converted} pounds")

#Guessing the game
# Guess the number = 0
# Guess the number = 2
# Guess the number = 3
# You failed to guess the number. 

# import random
# number = input("Guess the number : ")

# numberfromuser = random.randint(1,10)
# while(number == numberfromuser):
#     print(f"You've guessed the number. Yay!!, The number is {numberfromuser}")
#     break
# print("You've failed to guess the number")

#Another Tactic
# secret_number = 9
# guess_count = 0 
# guess_limit = 3
# while guess_count< guess_limit:
#     guess= int(input("Guess the number: "))
#     guess_count +=1
#     if guess == secret_number:
#         print("You won!!")
#         break
# else:
#     print("Sorry!! you failed.")


# prices = [10,20,30] 
# sum = 0
# for price in prices:
#     sum += price
# print(f"The total sum is {sum}")

# for x in range(4):
#     for y in range(3):
#         print(f"({x},{y})")

# number = [5,2,5,2,2]
# for num in number:
#     output= ''
#     for count in range(num):
#         output += "x"
#     print(output) \

my_list = [2,4,234,643,12,52,123,523]
max = my_list[0]
for number in my_list:
    if number > max:
        max = number
print(max)