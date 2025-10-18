class User:
    # In a real app, this data would come from a database
    users = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"},
    ]

    @classmethod
    def get_all_users(cls):
        return cls.users

    @classmethod
    def get_user_by_id(cls, user_id):
        return next((user for user in cls.users if user["id"] == user_id), None)
