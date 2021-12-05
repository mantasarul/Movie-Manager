import os


def update_list():
    # user_data = input("Files location: ")

    file = open("Watched Movie List.txt", "w")
    data = os.listdir("F:\Movies\SEEN\Blank")
    i = 1
    for d in data:
        file.write(f"{i}] {d}")
        file.write('\n \n')
        i += 1

    file.close()
    print('\n\nList Updated')


def new_list():
    while True:
        file_location = input("Files location: ")
        if file_location == '#$':
            break
        new_file_name = input("New List Name: ")
        if new_file_name == '#$':
            break
        txt = '.txt'
        new_file_name = new_file_name + txt
        file = open(new_file_name, "w")
        data = os.listdir(file_location)
        i = 1
        for d in data:
            file.write(f"{i}] {d}")
            file.write('\n \n')
            i += 1

        file.close()
        print('\n\nDone')


def search():
    while True:
        file = open("Watched Movie List.txt", "r")
        search_item = input("Enter Movie Name: ")
        found = False
        for x in file:
            x = x.upper()
            search_item = search_item.upper()
            if search_item in x:
                found = True
        if found:
            print("Found")
        elif search_item == '#$':
            break
        else:
            print("Not Found")
        file.close()


while True:
    menu = input("""
PRESS 1 TO UPDATE DEFAULT LIST
PRESS 2 TO CREATE NEW LIST
PRESS 3 TO SEARCH IN DEFAULT LIST
PRESS 4 TO EXIT
PRESS #$ TO GO BACK
Choose option from above: """)
    print("\n")
    if menu == '1':
        update_list()
    elif menu == '2':
        new_list()
    elif menu == '3':
        search()
    elif menu == '4':
        break
    else:
        print('Invalid Input')
        exit()



