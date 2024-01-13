import json

DEFAULT_FOLDER = 'diaries/'


class Book:
    def __init__(self, 
                 title: str, 
                 author: str, 
                 year: int,
                 month: str,
                 day: int,
                 publication_year: int,
                 genre: list[str],
                 number_of_pages: int,
                 ):
        self.title = title
        self.author = author
        self.year = year
        self.month = month
        self.day = day
        self.publication_year = publication_year
        self.genre = genre
        self.number_of_pages = number_of_pages

    def return_json(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'month': self.month,
            'day': self.day,
            'publication_year': self.publication_year,
            'genre': self.genre,
            'number_of_pages': self.number_of_pages,
        }


class Diary:
    def __init__(self):
        self.books: list[Book] = []
    
    def load(path: str):
        diary = Diary()

        # Check that path is correct
        if path[:len(DEFAULT_FOLDER)] != DEFAULT_FOLDER:
            path = DEFAULT_FOLDER + path
        if path[-5:] != '.json':
            path += '.json'
            
            
        with open(path, 'r') as file:
            json_to_load = json.load(file)

        for book in json_to_load["books"]:
            diary.books.append(Book(
                title=book['title'],
                author=book['author'],
                year=book['year'],
                month=book['month'],
                day=book['day'],
                publication_year=book['publication_year'],
                genre=book['genre'],
                number_of_pages=book['number_of_pages'],
            ))
        
        return path, diary

    def save(self, path: str):
        json_to_save = {"books": [
            book.return_json() for book in self.books
        ]}

        path = DEFAULT_FOLDER + path
        if path[-5:] != '.json':
            path += '.json'
        
        with open(path, 'w') as file:
            json.dump(json_to_save, file)

        return path
    
    def add_book(self, book: Book):
        self.books.append(book)

    def get_books(self, author_filter: str = None, title_filter: str = None):
        if author_filter is None and title_filter is None:
            return self.books.copy()
        elif author_filter is not None:
            return [book for book in self.books if book.author == author_filter].copy()
        elif title_filter is not None:
            return [book for book in self.books if book.title == title_filter].copy()
        else:
            return [book for book in self.books if book.author == author_filter and book.title == title_filter].copy()
    
    def remove_book(self, book: Book):
        self.books.remove(book)
