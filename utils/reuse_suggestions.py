def reuse_suggestion(plastic_type):

    suggestions = {

        "PET Bottle":
        "Convert it into a self-watering planter.",

        "Plastic Bag":
        "Reuse it as a grocery bag.",

        "Food Container":
        "Store household items or stationery.",

        "Milk Bottle":
        "Use it as a watering can.",

        "Plastic Cup":
        "Grow small indoor plants.",

        "Mixed Plastic":
        "Send it for proper recycling."
    }

    return suggestions.get(
        plastic_type,
        "Recycle responsibly."
    )