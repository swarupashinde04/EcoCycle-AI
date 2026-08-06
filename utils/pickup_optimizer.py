def optimize_route(requests):

    requests = sorted(
        requests,
        key=lambda x: x["City"]
    )

    return requests