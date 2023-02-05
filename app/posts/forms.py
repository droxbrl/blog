from wtforms import Form, StringField, TextAreaField


class PostFrom(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
   # tags = TextAreaField('Tags (if you want to ;)')
