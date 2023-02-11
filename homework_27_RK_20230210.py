def geo_prog(start, ratio, count):
        current = start
        for item in range(count):
            yield current
            current *= ratio

progression = geo_prog(start=2, ratio=5, count=10)
for number in progression:
    print(number)