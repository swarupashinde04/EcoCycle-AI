def calculate_ecoscore(weight):

    score = int(weight * 10)

    if score > 100:
        score = 100

    return score