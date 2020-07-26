from flask import Flask
from flask.json import jsonify
application = Flask(__name__)

from .scraper.scrape import scrape_for_names

@application.route('/<username>', methods=['GET'])
def get_pinned_repo_names(username):
    url = f'https://github.com/{username}/'
    names = scrape_for_names(url)
    return jsonify({ 'pinned_repos_names' : [name for name in names] } )