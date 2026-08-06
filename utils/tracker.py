def get_status(status):

    journey = {

        "Pending": 1,

        "Accepted": 2,

        "Pickup Scheduled": 3,

        "Completed": 4

    }

    return journey.get(status, 0)