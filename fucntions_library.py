import os


def update_list():

    # user_data = input("Files location: ")

    file = open("Watched Movie List.txt", "w")
    data = os.listdir('F:\Movies\SEEN\Blank')
    i = 1
    for d in data:
        file.write(f"{i}] {d}")
        file.write('\n \n')
        i += 1

    file.close()
    print('List Updated')


def new_list():
    file_location = input("Files location: ")
    new_file_name = input("New List Name: ")
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
    print('Done')
