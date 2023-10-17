# # # # # # # # # # print ("Lakshit")
# # # # # # # # # # print("o-------")
# # # # # # # # # # print("||||||||||")

# # # # # # # # # # price =  10
# # # # # # # # # # price = 20
# # # # # # # # # # rating = 4.9
# # # # # # # # # # name = "mosh"
# # # # # # # # # # os_published = False
# # # # # # # # # # print(price)


# # # # # # # # # # name= input("Enter the name:")
# # # # # # # # # # age = input("Your Age:")
# # # # # # # # # # os = input ("Are you a existing customer?")

# # # # # # # # # # if(os == True):
# # # # # # # # # #     print("You're a existing customer")
# # # # # # # # # # else:
# # # # # # # # # #     print("You're a new customer,welcome to the club")

# # # # # # # # # # print(f"I'm happy to say that, {name}" + f"is a new guest in our house and he is aged {age}")

# # # # # # # # # # ## Ask two questions: person's name and favorite color. Then, print a message like "Mosh like blue"

# # # # # # # # # # print(f"My name is {name}")
# # # # # # # # # # color = input("Tell your favorite color: ")

# # # # # # # # # # print(f"My name is {name}" + f"My favorite color is {color}")

# # # # # # # # # # ###-----------------------
# # # # # # # # # # birth_year = input('Birth Year')
# # # # # # # # # # print(type(birth_year))
# # # # # # # # # # age = 2023 - int(birth_year)
# # # # # # # # # # print(type(birth_year))
# # # # # # # # # # print(age)

# # # # # # # # # # ## Ask a user their weight in pounds, convert it to kilograms and print on the terminal

# # # # # # # # # # weight_inpounds= input("Tell me your weight in pounds: ")
# # # # # # # # # # weight_inkgs = int(weight_inpounds) * 0.454

# # # # # # # # # # print(weight_inkgs)

# # # # # # # # # course = '''Python is fun'''
# # # # # # # # # print(course [1:9])
# # # # # # # # # print(course [:8])
# # # # # # # # # # print(course [-2])
# # # # # # # # # # print(course [1:-1])

# # # # # # # # # ##Methods in python

# # # # # # # # # course = "Python is super fun"
# # # # # # # # # print(len(course))
# # # # # # # # # print(course.upper())
# # # # # # # # # print(course.lower())
# # # # # # # # # print(course.find('for'))
# # # # # # # # # # print(course.find('fun')) ##this gives the index 
# # # # # # # # # # print("Python" in course) ##this gives the boolean value
# # # # # # # # # # print(course.replace("super", "simple and"))

# # # # # # # # print ("Trying here")
# # # # # # # # print(10 // 3)
# # # # # # # # print(10 / 3)
# # # # # # # # x = 10
# # # # # # # # x+= 3
# # # # # # # # print(x)
# # # # # # # # print ("Trying here")

# # # # # # # # print(abs(-2.9))
# # # # # # # # x = 2.9
# # # # # # # # print(round(x))

# # # # # # # # import math

# # # # # # # # print(math.floor(2.9))
# # # # # # # # print(math.ceil(2.9))

# # # # # # # # credit = int(input("What percentage credit you've: "))
# # # # # # # # if(credit >= 50000):
# # # # # # # #     cre_num = 1000000* 0.1
# # # # # # # #     print(f"You need to put down 10% that will be {cre_num}")
# # # # # # # # else:
# # # # # # # #     cre_num = 1000000*0.2
# # # # # # # #     print(f"You need to put down 20% that will be {cre_num}")


# # # # # # # has_high_income = True
# # # # # # # has_good_credit = True
# # # # # # # has_criminal_credit = False

# # # # # # # if has_high_income and has_good_credit and not has_criminal_credit:
# # # # # # #     print("Eligible for loan")

# # # # # # # ## AND : both condiftion
# # # # # # # # OR : atleast one
# # # # # # # # NOT : noone 

# # # # # # # # Excercise
# # # # # # # # if name is less than 3 characters long
# # # # # # # #     name must be at least 3 characters otherwise 
# # # # # # # # if it's more than 50 characters long
# # # # # # # #     name can be a maximum of 50 characters
# # # # # # # # otherwise
# # # # # # # #     name looks good 

# # # # # # type_your_name = input("type_your_name: ")
# # # # # # if (len(type_your_name ) < 3 ):
# # # # # #     print("the name should be at 3 characters")
# # # # # # elif(len(type_your_name) > 50): 
# # # # # #     print("name can be maximum of 50 characters")
# # # # # # else:
# # # # # #     print("name looks good!")


# # # # # weight = int(input("weights: "))
# # # # # unit = input("(L)bs or (K)gs: " )

# # # # # if unit.upper() == "L":
# # # # #     converted = weight * 0.45
# # # # #     print(f"you are {converted} kilos")
# # # # # else:
# # # # #     converted = weight / 0.45
# # # # #     print(f"you are {converted} pounds")

# # # # # i = 5
# # # # # while i >=1:
# # # # #     print("*" * i)
# # # # #     i=i-1
# # # # # print("Done")

# # # # n = 5
# # # # i = 0
# # # # while i<n:
# # # #     star = "x" * (n - i)
# # # #     spaces = " " * (i)
# # # #     print(spaces+star)
# # # #     i +=1
# # # # i = 0
# # # # while i <=5:
# # # #     star = "x" * (i)
# # # #     print(star)
# # # #     i+=1
# # # # print("done")

# # # secret_number = 9
# # # i = 0 
# # # while i < 3:
# # #     x = int(input("Enter  the number: "))
# # #     i= i+1
# # #     if x == secret_number:
# # #         print("You guessed it !!")
# # #         break
# # # else:
# # #     print("Try next time!!")

# # # Car-Game ----------------------------
# # command = ""
# # car_status = False
# # while True:
# #     command = input("> ").lower()
# #     if command == "start":
# #         if car_status:
# #             print("The Car has already started!!")
# #         else:
# #             car_status = True
# #             print("Car started....")
# #     elif command == "stop":
# #         if not car_status:
# #             print("The Car has already stopped!!")
# #         else:
# #             car_status = False
# #             print("Car stopped....")
# #     elif command == "help":
# #         print("""
# # start - to start the car
# # stop - to stop the car
# # quit - to quit the game""")
# #     elif command == "quit":
# #         break
# #     else:
# #         print("Sorry, I don't understand the command!!")
# # #---------------------------
# # for item in "Python":
# # #     print(item)

# # for item in ['mosh','thor','diby','barakka']:
# #     print(item[5:12])

# # for item in range(212, 400, 5):
# #     print(item)

# prices = [10,20,30]
# total = 0
# for price in prices:
#     total += price
# print(f"total is equals to: {total}")


# # #print 
# # xxxxx
# # xx
# # xxxxx
# # xx
# # xx