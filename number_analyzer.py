while True:
    numbers = []
    even = []
    uneven = []

    while True:
        number = input('Enter a number or 0 to stop: ')
        try:
            value = int(number)
        except ValueError:
            print('Please enter a number.')
            continue
        if value == 0 and len(numbers) == 0:
            print('Please enter at least one number.')
            continue
        elif value == 0:
            break
        elif value % 2 == 0:
            even.append(value)
        else:
            uneven.append(value)
        numbers.append(value)

    while True:
        choice = input('Choose the operation (even/uneven/max/min/average or exit): ').lower().strip()
        if choice == 'exit':
            print('Thank you!')
            break
        elif choice == 'max':
            print(max(numbers))
        elif choice == 'min':
            print(min(numbers))
        elif choice == 'even':
            print(even)
        elif choice == 'uneven':
            print(uneven)
        elif choice == 'average':
            print(sum(numbers) / len(numbers))
        else:
            print('Please enter a valid choice.')
    while True:
        ar = input('Do you want to continue? (y/n): ')
        if ar in ['y', 'n']:
            break
        print('Please enter a valid choice.')

    if ar == 'n':
        break
