times = []
n = int(input("How many people are there?\n").strip())
for i in n:
    print("\nPerson " + (i+1) + ":")
    times.append(float(input("How many minutes were you on your phone")))

def scores(times:list, pot_size):
    minimum = min(times)
    maximum = max(times) - minimum
    times = [(maximum - (time - minimum)/maximum) ** 5 for time in times]
    sum_times = sum(times)
    prizes = [pot_size * time / sum_times for time in times]
    return prizes

prizes = scores(times, pot_size)
for prize in prizes:
    print(prize)