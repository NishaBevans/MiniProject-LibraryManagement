class User:
    def __init__(self, db):
        self.db = db
    
    def add_user(self, name, email, phone=None):
        query = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (name, email, phone))

    def view_user_details(self, user_id):
        query = "SELECT * FROM users WHERE user_id = %s"
        return self.db.fetch_query(query, (user_id,))
    
    def display_users(self):
        query = "SELECT * FROM users"
        return self.db.fetch_query(query)
