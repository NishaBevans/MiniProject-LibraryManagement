class Genre:
    def __init__(self, db):
        self.db = db
    
    def add_genre(self, name):
        query = "INSERT INTO genres (name) VALUES (%s)"
        self.db.execute_query(query, (name,))
    
    def display_genres(self):
        query = "SELECT * FROM genres"
        return self.db.fetch_query(query)
