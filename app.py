from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        var_username = request.form['username']
        var_password = request.form['password']

        new_user = User(username=var_username, password=var_password)

        try: 
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
        except: 
            return "Something happened and we didn't save your user"
    else:
        return render_template('index.html')

@app.route('/users')
def test():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)