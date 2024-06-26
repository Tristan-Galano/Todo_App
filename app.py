from flask import Flask, render_template, jsonify, request, redirect,url_for
from forms import TaskForm

from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

from config import Config


load_dotenv('./.flaskenv')

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
import models
app.app_context().push()

@app.route('/')
def index():
    tasks = models.Task.query.all()
    if request.headers.get('X-Requsted-With') =='XMLHttpRequest':
        return jsonify(tasks)
        
    return render_template('index.html',tasks=tasks)

@app.route('/create', methods=['POST'])
def create_task():
    user_input = request.get_json()
    form = TaskForm (data=user_input)

    if form.validate():
        task = models.Task(name=form.name.data)
        
        db.session.add(task)
        db.session.commit()

        return jsonify(task)
    
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete():
    
    task_id = request.get_json().get('id')
    task = models.Task.query.filter_by(id = task_id).first()
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'result':'ok'}), 200


@app.route('/complete', methods=['POST'])
def complete():
    
    task_id = request.get_json().get('id')
    task = models.Task.query.filter_by(id = task_id).first()
    
    task.completed =True
    db.session.add(task)
    db.session.commit()
    
    return jsonify({'result':'ok'}), 200
if __name__ == '__main__':
    app.run()
 