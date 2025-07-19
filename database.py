import sqlite3
from datetime import datetime

def dict_factory(cursor,row):
    d =  {}
    for idx,col in enumerate ( cursor.description):
        d[col[0]] =row [idx]
    return d
    
def connect_db():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = dict_factory
    return conn

def create_user(name,email,password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name,email,password) VALUES (?,?,?)",(name,email,password))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where id = ?", (id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?",(email,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email_and_password(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user
print(get_user_by_id(1))
def get_user_by_email_and_password(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, password, gender FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_avatar(user_id, avatar):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET avatar = ? WHERE id = ?', (avatar, user_id))
    conn.commit()
    conn.close()

def update_user(user_id, name, email, gender):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET name = ?, email = ?, gender = ? WHERE id = ?', (name, email, gender, user_id))
    conn.commit()
    conn.close()

print(get_user_by_id(2))
print(get_user_by_email("hellu@gmail.com"))

# Food Orders Functions
def add_food_order(food_name, address):
    """Thêm đơn hàng đồ ăn mới"""
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO food_orders (food_name, address)
        VALUES (?, ?)
    ''', (food_name, address))
    
    order_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return order_id

def get_all_food_orders():
    """Lấy tất cả đơn hàng đồ ăn"""
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, food_name, address, order_date
        FROM food_orders
        ORDER BY order_date DESC
    ''')
    
    orders = cursor.fetchall()
    conn.close()
    return orders

def delete_food_order(order_id):
    """Xóa đơn hàng đồ ăn theo ID"""
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM food_orders WHERE id = ?', (order_id,))
    
    conn.commit()
    conn.close()

# Trip Orders Functions
def add_trip_order(from_location, to_location, vehicle_type):
    """Thêm chuyến đi mới"""
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO trip_orders (from_location, to_location, vehicle_type)
        VALUES (?, ?, ?)
    ''', (from_location, to_location, vehicle_type))
    
    order_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return order_id

def get_all_trip_orders():
    """Lấy tất cả chuyến đi"""
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id, from_location, to_location, vehicle_type, order_date
        FROM trip_orders
        ORDER BY order_date DESC
    ''')
    
    orders = cursor.fetchall()
    conn.close()
    return orders

def delete_trip_order(order_id):
    """Xóa chuyến đi theo ID"""
    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM trip_orders WHERE id = ?', (order_id,))
    
    conn.commit()
    conn.close()