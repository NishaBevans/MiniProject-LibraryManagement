from connect_mysql import connect_database

class Book:
    def __init__(self, db):
        self.db = db
    
    def add_book(self, title, author_id, genre_ids, publication_year, available_copies):
        # Add book to the Books table
        query = "INSERT INTO books (title, author_id, publication_year, available_copies) VALUES (%s, %s, %s, %s)"
        data = (title, author_id, publication_year, available_copies)
        self.db.execute_query(query, data)

        # Get the ID of the newly inserted book
        query = "SELECT LAST_INSERT_ID()"
        book_id = self.db.fetch_query(query)[0]['LAST_INSERT_ID()']

        # Associate book with genres
        for genre_id in genre_ids:
            query = "INSERT INTO book_genres (book_id, genre_id) VALUES (%s, %s)"
            self.db.execute_query(query, (book_id, genre_id))
    
    def search_books(self, title=None, author_name=None):
        query = "SELECT b.book_id, b.title, a.name AS author, b.publication_year, b.available_copies " \
                "FROM books b JOIN authors a ON b.author_id = a.author_id"
        filters = []
        if title:
            query += " WHERE b.title LIKE %s"
            filters.append(f"%{title}%")
        if author_name:
            query += " AND a.name LIKE %s" if title else " WHERE a.name LIKE %s"
            filters.append(f"%{author_name}%")
        
        return self.db.fetch_query(query, tuple(filters))

    def display_books(self):
        query = "SELECT * FROM books"
        return self.db.fetch_query(query)
