def geo_prog(start, ratio, count):
        current = start
        for item in range(count):
            yield current
            current *= ratio

progression = geo_prog(start=2, ratio=2, count=100)
for number in progression:
    print(number)