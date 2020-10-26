def time_to_min(in_time: str) -> int:
    """
    Turns human given string to time in minutes
    e.g. 10h 15m -> 615
    """
    times = [int(x.strip()) for x in in_time.strip("m").split("h")]
    assert len(times) <= 2
    if len(times) == 1:
        return times[0]
    else:
        return times[0] * 60 + times[1]


def rounder(money_dist: list, pot: int, to_coin: int = 2) -> list:
    """
    Rounds the money distribution while preserving total sum
    stolen from https://stackoverflow.com/a/44740221
    """

    def custom_round(x):
        """ Rounds a number to be divisible by to_coin specified """
        return int(to_coin * round(x / to_coin))

    rs = [custom_round(x) for x in money_dist]
    k = pot - sum(rs)
    assert k == custom_round(k)
    fs = [x - custom_round(x) for x in money_dist]
    indices = [
        i
        for order, (e, i) in enumerate(
            reversed(sorted((e, i) for i, e in enumerate(fs)))
        )
        if order < k
    ]
    return [r + 1 if i in indices else r for i, r in enumerate(rs)]


def score(times: list, pot: int, power: int = 0.1) -> list:
    """ Main scoring function that calculates the winnings """
    power_times = [x ** power for x in times]
    max_time, min_time = max(power_times), min(power_times)

    scores = [max_time - x for x in power_times]

    return [round(float(x) / sum(scores) * pot, 2) for x in scores]


if __name__ == "__main__":
    n_players = int(input("# of Players: ").strip())
    pot = int(input("CHF each Player contributes: ").strip()) * n_players

    input("\n")

    times = list()

    for n in range(1, n_players + 1):
        times.append(time_to_min(input(f"\nTime for player #{n}: ")))

    print("\n\n", rounder(score(times, pot), pot))