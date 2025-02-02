from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange

app = Flask(__name__)

class RegistrationForm(FlaskForm):
    # Отключаем CSRF-защиту
    class Meta:
        csrf = False

    email = StringField("Email", validators=[InputRequired(), Email()])
    phone = IntegerField("Phone", validators=[InputRequired(), NumberRange(min=1000000000, max=9999999999)])
    name = StringField("Name", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    index = StringField("Postal Code", validators=[InputRequired()])
    comment = StringField("Comment")

@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm(request.form)
    
    if form.validate():
        email, phone, postal_code = form.email.data, form.phone.data, form.index.data
        return f"Successfully registered user {email} with phone +7{phone} and postal code {postal_code}"
    else:
        errors = [f"{field.label.text}: {field.errors[0]}" for field in form if field.errors]
        return f"Registration failed: {'; '.join(errors)}"

if __name__ == "__main__":
    app.run(debug=True)