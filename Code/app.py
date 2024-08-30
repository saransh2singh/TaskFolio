# import os
# from flask import Flask, render_template, request, redirect, url_for, jsonify
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# # Configure MySQL from environment variables
# app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
# app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
# app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'R_dra@123')
# app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'todo_app')
# app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# # Initialize MySQL
# mysql = MySQL(app)

# def init_db():
#     with app.app_context():
#         cur = mysql.connection.cursor()
#         cur.execute('''
#         CREATE TABLE IF NOT EXISTS items (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             title VARCHAR(255),
#             description TEXT
#         );
#         ''')
#         mysql.connection.commit()  
#         cur.close()

# # @app.route('/')
# # def hello():
# #     cur = mysql.connection.cursor()
# #     cur.execute('SELECT message FROM messages')
# #     messages = cur.fetchall()
# #     cur.close()
# #     return render_template('index.html', messages=messages)

# # @app.route('/submit', methods=['POST'])
# # def submit():
# #     new_message = request.form.get('new_message')
# #     cur = mysql.connection.cursor()
# #     cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
# #     mysql.connection.commit()
# #     cur.close()
# #     return jsonify({'message': new_message})
# @app.route('/')
# def index():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM items")
#     items = cur.fetchall()
#     cur.close()
#     return render_template('index.html', items=items)

# @app.route('/add', methods=['POST'])
# def add_item():
#     try:
#         name = request.form['name']
#         description = request.form['description']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
#         mysql.connection.commit()
#         cur.close()
#         return redirect('/')
#     except Exception as e:
#         print(f"Error: {e}")
#         mysql.connection.rollback()
#         return redirect('/')

# if __name__ == '__main__':
#     init_db()
#     app.run(host='0.0.0.0', port=5000, debug=True)







# from flask import Flask, request, redirect, url_for
# from flask_mysqldb import MySQL

# app = Flask(__name__)

# # MySQL configuration
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'R_dra@123'
# app.config['MYSQL_DB'] = 'todo_app'

# mysql = MySQL(app)

# @app.route('/')
# def index():
#     return '''
#         <form action="/add" method="POST">
#             Name: <input type="text" name="name"><br>
#             Description: <input type="text" name="description"><br>
#             <input type="submit" value="Add Item">
#         </form>
#     '''

# @app.route('/add', methods=['POST'])
# def add_item():
#     name = request.form.get('name')
#     description = request.form.get('description')

#     if not name or not description:
#         return "Both name and description are required!", 400

#     try:
#         cur = mysql.connection.cursor()
#         print(f"Executing SQL: INSERT INTO items (name, description) VALUES ({name}, {description})")
#         cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
#         mysql.connection.commit()
#         return redirect(url_for('index'))
#     except Exception as e:
#         print(f"SQL Execution Error: {e}")
#         mysql.connection.rollback()
#         return "An error occurred while adding the item.", 500
#     finally:
#         cur.close()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'R_dra@123')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'todo_app')
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_item():
    try:
        name = request.form['name']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    except Exception as e:
        print(f"Error: {e}")
        mysql.connection.rollback()
        return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

