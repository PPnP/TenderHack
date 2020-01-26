from flask.views import MethodView
from flask import render_template


class IndexPageController(MethodView):
    def get(self, flag):
        if flag == '1':
            return render_template('index1.html')
        else
            return render_template('index2.html')
