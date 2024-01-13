import os
from data_classes import Diary, Book
from data_classes import DEFAULT_FOLDER


def print_red(text: str):
    print(f'\033[91m{text}\033[0m')


def print_green(text: str):
    print(f'\033[92m{text}\033[0m')


def input_blue(text: str):
    return input(f'\033[94m{text}\033[0m')


def requires_open_diary(func):
    def wrapper(self, *args, **kwargs):
        if self.diary_is_open():
            return func(self, *args, **kwargs)
        else:
            print_red('You are not working on a diary. Create or load one first.')
    return wrapper


def requires_closed_diary(func):
    def wrapper(self, *args, **kwargs):
        if self.diary_is_open():
            print_red('You are already working on a diary. Delete or close it first.')
        else:
            return func(self, *args, **kwargs)
    return wrapper


class ProgramController():
    def __init__(self):
        self.current_diary = None


    def help(self):
        print_green('List of commands:')
        print("""
    - show (shows books in currently opened diary)
    - close (closes current diary)
    - create (creates new diary object)
    - save {diary_name} (saves currently open diary with specified name)
    - load {diary_name} (opens diary if it exists in folder diaries/)
    - insert {book_title} (creates a new book object. It will ask you for data like author, genre etc.)
    - find title:"{title_name}" author:"{author_name}" (finds all books with title/author provided. You can write only title or only author if you want.)
    - remove title:"{title_name}" author:"{author_name}" (if you don't provide any parameters, all books will be deleted.)
    - delete {diary_name} (deletes diary with specified name)""")


    def diary_is_open(self):
        if self.current_diary is None:
            return False
        else:
            return True


    @requires_open_diary
    def close(self):
        self.current_diary = None
        print_green('Closed the diary.')


    @requires_open_diary
    def show(self):
        current_books = self.current_diary.get_books()
        if len(current_books) == 0:
            print_green('You are working on an empty diary.')
        else:
            for i, book in enumerate(current_books):
                print_green(f'{i+1}: {book.title} by {book.author}')


    @requires_closed_diary
    def create_diary(self):
        self.current_diary = Diary()
        print_green(f'Created a new diary.')


    @requires_open_diary
    def save_diary(self, path: str):
        if len(path.strip()) == 0:
            print_red('Diary save path cannot be empty.')
        else:
            try:
                saved_path = self.current_diary.save(path)
                print_green(f'Saved a diary at "{saved_path}".')
            except Exception as e:
                print_red(f'Error while saving a diary: {e}')


    @requires_closed_diary
    def load_diary(self, path: str):
        if len(path.strip()) == 0:
            print_red('Diary load path cannot be empty.')
        else:
            try:
                actual_path, diary = Diary.load(path)
                self.current_diary = diary
                print_green(f'Loaded diary at "{actual_path}".')
            except FileNotFoundError:
                print_red(f"Error while loading a diary - diary {path} doesn't exist.")
            except Exception as e:
                print_red(f'Error while loading a diary: {e}')

    @requires_open_diary
    def insert_book(self, book_title: str):
        try:
            new_book = Book(
                title=book_title,
                author=input_blue('Author (string): '),
                year=int(input_blue('Year (integer): ')),
                month=input_blue('Month (string): '),
                day=int(input_blue('Day (integer): ')),
                publication_year=int(input_blue('Publication year (integer): ')),
                genre=input_blue('Genres (string): '),
                number_of_pages=int(input_blue('Number of pages (integer): ')),
            )

            self.current_diary.add_book(new_book)
            print_green(f'Inserted a book "{new_book.title}".')
        except ValueError:
            print_red(f"ValueError. Seems like your input had an incorrect type.")
        except Exception as e:
            print_red(f'Error while inserting a book: {e}')


    def preprocess_input_filters(self, input_string: str):
        try:
            if 'author' in input_string:
                author = input_string.split('author:"')[1].split('"')[0]
            else:
                author = None
            
            if 'title' in input_string:
                title = input_string.split('title:"')[1].split('"')[0]
            else:
                title = None
            
            return author, title
        except Exception as e:
            print_red(f'Error while preprocessing input: {e}')
            return None, None


    @requires_open_diary
    def find_book(self, input_string: str):
        try:
            author, title = self.preprocess_input_filters(input_string)
            print(f'Looking for book with author: "{author}" and title: "{title}"')
            
            found_books = self.current_diary.get_books(author_filter=author, title_filter=title)
            if len(found_books) == 0:
                print_green('No books found.')
            else:
                for i, book in enumerate(found_books):
                    print_green(f'{i+1}: {book.title} by {book.author}')
        except Exception as e:
            print_red(f'Error while looking for a book: {e}')


    @requires_open_diary
    def remove_book(self, input_string: str):
        try:
            author, title = self.preprocess_input_filters(input_string)
            
            found_books = self.current_diary.get_books(author_filter=author, title_filter=title)
            if len(found_books) == 0:
                print_green('No books found.')
            else:
                print('Found these books:')
                for book in found_books:
                    print(f'"{book.title}" by "{book.author}".')
                inp = input_blue('Are you sure you want to remove these books? Type "yes" to confirm: ')
                
                if inp == 'yes':
                    print("AFFF", found_books)
                    for book in found_books:
                        print("AF", book.title)
                        self.current_diary.remove_book(book)
                    print_green('Removed all found books.')
                else:
                    print_green('Cancelled.')
        except Exception as e:
            print_red(f'Error deleting books: {e}')


    def delete_diary(self, path: str):
        if len(path.strip()) == 0:
            print_red('Diary delete path cannot be empty.')
        else:
            if path[:len(DEFAULT_FOLDER)] != DEFAULT_FOLDER:
                path = DEFAULT_FOLDER + path
            if path[-5:] != '.json':
                path += '.json'
            try:
                os.remove(DEFAULT_FOLDER + path)
                print_green(f'Deleted diary at "{DEFAULT_FOLDER + path}".')
            except FileNotFoundError:
                print_red(f"Error while deleting a diary - diary {path} doesn't exist.")
            except Exception as e:
                print_red(f'Error while deleting a diary: {e}')
