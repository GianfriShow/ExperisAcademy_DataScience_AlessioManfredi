# 1
# you're managing a bookshop: create the classes Book and Bookshop
# the Book class should have the attributes: title, author, isbn (book ID, primary key)
# additionally, it should have a method description() returning a string with all the attribute info
# the class Bookshop should have the attribute 'catalogue' containing a list with all the Book objects
# additionally, it should have the methods:
# - add_book(book) taking a Book object input and adding it to the catalogue
# - remove_book(isbn) removing a book from the catalogue based on its ID
# - search_by_title(title) returning a list of books with the given title
# - show_catalogue() printing a description of all books in the catalogue