from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, BooleanField, DateField
from wtforms.validators import DataRequired, Length

CATEGORIES = [("tech", "Tech"), ("science", "Science"), ("lifestyle", "Lifestyle")]

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(max=100)])
    content = TextAreaField("Content", validators=[DataRequired()])
    category = SelectField("Category", choices=CATEGORIES)
    is_active = BooleanField("Active")
    publication_date = DateField("Publication Date", format="%Y-%m-%d")
    submit = SubmitField("Submit")
