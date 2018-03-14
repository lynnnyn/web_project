from flask import Flask, request, redirect, url_for, render_template,flash,session
from flask_sqlalchemy import SQLAlchemy
import sys

import dbconnect


app = Flask(__name__)

# 连接数据库 mysql://用户名:密码@localhost:3306/数据库名?charset=utf8mb4
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:84302448@localhost:3306/foooooodie_program?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    phone_number  = db.Column(db.String(64))
    address  = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    selling_score = db.Column(db.Integer)
    purchasing_score = db.Column(db.Integer)

class Food(db.Model):
    __tablename__ = 'Food'
    food_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    area = db.Column(db.String(64))
    Ingredient = db.Column(db.String(64))
    Price = db.Column(db.String(64))
    maker = db.Column(db.String(64))
    Description = db.Column(db.String(64))
    Available_amount = db.Column(db.String(64))
    Food_score = db.Column(db.Integer)
    category = db.Column(db.String(64))

# 主页
@app.route('/', methods = ['GET'])
def index():
    pass

# 附近，利用area
@app.route('/nearby/', methods = ['GET'])
def nearby():
    if request.method == 'GET':
        location = 'urbana' # 此处用于提取用户位置,用户登陆后修改此处代码

        sql = 'SELECT * FROM Food WHERE area = "%s" ' % location
        food_list = db.session.execute(sql).fetchall()

        if len(food_list) > 0:
            result_str = 'Found %d food(s)!' % len(food_list)
        else:
            result_str = 'No food nearby!'
        return render_template('nearby.html', result=result_str, food_list=food_list)

# 搜索
@app.route('/search/',methods = ["GET"])
def search():
    if request.method == "GET" :
        attempted_search = request.args.get('attempted_search')
        attempted_search = 'coffee' # 此处用于获取用户搜索字符串，正常传入数据后此句应注释

        sql = 'SELECT * FROM Food WHERE name = "%s" ' %attempted_search
        food_list = db.session.execute(sql).fetchall()
        if len(food_list) > 0:
            result_str = 'Found %d food(s)!' % len(food_list)
        else:
            result_str = 'That food do not exist! Please search another!'
        return render_template('search.html', result=result_str, food_list=food_list)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8002, debug= True)
