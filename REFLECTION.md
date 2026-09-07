Passing Test:
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 0.007s

OK
Destroying test database for alias 'default'...

Failing Test:
Found 4 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F...
======================================================================
FAIL: test_book_appears_on_books_page (catalog.tests.BookListViewTests.test_book_appears_on_books_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/pjanota/Documents/CIDM_3312/book-catalog/catalog/tests.py", line 34, in test_book_appears_on_books_page
    self.assertContains(response, self.book.title)
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Test Book' in the following response
b'<!DOCTYPE html>\n<html lang="en">\n    <head>\n        <meta charset="UTF-8">\n        <title>Books</title>\n    </head>\n    <body>\n        <nav>\n            <a href="/">Books</a> |\n            <a href="/publishers/">Publishers</a> |\n            <a href="/reviews/">Reviews</a>\n        </nav>\n\n        <main>\n            \n<h1>Books</h1>\n\n\n        </main>\n    </body>\n</html>'

----------------------------------------------------------------------
Ran 4 tests in 0.006s

FAILED (failures=1)
Destroying test database for alias 'default'...

Was able to create this error by disabling any books from querying by adding the following lines in views.py
    def get_queryset(self):
        return Book.objects.none()

Essentially this error told me that it was unable to find the test database it created as part of my code essentially omitted all of the books from querying.

Question 1: 
    Question: Your models use two foreign keys. Pick one of them. Name which model carries the ForeignKey and which model it points at, and explain why you arranged it that way. What would be different about the data you entered if you had reversed it?
    Answer: One of the relationships I had was the Book carrying the ForeignKey that pointed to the Publisher. The reason for this is because of their cardinalities, a publisher can have many books, but a book can only have one publisher exactly.
    If I was to reverse the cardinality it could potentially duplicate the publisher, as a publisher can have one or many books, and a book can have exactly one publisher, a flipped version of this could mean that multiple of the exact same publisher
    exist one per book. Meaning if we were to need to know how many books a publisher had we would have to count every matching row of publishers.
\n
Question 2:
    Question: You added one field of your own to Book. Which field type did you choose, and why that type rather than another? What would you lose if you had stored the same fact as a CharField?
    Answer: The additional field I included was the publication_year as an IntegerField. I chose this because publication year is numeric in nature and allows us to further compare and order our database. Other data types would either be uneccesary or misleading.
    If I stored it as a CharField it would loose its sorting purpose. CharField sorts based on the string values not numbers so I would have to make additional complicated logic to have it work properly with numbers or some other data type.

