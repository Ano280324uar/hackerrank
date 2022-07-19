n = int(input())
#1 to 10 inclusive: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#1 to 10 exclusive: 1, 2, 3, 4, 5, 6, 7, 8, 9
if n%2!=0:
    print("Weird")
else:
    if n in range(2, 6): #range is an exclusive func, rang(2, 5) -> 2,3,4, we should to type range(2, 6) to make an inclusive range of 2 to 5
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")
