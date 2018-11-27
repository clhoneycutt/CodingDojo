# Basic - Print all the numbers/integers from 0 to 150.

# for count in range(0, 151):
#     print(count)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000,000.

# x = 1
# while x > 0:
#     y = x * 5
#     print(y)
#     x += 1
#     if y == 1000000:
#         break


# Counting, the Dojo Way - Print integers 1 to 100.  If divisible by 5, print "Coding" instead.
# If by 10, also print " Dojo".


# for count in range(1, 101):
#     if count % 10 == 0:
#         print("Coding Dojo")
#     elif count % 5 == 0:
#         print("Coding")
#         continue
#     else:
#         print(count)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.


# total = 0
# for i in range(0,500001):
#     if i % 2 == 0:
#         continue
#     else:
#         total += i
#
# print(total)


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours (exclude 0).


# pos = 2018
# while pos > 0:
#     if pos % 4 == 0:
#         print(pos)
#     elif pos == 0:
#         break
#     pos -= 1


# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult
# from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)


# def flexCount(lowNum, highNum, mult):
#     for i in range(lowNum, highNum):
#         if i % mult == 0:
#             print(i)
#
#
# flexCount(5,20,2)


# Now, please predict the output for the following codes.

list = [3,5,1,2]
for i in list:
    print(i)

# ** Output: 3, 5, 1, 2


list = [3,5,1,2]
for i in range(list):
    print(i)

# ** Output: Error



list = [3,5,1,2]
for i in range(len(list)):
    print(i)

# ** Output: 1, 2, 3, 4

# 2 out of 3 predictions correct, and at least I was close on the last one. :)  retrospect: range is 4, but starts at 0 by default and doesn't include 