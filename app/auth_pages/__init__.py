from flask import Blueprint, abort, render_template
from jinja2 import TemplateNotFound

auth_pages = Blueprint('auth_pages', __name__,
                         template_folder='templates')


@auth_pages.route('/about')
def about():
    try:
        return render_template('about.html')
    except TemplateNotFound:
        abort(404)
