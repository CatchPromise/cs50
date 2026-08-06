score = int(input("score: "))

if score >= 90 and score < 100:
    print("Grade: A, PASSED")
elif score >= 80 and score < 90:
    print("Grade B, GREAT")
elif score >= 70 and score < 80:
    print("Grade C, GOOD")
elif score >= 60 and score < 70:
    print("Grade D,OKAY")
elif score >= 50 and score < 60:
    print("Grade E,NO PROBLEM")
else:
    print("Grade F")