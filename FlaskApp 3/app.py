from flask import Flask, request, redirect, url_for, render_template,flash,session
from flask_sqlalchemy import SQLAlchemy
import sys
from flask.ext.wtf import Form
# import dbconnect
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


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
    user_id = 1
    user_name = hzong2
    user_zipcode = 61801

    def process_dict(inputlist, attr):
        outputlist = []
        for i in inputlist:
            dict_list = dict(zip(attr, i))
            outputlist.append(dict_list)
        return outputlist

    attr_food   = ('id', 'name', 'area', 'price', 'maker_id', 'description', 'available_amount', 'score', 'category_id')
    attr_search = ('name', 'area','price','description','available_amount', 'score','AVG_PRICE','AVG_SCORE','seller_score')

    if request.method == "POST":
        # search          = request.form['search']
        # price_all       = request.form['price']    #return true/false
        # price_low       = request.form['price_low']
        # price_high      = request.form['price_high']
        # foodscore_all   = request.form['foodscore']
        # foodscore_low   = request.form['foodscore_low']
        # foodscore_high  = request.form['foodscore_high']

        result = {'search': 'sdf',
                  'Food.price': {'select': 'descent', 'low': '3', 'high': '10'},
                  'Food.score': {'select': 'ascent', 'low': '2', 'high': ''},
                  'User.selling_score': {'select': 'null', 'low': '', 'high': ''},
                  'Food.available_amount': {'select': 'ascent', 'low': '1', 'high': '5'}}
        result = request.json
        sort = ''
        where = ''
        for attr in result:
            if attr == 'search':
                continue
            # print('attr',attr)
            # print('result[attr]',result[attr])
            # print(result[attr]['select'])

            if result[attr]['select'] == 'descent':
                sort = sort + attr + ' ' + 'DESC,'
            elif result[attr]['select'] == 'ascent':
                sort = sort + ' ' + attr + ','

            if result[attr]['low'] != '':
                # print('result[attr][low]',result[attr]['low'])
                where = where + ' ' + 'AND' + ' ' + attr + ">" + result[attr]['low']

            if result[attr]['high'] != '':
                # print('result[attr][high]',result[attr]['high'])
                where = where + ' ' + 'AND' + ' ' + attr + "<" + result[attr]['high']
        search = result['search']

        sort = sort[:-1]

        # user_id = request.args.get('')
        # sql_search  = 'SELECT * FROM Food WHERE name = "%s" ' % search
        # sql_search  = '(SELECT Food.name,Food.area,Food.price,Food.description,Food.available_amount,Food.score,AVG_PRICE,AVG_SCORE,User.selling_score FROM Food LEFT JOIN(SELECT Food.name, Food.area ,AVG(Food.price) AS AVG_PRICE,AVG(Food.score) AS AVG_SCORE FROM Food GROUP BY Food.name, Food.area) NEW_FOOD ON Food.name = NEW_FOOD.name AND Food.area = NEW_FOOD.area LEFT JOIN User ON Food.maker_id = User.id LEFT JOIN Category ON Food.category_id = Category.id WHERE Food.name LIKE "%%%s%%" OR Category.name LIKE "%%%s%%" OR User.name LIKE "%%%s%%" OR Food.area = "%s" ORDER BY Food.score DESC,Food.price,User.selling_score DESC,Food.available_amount DESC)' % (search,search,search,search)
        # sql_search  = '(SELECT Food.name,Food.area,Food.price,Food.description,Food.available_amount,Food.score,AVG_PRICE,AVG_SCORE,User.selling_score FROM Food LEFT JOIN(SELECT Food.name, Food.area ,AVG(Food.price) AS AVG_PRICE,AVG(Food.score) AS AVG_SCORE FROM Food GROUP BY Food.name, Food.area) NEW_FOOD ON Food.name = NEW_FOOD.name AND Food.area = NEW_FOOD.area LEFT JOIN User ON Food.maker_id = User.id LEFT JOIN Category ON Food.category_id = Category.id WHERE Food.name LIKE "%%%s%%" OR Category.name LIKE "%%%s%%" OR User.name LIKE "%%%s%%" OR Food.area = "%s" "%s" ORDER BY "%s")' % (search,search,search,search,where,sort)
        sql_search  = '(SELECT DISTINCT Food.name,Food.area,Food.price,Food.description,Food.available_amount,Food.score,AVG_PRICE,AVG_SCORE,User.selling_score FROM Food LEFT JOIN(SELECT Food.name, Food.area ,AVG(Food.price) AS AVG_PRICE,AVG(Food.score) AS AVG_SCORE FROM Food GROUP BY Food.name, Food.area) NEW_FOOD ON Food.name = NEW_FOOD.name AND Food.area = NEW_FOOD.area LEFT JOIN User ON Food.maker_id = User.id LEFT JOIN Food_Category ON Food.id = Food_Category.food_id LEFT JOIN Category ON Food_Category.category_id = Category.id WHERE Food.name LIKE "%%%s%%" OR Category.name LIKE "%%%s%%" OR User.name LIKE "%%%s%%" OR Food.area = "%s" %s ORDER BY %s)' % (search,search,search,search,where,sort)
        print(sql_search)
        search_list = db.session.execute(sql_search).fetchall()
        search_l    = process_dict(search_list, attr_search)
        print(search_l)
        return render_template('home.html', nearby = {},recommendation = {},search = search_l)

    elif request.method == 'GET':

        user   = 'hzong2'

        sql_nearby = 'SELECT * FROM Food LEFT JOIN User ON Food.area = User.zipcode WHERE User.name = "%s"' % user

        # sql_prefer = '(SELECT * FROM Food WHERE Food.category_id IN (SELECT DISTINCT Food.category_id FROM Suborder LEFT JOIN Orders ON Suborder.order_id = Orders.id LEFT JOIN User ON Orders.buyer_id = User.id LEFT JOIN Food ON Food.id = Suborder.food_id WHERE User.name = "%s")) UNION (SELECT * FROM Food WHERE Food.category_id IN (SELECT DISTINCT Food.category_id FROM Food LEFT JOIN Preference ON Food.category_id = Preference.category_id LEFT JOIN User ON Preference.user_id = User.id WHERE User.name = "%s" AND Food.area = User.zipcode))' % (user,user)
        sql_prefer = '(SELECT DISTINCT Food.* FROM Food, Food_Category WHERE Food_Category.food_id = Food.id AND Food_Category.category_id IN (SELECT DISTINCT Food_Category.category_id FROM Food_Category, Orders LEFT JOIN User ON Orders.buyer_id = User.id LEFT JOIN Food ON Food.id = Orders.food_id WHERE User.name = "nyn88" AND Food_Category.food_id = Food.id)) UNION(SELECT DISTINCT Food.* FROM Food,Food_Category WHERE Food.id = Food_Category.food_id AND Food_Category.category_id IN( SELECT DISTINCT Food_Category.category_id FROM Food_Category,User,Preference,Food WHERE User.id = Preference.user_id AND Food_Category.category_id = Preference.category_id AND User.id = Preference.user_id AND Food_Category.food_id = Food.id AND User.name = "nyn88" AND User.zipcode = Food.area))'

    prefer_list = db.session.execute(sql_prefer).fetchall()
    nearby_l    = process_dict(nearby_list, attr_food)
    prefer_l    = process_dict(prefer_list, attr_food)

    return render_template('home.html', nearby = nearby_l, recommendation = prefer_l,search = {})


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

# profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():

    user_name = hzong2

    def process_dict(inputlist, attr):
        outputlist = []
        for i in inputlist:
            dict_list = dict(zip(attr, i))
            outputlist.append(dict_list)
        return outputlist

    attr_food = ('id', 'name', 'area', 'price', 'maker_id', 'description', 'available_amount', 'score', 'category_id')

    if request.method == "POST":
        description = request.form['search']
        print(search)
        # user_id = request.args.get('')
        # sql_search  = 'SELECT * FROM Food WHERE name = "%s" ' % search
        sql_search = 'SELECT Food.name,Food.area,Food.price,Food.description,Food.available_amount,Food.score,AVG_PRICE,AVG_SCORE, User.selling_score FROM Food LEFT JOIN(SELECT Food.name,AVG(Food.price) AS AVG_PRICE,AVG(Food.score) AS AVG_SCORE FROM Food GROUP BY Food.name) NEW_FOOD ON Food.name = NEW_FOOD.name LEFT JOIN User ON Food.maker_id = User.id WHERE Food.name = ' % s
        ' ORDER BY Food.price,Food.score DESC,User.selling_score DESC' % search
        search_list = db.session.execute(sql_search).fetchall()
        search_l = process_dict(search_list, attr_food)
        return render_template('home.html', nearby={}, recommendation={}, search=search_l)

    elif request.method == 'GET':

        sql_maker = 'SELECT * FROM `Food` WHERE Food.maker_id = (SELECT User.id FROM User WHERE User.name = '%s')' % user_name

    maker_list = db.session.execute(sql_maker).fetchall()
    maker_l  = process_dict(maker_list, attr_food)

    return render_template('profile.html', maker = maker_l)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8008, debug= True)
