"""
1.
"""
def return_largest(a, b, c):
    """ Return the largest of 3 numbers. """
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c
    return largest

"""
2.
"""
def return_count(n, last):
    """ Return the number of occurences of n between 0 and last. """
    counter = 0
    for i in range(last):
        if str(n) in str(i):
            counter += 1
    return counter

"""
3. Basic code structure of a library book lending system. 
"""
class Library:
    def __init__(name):
        pass

    def add(book):
        pass
    
    def lend(book):
        pass

    def accept(book):
        pass

class BookCategory:
    """ Categories of Books. """
    def __init__(name):
        pass

class Rating:
    """ Ratings of books by lenders. """
    def __init__():
        pass

    def rate(book, rating):
        pass

class Book:
    """ A Book instance is a record of a book in the library. """
    def __init__(name, category, year, isbn, author):
        pass

class Lender:
    """ A lender basically borrows and returns books. Books are lent 
        out in Library.lend() and accepted in Library.accept(). """
    def __init__():
        pass


""" 
4. Abstract Factory Design Pattern 
"""
class File:
    def __init__(name, file_type):
        pass

class StoreFile:
    def __init__(file_):
        store(file_.name, file_.file_type)
    
    def store(name, file_type):
        if file_type in ('txt', 'xls', 'ppt'):
            _store_document(name)
        elif file_type in ('psd', 'ai'):
            _store_design(name)
        else:
            _store_others(name)
    
    def _store_design(name):
        """ storage = Storage("Dropbox") """
        pass
    
    def _store_document(name):
        """ storage = Storage("Google Drive") """
        pass
    
    def _store_others(name):
        """ storage = Storage("Box.net") """
        pass
    
class Storage:
    """ Storage: Google Drive, Dropbox, Box.net """
    def __init__(name):
        pass
