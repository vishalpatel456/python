score = int(input("Enter the score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
elif score >= 35 and score < 60:
    print("Grade: E")
elif score >= 0 and score < 35:
    print("Grade: F")
else:
    print("Invalid score! Please enter a score between 0 and 100.")
