# Python Basic Programming Course Project

This is my Python project for the Python Basic Programming course at CTU (and hopefully getting Zapocet).

## Description

This program is a "reader's diary". The main file for this project is main.py. Run it to start working with your diaries. 

I wasn't fully sure how to interpret the instructions of the task, so this is how I understood it:
- there are objects called "diary".
- every diary has data about read books.
- diaries can be saved as separate objects. 
- diaries don't have anything in them except for 1 array of books.

## Instructions

Use the following commands to control the program:
- show (shows books in currently opened diary)
- close (closes current diary)
- create {diary_name} (creates new diary object)
- save {diary_name} (saves currently open diary with specified name)
- load {diary_name} (opens diary if it exists in folder diaries/)
- insert {book_title} (creates a new book object. It will ask you for data like author, genre etc.)
- find title:"{title_name}" author:"{author_name}" (finds all books with title/author provided. You can write only title or only author if you want.)
- remove title:"{title_name}" author:"{author_name}" (if you don't provide any parameters, all books will be deleted.)
- delete {diary_name}


## Requirements

To run this project, you need to have Python installed on your machine. The project is compatible with Python 3.x.

I used only default Python libraries as it was written in the task instructions.