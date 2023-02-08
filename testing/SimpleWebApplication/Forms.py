from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms.fields import EmailField, DateField

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=300), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=300), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    gender = SelectField('Rating', [validators.DataRequired()], choices=[('', 'Select'), ('1', 'Bad'), ('2', 'Average'), ('3', 'Good')], default='')
    membership = RadioField('Category', choices=[('W', 'Website'), ('S', 'Service'), ('P', 'Product')], default='')
    remarks = TextAreaField('Write-up of praises or complain ', [validators.Optional()])

class CreateCustomerForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    gender = SelectField('Gender', [validators.DataRequired()], choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date Joined', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    membership = RadioField('Membership', choices=[('F', 'Fellow'), ('S', 'Senior'), ('P', 'Professional')], default='F')
    remarks = TextAreaField('Remarks', [validators.Optional()])
