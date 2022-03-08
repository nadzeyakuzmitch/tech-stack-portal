"""These are reusable template function"""
from os import getenv
import datetime

def utility_text_processors():

    def deployment_environment():
        return getenv('INPUT_FLASK_ENV', None)

    def current_year():
        currentDateTime = datetime.datetime.now()
        date = currentDateTime.date()
        year = date.strftime("%Y")
        return year

    return dict(
        deployment_environment=deployment_environment(),
        year=current_year()
    )



