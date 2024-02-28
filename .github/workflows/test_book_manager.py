import unittest
from book_manager import Book, BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()

    def test_add_book(self):
        # Write test cases for adding books
        pass

    def test_remove_book(self):
        # Write test cases for removing books
        pass

    def test_list_books(self):
        # Write test cases for listing books
        pass

if __name__ == '__main__':
    unittest.main()

def test_add_book(self):
    # Create instances of books for testing
    book1 = Book("1234567890", "Book Title 1", "Author 1")
    book2 = Book("0987654321", "Book Title 2", "Author 2")

    # Add books to the manager
    self.manager.add_book(book1)
    self.manager.add_book(book2)

    # Verify that books are added correctly
    self.assertIn(book1, self.manager.books)
    self.assertIn(book2, self.manager.books)


def test_remove_book(self):
    # Create instances of books for testing
    book1 = Book("1234567890", "Book Title 1", "Author 1")
    book2 = Book("0987654321", "Book Title 2", "Author 2")

    # Add books to the manager
    self.manager.add_book(book1)
    self.manager.add_book(book2)

    # Remove a book by ISBN
    self.manager.remove_book("1234567890")

    # Verify that the specified book is removed
    self.assertNotIn(book1, self.manager.books)
    self.assertIn(book2, self.manager.books)



def test_list_books(self):
    # Create instances of books for testing
    book1 = Book("1234567890", "Book Title 1", "Author 1")
    book2 = Book("0987654321", "Book Title 2", "Author 2")

    # Add books to the manager
    self.manager.add_book(book1)
    self.manager.add_book(book2)

    # Get the list of books from the manager
    books_list = self.manager.list_books()

    # Verify that the returned list contains all added books
    self.assertEqual(len(books_list), 2)
    self.assertIn(book1, books_list)
    self.assertIn(book2, books_list)



