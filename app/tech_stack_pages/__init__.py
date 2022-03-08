from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

tech_stack_pages = Blueprint('tech_stack_pages', __name__,
                         template_folder='templates', static_folder='static')


@tech_stack_pages.route('/', defaults={'page': 'index'})
@tech_stack_pages.route('/<page>')
def show(page):
    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)
