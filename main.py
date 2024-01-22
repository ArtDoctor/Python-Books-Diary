from main_functions import ProgramController

def main(controller: ProgramController):
    command = input()
    if command == 'help':
        controller.help()
    elif command == 'close':
        controller.close()
    elif command == 'show':
        controller.show()
    elif command[:6] == 'create':
        controller.create_diary()
    elif command[:4] == 'save':
        controller.save_diary(command[5:])
    elif command[:4] == 'load':
        controller.load_diary(command[5:])
    elif command[:6] == 'insert':
        controller.insert_book(command[7:])
    elif command[:4] == 'find':
        controller.find_book(command[5:])
    elif command[:6] == 'remove':
        controller.remove_book(command[7:])
    elif command[:6] == 'delete':
        controller.delete_diary(command[7:])
    else:
        print('Unknown command. Type down "help" to see the list of commands.')

if __name__ == "__main__":
    controller = ProgramController()
    print('Welcome to the Book Diary!')
    print('Type down "help" to see the list of commands.')
    while True:
        main(controller)