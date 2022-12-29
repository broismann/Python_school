while True:
    name = input('Please enter your name: ')
    age = input(f'Helo {name}, please enter your age: ')
    if not age.isdigit() or int(age) <= 0:
        print('Sorry, wrong input:(')
    elif 0 < int(age) < 10:
        print(f'Hello, {name}, tomboy :)')
    elif 10 < int(age) < 18:
        print(f'How is it going, {name}?')
    elif 18 < int(age) < 100:
        print(f'How can I help you, {name}?')
    else:
        print(f"{name}, I gues you're lying or Tibetan monk")
    stop_it = input(f'Hey {name}, do you want to exit? (Y/Д): ')
    if stop_it.upper() in ('Y', 'Д'):
        break
    else:
        print('Here we go again :)')
        continue
