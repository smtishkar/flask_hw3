# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", 
# "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны 
# сохраняться в базе данных, а пароль должен быть зашифрован.

from flask import Flask, render_template, request
# from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from forms_1 import RegistrationForm
from base_model import User, db 






app = Flask(__name__)
app.config['SECRET_KEY'] = '5a72409473a717fb930c2c2b12523af335fe96b9de3dd5d86e8a6088c142ab54'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///site.db'
db.init_app(app)
csrf = CSRFProtect(app)




@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('Created DB!')


# @app.route('/')
# def index():
#     return "Hi"

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        print(email, password)

        user = User(username=username, last_name=last_name, password=password, email=email)
        user.password_hash(password)
        db.session.add(user)
        db.session.commit()
        return 'Registration succesfull!'
    return render_template('register.html', form=form)
        




if __name__ == '__main__':
    app.run(debug=True)