import random

NUMBERS_PER_LINE = 6
MAX_NUMBER = 45
MIN_NUMBER = 1


def main():
    """Asks user for quick pick and generates them"""
    ask_quick_pick = int(input("How many quick picks do you want?: "))
    while ask_quick_pick <= 0:
        print("""That can't happen.
        Try again""")
        ask_quick_pick = int(input("How many quick picks do you want?: "))
    for i in range(ask_quick_pick):
        generated_quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            quick_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
            while quick_pick in generated_quick_pick:
                quick_pick = random.randint(MIN_NUMBER, MAX_NUMBER)
            generated_quick_pick.append(quick_pick)
        generated_quick_pick.sort()
        print(" ".join("{:2}".format(quick_pick) for quick_pick in generated_quick_pick))


main()
