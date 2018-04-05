grocery_list = ['juice', 'tomatoes', 'potatoes', 'bananas']

if __name__ == '__main':
    print(grocery_list)
    print(grocery_list[1])
    print(grocery_list[1:2])

    other_events = ['wash car', 'pick up kids', 'driver car', 'cash check']

    to_do_list = [other_events, grocery_list]

    print(to_do_list)
    print(to_do_list[1][1])

    grocery_list.append('Onions')
    print(to_do_list)

    grocery_list.insert(1, 'Pickle')

    grocery_list.remove('juice')

    grocery_list.sort()

    grocery_list.reverse()

    del grocery_list[4]

    print(to_do_list)

    to_do_list2 = other_events + grocery_list

    print(to_do_list2)

    print(len(to_do_list2))
    print(max(to_do_list2))
    to_do_list2.insert(2, 'zdasddas')
    print(to_do_list2)
    print(max(to_do_list2))
    print(min(to_do_list2))

