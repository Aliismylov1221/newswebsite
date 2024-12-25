from flask import Flask
from controllers.news_controller import news_controller

# Initialize the Flask application
app = Flask(__name__)

# Register the news controller blueprint
app.register_blueprint(news_controller)

# Route for the home page (optional)
@app.route('/')
def home():
    return "Welcome to the News Media API!"

# Main entry point to run the app
if __name__ == '__main__':
    # Run the Flask application with debug mode enabled
    app.run(debug=True)
