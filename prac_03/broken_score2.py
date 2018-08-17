"""
CP1404/CP5632 - Practical
Broken program to determine score status
The intention is that the score
must be between 0 and 100 inclusive;
90 or more is excellent;
50 or more is a pass;
below 50 is bad.
Rewrite the following programming attempt using the most efficient if-elif-else 'ladder' you can
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Your score is excellent")
elif score >= 50:
    print("Your score is a pass")
else:
    print("Your score is bad")
