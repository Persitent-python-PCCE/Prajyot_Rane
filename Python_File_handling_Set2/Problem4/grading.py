def get_grade(average):
    if average > 90:
        return "A"
    elif average > 75 and average < 89:
        return "B"
    elif average > 60 and average < 74:
        return "C"
    elif average > 40 and average < 59:
        return "D"
    else:
        return "F"
