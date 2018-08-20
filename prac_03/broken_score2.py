def main():
    """Get an input of a score and display its value"""
    score = float(input("Enter score: "))
    result = score_check(score)
    print(score_check(score))


def score_check(score):
    """Determine type of result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent score"
    elif score >= 50:
        return "Pass score"
    else:
        return "Bad score"


main()
