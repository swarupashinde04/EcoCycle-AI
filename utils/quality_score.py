import random

def calculate_quality():

    score = random.randint(60, 100)

    if score >= 90:
        grade = "Excellent"

    elif score >= 75:
        grade = "Good"

    else:
        grade = "Average"

    return score, grade