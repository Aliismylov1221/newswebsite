from flask import Blueprint, request, jsonify
from services.news_service import NewsService

# Initialize the Blueprint for news routes
news_controller = Blueprint('news_controller', __name__)

# Create an instance of NewsService
news_service = NewsService()

# Route for getting all news articles
@news_controller.route('/news', methods=['GET'])
def get_all_news():
    """
    Get all news articles.
    """
    news = news_service.get_all_news()
    return jsonify(news)

# Route for creating a new news article
@news_controller.route('/news', methods=['POST'])
def create_news():
    """
    Create a new news article.
    """
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        return jsonify({'error': 'Missing title or content'}), 400

    news = news_service.create_news(title, content)
    return jsonify(news.to_dict()), 201

# Route for getting a specific news article by ID
@news_controller.route('/news/<int:news_id>', methods=['GET'])
def get_news_by_id(news_id):
    """
    Get a specific news article by its ID.
    """
    news = news_service.get_news_by_id(news_id)
    if news:
        return jsonify(news)
    return jsonify({'error': 'News not found'}), 404
