from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)

# Database URI 
app.config['SQLALCHEMY_DATABASE_URI']  = "sqlite:///dag.db"

# Instantiate db 
db = SQLAlchemy(app)

# Importing tables 
from models.data import userdata

# Creating all databases and tables automatically before the first request
@app.before_first_request
def create():
    db.create_all()

# Our route 
@app.route('/')
@app.route('/name',methods=['POST','GET'])
def name():
    if request.method == 'POST':
        username_ = request.form.get('username')
        password_ = request.form.get('password')

        staging_data_with_dbtable = userdata(Username= username_, Password= password_)
        staging_data_with_dbtable.saveinfo()
        return 'Thanks for your registration'
    else:
        return render_template('index.html')

@app.route("/all" ,methods=['POST','GET'])
def all():
    all = userdata.query.all()
    return render_template("all.html", names_in_db = all)


if __name__ == '__main__':
    app.run(debug=True)