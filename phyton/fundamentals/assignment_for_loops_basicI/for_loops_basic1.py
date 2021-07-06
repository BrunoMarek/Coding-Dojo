# Basic - Print all integers from 0 to 150.
for x in range(0, 151):
    print(x)

print("Next assignment")

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for y in range(5, 1001):
    if y % 5 == 0:
        print(y)

print("Next assignment")

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for counting in range(1, 101):
    if counting % 10 == 0:
        print("Coding Dojo")
    elif counting % 5 == 0:
        print("Coding")
    else:
        print(counting)

print("Next assignment")

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
for sum in range(0,500001,2):
    sum += sum
    print(sum)

print("Next assignment")

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for countdown in range(2018,-1, -4):
    print(countdown)

print("Next assignment")

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for flexcount in range(lowNum,highNum + 1):
    if flexcount % mult == 0:
        print(flexcount)