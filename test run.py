def search_item(item):
    file = open("Watched Movie List.txt", "r")
    for x in file:
        x = x.upper()
        item = item.upper()
        if item in x:
            x == item
            print('Found')

    file.close()

search_item('12 monkeys')
