from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField

class CreateFeedbackForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=300), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=300), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    gender = SelectField('Rating', [validators.DataRequired()], choices=[('', 'Select'), ('1', 'Bad'), ('2', 'Average'), ('3', 'Good')], default='')
    membership = RadioField('Category', choices=[('W', 'Website'), ('S', 'Service'), ('P', 'Product')], default='')
    remarks = TextAreaField('Write-up of praises or complain ', [validators.Optional()])

