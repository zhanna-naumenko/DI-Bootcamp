#Exercise 1
print("Hello world\n" * 4 + "I love python\n" * 4)

#Exercise 2
season = int(input("Please input a month from 1 to 12: "))

if season == 12 or season == 1 or season == 2:
    print("This is a Winter season.")
elif season == 3 or season == 4 or season == 5:
    print("This is a Spring season.")
elif season == 6 or season == 7 or season == 8:
    print("This is a Summer season.")
elif season == 9 or season == 10 or season == 11:
    print("This is a Autumn season.")
else:
    print("The number is out of the range. Please try again.")


# season = int(input("Please input a month from 1 to 12: "))
# winter = [12, 1, 2]
# spring = range(3, 6)
# summer = range(6, 9)
# autumn = range(9, 12)
#
# if season in winter:
#     print("This is a Winter season.")
# elif season in spring:
#     print("This is a Spring season.")
# elif season in summer:
#     print("This is a Summer season.")
# elif season in autumn:
#     print("This is a Autumn season.")
# else:
#     print("The number is out of the range. Please try again.")