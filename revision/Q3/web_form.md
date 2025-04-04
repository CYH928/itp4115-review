```python
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField 
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm): 
    password = # (a)
    submit = # (b)
```


### (a) Write down the code that creates a required Password field to password
`
password = PasswordField('Password', vaildators=[DataRequired()])
`

### (b) Write down the code that creates a submit field as a “Sign in” button
`
submit = SubmitField('Sign In')
`

---

# Optional:
```python
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm): 
    username = 
    remember_me = 
    confirmPassword = 
    message = 
```

# Write down the code that creates a required String field to username
`
username = StringField('Username', validators=[DataRequired()])
`

# Write down the code that creates a “Remember me” checkbox field
`
remember_me = BooleanField('Remember Me')
`

# Write down the code that creates a required Confirm Password field to password
`
confirmPassword = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
`

# Write down the code that creates a TextArea field to message
`
message = TextAreaField('Message', validators=[Length(min=1, max=1000)])
`