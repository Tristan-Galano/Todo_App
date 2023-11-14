from flask import Flask, render_template

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from config import Config


load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)



@app.route('/')
def index():
    name = 'TristanG'
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run()
 