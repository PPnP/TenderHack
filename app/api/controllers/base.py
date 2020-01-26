from flask import render_template, flash
from flask.views import MethodView
from flask_wtf import FlaskForm


class BaseController(MethodView):
    def post(self):
        form = self.get_form()
        if form.validate():
            return self.process(form)
        for error in list(form.errors.values()):
            flash(error[0])
        raise NotImplementedError('Form is invalid')

    def get_form(self) -> FlaskForm:
        raise NotImplementedError('Specify the form')

    def process(self, form: FlaskForm):
        raise NotImplementedError('Specify the action')
