from flask_wtf import Form 
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class CurrencyRate(Form):
  currency1 = StringField('Currency 1', validators=[DataRequired("Please enter currency1")])
  currency2 = StringField('Currency 2', validators=[DataRequired("Please enter currency2")])
  
  submit = SubmitField('Currency Rate')

