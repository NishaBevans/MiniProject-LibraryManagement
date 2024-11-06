class Author:
    def __init__(self, db):
        self.db = db
    
    def add_author(self, name, biography=None):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        self.db.execute_query(query, (name, biography))
    
    def view_author_details(self, author_id):
        query = "SELECT * FROM authors WHERE author_id = %s"
        return self.db.fetch_query(query, (author_id,))
    
    def display_authors(self):
        query = "SELECT * FROM authors"
        return self.db.fetch_query(query)
