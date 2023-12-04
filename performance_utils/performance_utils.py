import timeit


def measure_performance(name, func, *args):
    warmup_start = timeit.default_timer()

    for _ in range(1000):
        func(*args)
    warmup_end = timeit.default_timer()
    print(
        f"Finished 1000 warmup runs for {name} in ~{(warmup_end - warmup_start):.2f} seconds."
    )

    starts = []
    ends = []
    for _ in range(10000):
        starts.append(timeit.default_timer())
        answer = func(*args)
        ends.append(timeit.default_timer())

    print(
        f"{name.capitalize()} answer: \033[92m{answer}\x1b[0m. Ran 10000 times in ~{(sum(ends) / len(starts) - sum(starts) / len(starts)) * 1000:.2f} milliseconds on average.\n"
    )
