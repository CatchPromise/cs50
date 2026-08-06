salary = int(input("Enter salary: "))

if salary < 0:
    print("invalid")
elif salary >= 0 and salary <= 20000:
    print("poverty")
elif salary >=30000 and salary <= 49999:
    print("below poverty")
elif salary >50001 and salary <= 100000:
    print("lower poverty")
elif salary >100001 and salary <= 150000:
    print("upper class")
elif salary > 1000000:
    print("wealthy")
