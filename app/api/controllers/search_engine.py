from flask.views import MethodView
from flask import render_template


class SearchEngineController(MethodView):
    def get(self, flag):
        if flag == '1':
            return render_template('search.html', flag=1)
        else:
            return render_template('search.html', flag=0)
