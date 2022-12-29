names_list = []
phones_list = []

def init():
    
    with open('names.csv', 'r', encoding='UTF-8') as data:

        for name in data:
            name = name.replace('\n', '')
            names_list.append(list(name.split(';')))

    with open('phones.csv', 'r', encoding='UTF-8') as data:

        for line in data:
            line = line.replace('\n', '')
            phones_list.append(list(line.split(';')))

def print_names():
    for id in range(len(names_list)):
        print(f'{names_list[id][0]}:{names_list[id][1]}')

def print_numbers_name(id_name: str):
    view = ''
    view += f'{str(names_list[(int(id_name))-1][1])} '
    view += str(f'{phones_list[(int(id_name))-1][1]} ')
    return (view)

def change_contact():
    print('Change contact mode')
    num = input('What contact are you want to change? ')
    for i in range(len(names_list)):
        if num == names_list[i][0]:
            print(
                f'Name is {names_list[i][1]}, \nIf you want to change, - input new NAME, or - keep it EMPTY')
            inputing = input()
            if inputing == '':
                break
            else:
                names_list[i][1] = inputing
    for i in range(len(phones_list)):
        if num == phones_list[i][0]:
            print(
                f'Number is "{phones_list[i][1]}"\nIf you want to change, - input new NUMBER, or - keep it EMPTY')
            inputing = input()
            if inputing != '':
                phones_list[i][1] = inputing

def checker_zero():
    if len(phones_list) == 0 and len(names_list) == 0:
        print('Your contact list is EMPTY, \nCreate a new contact? ')
        new_id_name = 1
        new_name = input('NAME? ')
        new_number = input('NUMBER? ')
        new_name = (new_id_name, new_name)
        new_name = list(new_name)
        names_list.append(new_name)
        new_number = (new_id_name, new_number)
        new_number = list(new_number)
        phones_list.append(new_number)

def add_contact():
    print("Add Contact mode")
    new_id_name = int(names_list[-1][0]) + 1
    new_name = input('NAME? ')
    new_number = input('NUMBER? ')
    new_name = (new_id_name, new_name)
    new_name = list(new_name)
    names_list.append(new_name)
    new_number = (new_id_name, new_number)
    new_number = list(new_number)
    phones_list.append(new_number)

def search_contact():
    print('Searching mode')
    search = input('Input NAME ').lower()
    for i in range(len(names_list)):
        if search == (str(names_list[i][1]).lower()):
            print(print_numbers_name(names_list[i][0]))
            break

def delete_contact():
    print('Delete mode')
    num = input(
        'What contact are you want to delete? \nKeep it EMPTY if NONE:\n')
    if num != '':
        for i in range(len(names_list)):
            if names_list[i][0] == num:
                names_list.pop(i)
                break
        for i in range(len(phones_list)):
            if phones_list[i][0] == num:
                phones_list.pop(i)
                break

def refresher_db():
    with open('names.csv', 'w') as data:
        for i in range(len(names_list)):
            for j in range(2):
                if j != 1:
                    data.write(str(names_list[i][j]))
                    data.write(';')
                else:
                    data.write(str(names_list[i][j]))
            data.write('\n')
        with open('phones.csv', 'w') as data:
            for i in range(len(phones_list)):
                for j in range(2):
                    if j != 1:
                        data.write(str(phones_list[i][j]))
                        data.write(';')
                    else:
                        data.write(str(phones_list[i][j]))
                data.write('\n')

def sort_after_delete():
       
    if names_list[-1][0] == str(len(names_list)):
        print('ok') 
    else:
        for i in range(len(names_list)):
            if i+1 == int(names_list[i][0]):
                print()
            else:
                names_list[i][0] = i+1
                phones_list[i][0] = i+1
        

