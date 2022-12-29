import controller as c
import os
import sys
def initialisation():
    c.init()
    c.checker_zero()
    clear = lambda: os.system('cls')
    ex = True
    while ex == True:
        clear()
        c.print_names()
        value = input('-----------------\n1. Select contact \n2. Add contact\n3. Delete contact\n4. Search contact\n5. Change contact\n>>> ')
        match value:
            case '1': 
                v =  input("Select contact ")
                clear()
                print(c.print_numbers_name(v))
                v = input('Press any key ')
            case '2':
                c.add_contact()
                c.refresher_db
            case '3':
                c.delete_contact()
                c.sort_after_delete()
                c.refresher_db()
            case '4':
                clear()
                c.search_contact()
                v = input('Press any key ')
            case '5':
                c.change_contact()
                clear()
                v = input('Press any key ')
                c.refresher_db()
            case '':
                c.refresher_db()
            case 'exit':
                print('Shutting down')
                sys.exit()    
            case __:
                print("Incorrect")

                
            

        

