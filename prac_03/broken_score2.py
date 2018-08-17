def main():
    """Get an input of a score and display its value"""
    score = float(input("Enter score: "))
    result = score_check(score)
    if result == 1:
        print("Invalid score")
    elif result == 2:
        print("Your score is excellent")
    elif result == 3:
        print("Your score is a pass")
    elif result == 4:
        print("Your score is bad")


def score_check(score):
    """Determine type of result"""
    result = 0
    if score < 0 or score > 100:
        result += 1
    elif score >= 90:
        result += 2
    elif score >= 50:
        result += 3
    else:
        result += 4
    return result


main()
