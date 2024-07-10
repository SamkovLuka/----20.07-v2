import math



#1

#зроблене

# try:
#     num = int(input("Enter number: "))
#     print(math.factorial(num))
# except ValueError:
#     print("Negative number")


#2

#зроблене


#2.1
# num = int(input("Enter number: "))
# if num < 0:
#     print("Negative number")
# def Factorial(num):
#     print(math.factorial(num))


# print(Factorial(num))


#2.2
# num = int(input("Enter number: "))
# def Factorial(num):
#     try:
#       print(math.factorial(num))
#     except ValueError:
#         print("Negative number")


# print(Factorial(num))


#3


#зроблено


# try:
#     num_1 = int(input("Enter number: "))
#     num_2 = int(input("Enter number: "))
#     num_3 = int(input("Enter number: "))
#     num_4 = int(input("Enter number: "))
#     num_5 = int(input("Enter number: "))
#     list = [num_1,num_2,num_3,num_4,num_5]
#     print("1 - show list, 2 - show maximum value, 3 - show minimum value, 4 - show value of element by index, 5 - show element by index ")
#     ch = int(input("Enter your choice: "))

#     if ch == 1:
#         print(list)
#     elif ch == 2:
#         print(max(list))
#     elif ch == 3:
#         print(min(list))
#     elif ch == 4:
#         fnm = int(input("Enter index: "))
#         if fnm == 0:
#             print(num_1)
#         elif fnm == 1:
#             print(num_2)
#         elif fnm == 2:
#             print(num_3)
#         elif fnm == 3:
#             print(num_4)
#         elif fnm == 4:
#             print(num_5)
#     elif ch == 5:
#         zf = int(input("Enter index: "))
#         if zf == 0:
#             print("num_1")
#         elif zf == 1:
#             print("num_2")
#         elif zf == 2:
#             print("num_3")
#         elif zf == 3:
#             print("num_4")
#         elif zf == 4:
#             print("num_5")
# except ValueError:
#     print("Invalid index")
#     if fnm<0:
#         print(ValueError)
#     elif fnm>4:
#         print(ValueError)
#     if zf<0:
#         print(ValueError)
#     elif zf>4:
#         print(ValueError)


#4

#зроблено

#4.1

# num_1 = int(input("Enter number: "))
# num_2 = int(input("Enter number: "))
# num_3 = int(input("Enter number: "))
# num_4 = int(input("Enter number: "))
# num_5 = int(input("Enter number: "))
# list = [num_1,num_2,num_3,num_4,num_5]

# if fnm<0:
#     print("Invalid index")
# elif fnm>4:
#     print("Invalid index")
# if zf<0:
#     print("Invalid index")
# elif zf>4:
#     print("Invalid index")
# def listAct(list):
#     print("1 - show list, 2 - show maximum value, 3 - show minimum value, 4 - show value of element by index, 5 - show element by index ")
#     ch = int(input("Enter your choice: "))

#     if ch == 1:
#         print(list)
#     elif ch == 2:
#         print(max(list))
#     elif ch == 3:
#         print(min(list))
#     elif ch == 4:
#         fnm = int(input("Enter index: "))
#         if fnm == 0:
#             print(num_1)
#         elif fnm == 1:
#             print(num_2)
#         elif fnm == 2:
#             print(num_3)
#         elif fnm == 3:
#             print(num_4)
#         elif fnm == 4:
#             print(num_5)
#     elif ch == 5:
#         zf = int(input("Enter index: "))
#         if zf == 0:
#             print("num_1")
#         elif zf == 1:
#             print("num_2")
#         elif zf == 2:
#             print("num_3")
#         elif zf == 3:
#             print("num_4")
#         elif zf == 4:
#             print("num_5")



# print(listAct(list))



#4.2


# num_1 = int(input("Enter number: "))
# num_2 = int(input("Enter number: "))
# num_3 = int(input("Enter number: "))
# num_4 = int(input("Enter number: "))
# num_5 = int(input("Enter number: "))
# list = [num_1,num_2,num_3,num_4,num_5]

# def listAct(list):
#     try:
#        print("1 - show list, 2 - show maximum value, 3 - show minimum value, 4 - show value of element by index, 5 - show element by index ")
#        ch = int(input("Enter your choice: "))
#     except ValueError:
#        print("Invalid index")
#     if fnm<0:
#         print(ValueError)
#     elif fnm>4:
#         print(ValueError)
#     if zf<0:
#         print(ValueError)
#     elif zf>4:
#             print(ValueError)
#     if ch == 1:
#         print(list)
#     elif ch == 2:
#         print(max(list))
#     elif ch == 3:
#         print(min(list))
#     elif ch == 4:
#         fnm = int(input("Enter index: "))
#         if fnm == 0:
#             print(num_1)
#         elif fnm == 1:
#             print(num_2)
#         elif fnm == 2:
#             print(num_3)
#         elif fnm == 3:
#             print(num_4)
#         elif fnm == 4:
#             print(num_5)
#     elif ch == 5:
#         zf = int(input("Enter index: "))
#         if zf == 0:
#             print("num_1")
#         elif zf == 1:
#             print("num_2")
#         elif zf == 2:
#             print("num_3")
#         elif zf == 3:
#             print("num_4")
#         elif zf == 4:
#             print("num_5")



# print(listAct(list))