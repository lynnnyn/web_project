from flask import Flask, request, redirect, url_for, render_template,flash,session
from flask_sqlalchemy import SQLAlchemy
import sys
from flask.ext.wtf import Form
import dbconnect


app = Flask(__name__)
app.secret_key = 'my is some_secret'
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



    def __repr__(self):
        return '<User, id: %r, name: %r, password_hash: %r, email: %r, phone_number: %r, address: %r, gender: %r, selling_score: %r, purchasing_score: %r, zipcode: %r>' % (
        self.id, self.name, self.password_hash, self.email, self.phone_number, self.address, self.gender,
        self.selling_score, self.purchasing_score, self.zipcode)

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

    def __repr__(self):
        return '<Preference, user_id: %r, category_id: %r>' % (self.user_id, self.category_id)




# 主页
@app.route('/', methods = ['GET','POST'])
def home():

    if request.method == "POST":
        search = request.form['search']
        print(search)
        # user_id = request.args.get('')
        return render_template('home.html', nearby = {},recommendation = {},search = search)

    elif request.method == 'GET':
        search = 'coffee'
        sql_search = 'SELECT * FROM Food WHERE name = "%s" ' % search
        location = 'urbana'
        sql_nearby = 'SELECT * FROM Food WHERE area = "%s" ' % location
        prefer = 'lynn'
        # sql_prefer = 'SELECT * FROM User left join Preference on User.id = Preference.user_id WHERE User.name = "%s" ' % prefer
        sql_prefer = 'SELECT * FROM User left join Preference on User.user_id = Preference.user_id WHERE User.user_name = "%s" ' % prefer



    def process_dict(inputlist, attr):
        outputlist = []
        for i in inputlist:
            dict_list = dict(zip(attr,i))
            outputlist.append(dict_list)
        return outputlist


    attr_food   = ('id', 'name', 'area', 'price', 'maker_id', 'description', 'available_amount', 'score', 'category_id')
    attr_prefer = ('id', 'name','password_hash','email','phone_number','address','gender','selling_score','purchasing_score','zipcode','user_id','category_id')

    search_list = db.session.execute(sql_search).fetchall()
    nearby_list = db.session.execute(sql_nearby).fetchall()
    prefer_list = db.session.execute(sql_prefer).fetchall()
    search_l    = process_dict(search_list, attr_food)
    nearby_l    = process_dict(nearby_list, attr_food)
    prefer_l    = process_dict(prefer_list, attr_prefer)
    # print(prefer_l)


    return render_template('search.html', nearby = nearby_l, recommendation = prefer_l,search = search_l)




    # pass
#
# # 附近，利用area
# @app.route('/nearby/', methods = ['GET'])
# def nearby():
#
#     if request.method == 'GET':
#         location = 'urbana' # 此处用于提取用户位置,用户登陆后修改此处代码
#
#         # user_id = request.args.get('user_id')
#         # sql = 'SELECT * FROM Food left join User on User.zipcode = Food.area WHERE User.id = "%s" '%user_id
#
#         sql = 'SELECT * FROM Food WHERE area = "%s" ' % location
#         food_list = db.session.execute(sql).fetchall()
#         print(food_list)
#
#         if len(food_list) > 0:
#             result_str = 'Found %d food(s)!' % len(food_list)
#         else:
#             result_str = 'No food nearby!'
#         return render_template('nearby.html', result=result_str, food_list=food_list)

# 搜索

# @app.route('/search/',methods = ["GET"])
# def search():
#     if 'user_id' not in session:
#         return redirect(url_for('login'))
#     else:
#         myname = session['username']
#         if request.method == "GET" :
#             attempted_search = request.args.get('attempted_search')
#             attempted_search = 'coffee' # 此处用于获取用户搜索字符串，正常传入数据后此句应注释
#
#             sql = 'SELECT * FROM Food WHERE name = "%s" ' %attempted_search
#             food_list = db.session.execute(sql).fetchall()
#             if len(food_list) > 0:
#                 result_str = 'Found %d food(s)!' % len(food_list)
#             else:
#                 result_str = 'That food do not exist! Please search another!'
#             return render_template('search.html', result=result_str, food_list=food_list)


# # preferred
#
# @app.route('/preferred/',methods = ["GET"])
# def prefer():
#     # if 'user_id' not in session:
#     #     return redirect(url_for('login'))
#     # else:
#     #     myname = session['username']
#     if request.method == "GET":
#         # preferred = request.args.get('attempted_search')
#         preferred = 'lynn' # 此处用于获取用户搜索字符串，正常传入数据后此句应注释
#
#         sql = 'SELECT * FROM User left join Preference on User.user_id = Preference.user_id WHERE User.user_name = "%s" ' %preferred     #电脑test用
#         # sql = 'SELECT * FROM User left join Preference on User.id = Preference.user_id WHERE User.name = "%s" ' % preferred   #cpanel
#         food_list = db.session.execute(sql).fetchall()
#         if len(food_list) > 0:
#             result_str = 'Found %d food(s)!' % len(food_list)
#         else:
#             result_str = 'No preferred food!'
#         return render_template('prefer.html', result=result_str, food_list=food_list)
#


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8008, debug= True)
