from flask_app import app
# Remember to continuously add controller files as you create them
from flask_app.controllers import controller_users

# This needs to be at the bottom
if __name__ == "__main__":
    app.run(debug=True)