from flask import Flask, render_template
from models.user import User

app = Flask(__name__)

# Home route that displays all users
@app.route('/')
def index():
    users = User.get_all_users()  # Get all users from the model
    return render_template('index.html', users=users)  # Pass data to the view

# User details route
@app.route('/user/<int:user_id>')
def user_details(user_id):
    user = User.get_user_by_id(user_id)  # Get specific user
    if user:
        return render_template('user_details.html', user=user)  # Pass user data to the view
    else:
        return f"User with ID {user_id} not found", 404

if __name__ == '__main__':
    app.run(debug=True)
