from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
from database import *

class MessageBox():
    def success_box(self,message):
        box = QMessageBox()
        box.setWindowTitle("Success")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Information)
        box.exec()
    
    def error_box(self, message):
        box = QMessageBox()
        box.setWindowTitle("Error")
        box.setText(message)
        box.setIcon(QMessageBox.Icon.Critical)
        box.exec()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/login.ui", self)

        self.email = self.findChild(QLineEdit, "txt_email")
        self.password = self.findChild(QLineEdit, "txt_password")
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_eye_p = self.findChild(QPushButton, "btn_eye_p")

        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye_p.clicked.connect(lambda: self.hiddenOrShow(self.password, self.btn_eye_p))

    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
    def login(self):
        msg = MessageBox()
        email = self.email.text()
        password = self.password.text()

        if email =="":
            msg.error_box("Email không được để trống")
            self.email.setFocus()
            return
        if password =="":
            msg.error_box("Mật khẩu không được để trống")
            self.password.setFocus()
            return
        user = get_user_by_email_and_password(email, password)
        if user is not None:
            msg.success_box("Đăng nhập thành công")
            self.show_home(user["id"])
        else:
            msg.error_box("Email hoặc mật khẩu không chính xác")
            self.email.setFocus()

    def show_home(self, user_id):
        self.home = Home(user_id)
        self.home.show()
        self.close()

    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()

class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/register.ui", self)

        self.name = self.findChild(QLineEdit, "txt_name")
        self.email = self.findChild(QLineEdit, "txt_email")
        self.password = self.findChild(QLineEdit, "txt_password")
        self.confirm_password = self.findChild(QLineEdit, "txt_conf_pwd")
        self.btn_register = self.findChild(QPushButton, "btn_register")
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_eye_p = self.findChild(QPushButton, "btn_eye_p")
        self.btn_eye_cp = self.findChild(QPushButton, "btn_eye_cp")

        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.show_login)
        self.btn_eye_p.clicked.connect(lambda: self.hiddenOrShow(self.password, self.btn_eye_p))
        self.btn_eye_cp.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password, self.btn_eye_cp))

    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
    def register(self):
        msg = MessageBox()
        name = self.name.text()
        email = self.email.text()
        password = self.password.text()
        confirm_password = self.confirm_password.text()

        if name =="":
            msg.error_box("Họ tên không được để trống")
            self.name.setFocus()
            return
        if email =="":
            msg.eror_box("Email không được để trống")
            self.email.setFocus()
            return
        if password =="":
            msg.error_box("Mật khẩu không được để trống")
            self.password.setFocus()
            return
        if confirm_password =="":
            msg.error_box("Xác nhận mật khẩu không được để trống")
            self.confirm_password.setFocus()
            return
        if password != confirm_password:
            msg.error_box("Mật khẩu không trùng khớp")
            self.confirm_password.setText("")
            self.password.setFocus()
        if not self.validate_email(email):
            msg.error_box("Email không hợp lệ")
            self.email.setFocus()
            return
        check_email = get_user_by_email(email)
        if check_email is not None:
            msg.error_box("Email đã tồn tại")
            return
        create_user(name, email, password)
        msg.success_box("Đăng ký thành công")
        self.show_login()

    def validate_email(self, s):
        idx_at = s.find('@')
        if idx_at == -1:
            return False
        return '.' in s[idx_at+1:]

    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        
class CustomListItem(QWidget):
    """Widget tùy chỉnh cho item trong ListWidget với nút xóa"""
    delete_clicked = pyqtSignal(int)  # Signal để xóa item theo ID
    
    def __init__(self, item_id, text, parent=None):
        super().__init__(parent)
        self.item_id = item_id
        self.setup_ui(text)
    
    def setup_ui(self, text):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 2, 5, 2)
        
        # Label hiển thị text
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("""
            QLabel {
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 8px;
                margin-right: 5px;
            }
        """)
        
        # Nút xóa
        self.delete_btn = QPushButton("🗑️")
        self.delete_btn.setFixedSize(30, 30)
        self.delete_btn.setStyleSheet("""
            QPushButton {
                background-color: #ff4444;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #cc0000;
            }
        """)
        self.delete_btn.clicked.connect(self.on_delete_clicked)
        
        layout.addWidget(self.label, 1)
        layout.addWidget(self.delete_btn)
        
        self.setLayout(layout)
    
    def on_delete_clicked(self):
        self.delete_clicked.emit(self.item_id)

class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.user_id = user_id
        self.user = get_user_by_id(user_id)

        self.main_widget = self.findChild(QStackedWidget, "main_widget")
        self.main_widget.setCurrentIndex(0)
        
        # Navigation buttons
        self.btn_nav_home = self.findChild(QPushButton, "btn_nav_home")
        self.btn_nav_account = self.findChild(QPushButton, "btn_nav_account")
        self.btn_nav_trip = self.findChild(QPushButton, "btn_nav_trip")
        self.btn_nav_food = self.findChild(QPushButton, "btn_nav_food")
        self.btn_avatar = self.findChild(QPushButton, "btn_avatar")
        
        # Food ordering elements
        self.txt_food_name = self.findChild(QLineEdit, "txt_food_name")
        self.txt_food_address = self.findChild(QLineEdit, "txt_food_address")
        self.btn_order_food = self.findChild(QPushButton, "btn_order_food")
        self.list_food_orders = self.findChild(QListWidget, "list_food_orders")
        
        # Trip booking elements
        self.txt_from_location = self.findChild(QLineEdit, "txt_from_location")
        self.txt_to_location = self.findChild(QLineEdit, "txt_to_location")
        self.combo_vehicle_type = self.findChild(QComboBox, "combo_vehicle_type")
        self.btn_book_trip = self.findChild(QPushButton, "btn_book_trip")
        self.list_trip_orders = self.findChild(QListWidget, "list_trip_orders")
        
        # Connect signals
        self.btn_nav_home.clicked.connect(lambda: self.navMainScreen(0))
        self.btn_nav_account.clicked.connect(lambda: self.navMainScreen(1))
        self.btn_nav_trip.clicked.connect(lambda: self.navMainScreen(2))
        self.btn_nav_food.clicked.connect(lambda: self.navMainScreen(3))
        self.btn_avatar.clicked.connect(self.update_avatar)
        
        # Connect food and trip buttons
        self.btn_order_food.clicked.connect(self.add_food_order)
        self.btn_book_trip.clicked.connect(self.add_trip_order)
        
        # Connect update profile button
        self.btn_update_profile = self.findChild(QPushButton, "btn_update_profile")
        if self.btn_update_profile:
            self.btn_update_profile.clicked.connect(self.update_profile)
      
        self.loadAccountInfo()
        self.load_data()

    def loadAccountInfo(self):
        self.txt_name = self.findChild(QLineEdit, "txt_name")
        self.txt_email = self.findChild(QLineEdit, "txt_email")
        self.txt_name_2 = self.findChild(QLineEdit, "txt_name_2")  # password field
        self.combo_gender = self.findChild(QComboBox, "combo_gender")  # gender field
        
        avatar_path = self.user.get("avatar", "")
        if avatar_path:
            self.btn_avatar.setIcon(QIcon(avatar_path))
        
        self.txt_name.setText(str(self.user["name"]))
        self.txt_email.setText(str(self.user["email"]))
        self.txt_name_2.setText(str(self.user.get("password", "")))
        
        # Set gender in combo box
        gender = self.user.get("gender", "")
        if gender == "Male":
            self.combo_gender.setCurrentIndex(1)
        elif gender == "Female":
            self.combo_gender.setCurrentIndex(2)
        else:
            self.combo_gender.setCurrentIndex(0)  # None
        
        # Connect update button if exists
        if hasattr(self, 'btn_update_profile'):
            self.btn_update_profile.clicked.connect(self.update_profile)

    def load_data(self):
        """Load dữ liệu từ database"""
        self.load_food_orders()
        self.load_trip_orders()
    
    def load_food_orders(self):
        """Load danh sách đơn hàng đồ ăn"""
        self.list_food_orders.clear()
        orders = get_all_food_orders()
        
        for order in orders:
            order_id, food_name, address, order_date = order
            text = f"🍽️ {food_name}\n📍 {address}\n📅 {order_date}"
            
            # Tạo custom item với nút xóa
            item = QListWidgetItem()
            custom_widget = CustomListItem(order_id, text)
            custom_widget.delete_clicked.connect(self.delete_food_order)
            
            self.list_food_orders.addItem(item)
            self.list_food_orders.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint())
    
    def load_trip_orders(self):
        """Load danh sách chuyến đi"""
        self.list_trip_orders.clear()
        orders = get_all_trip_orders()
        
        for order in orders:
            order_id, from_location, to_location, vehicle_type, order_date = order
            text = f"🚗 {vehicle_type}\n📍 Từ: {from_location}\n🎯 Đến: {to_location}\n📅 {order_date}"
            
            # Tạo custom item với nút xóa
            item = QListWidgetItem()
            custom_widget = CustomListItem(order_id, text)
            custom_widget.delete_clicked.connect(self.delete_trip_order)
            
            self.list_trip_orders.addItem(item)
            self.list_trip_orders.setItemWidget(item, custom_widget)
            item.setSizeHint(custom_widget.sizeHint())
    
    def add_food_order(self):
        """Thêm đơn hàng đồ ăn mới"""
        food_name = self.txt_food_name.text().strip()
        address = self.txt_food_address.text().strip()
        
        if not food_name or not address:
            msg = MessageBox()
            msg.error_box("Vui lòng nhập đầy đủ thông tin!")
            return
        
        try:
            add_food_order(food_name, address)
            self.txt_food_name.clear()
            self.txt_food_address.clear()
            self.load_food_orders()
            msg = MessageBox()
            msg.success_box("Đặt hàng thành công!")
        except Exception as e:
            msg = MessageBox()
            msg.error_box(f"Không thể đặt hàng: {str(e)}")
    
    def add_trip_order(self):
        """Thêm chuyến đi mới"""
        from_location = self.txt_from_location.text().strip()
        to_location = self.txt_to_location.text().strip()
        vehicle_type = self.combo_vehicle_type.currentText()
        
        if not from_location or not to_location:
            msg = MessageBox()
            msg.error_box("Vui lòng nhập đầy đủ thông tin!")
            return
        
        try:
            add_trip_order(from_location, to_location, vehicle_type)
            self.txt_from_location.clear()
            self.txt_to_location.clear()
            self.load_trip_orders()
            msg = MessageBox()
            msg.success_box("Đặt xe thành công!")
        except Exception as e:
            msg = MessageBox()
            msg.error_box(f"Không thể đặt xe: {str(e)}")
    
    def delete_food_order(self, order_id):
        """Xóa đơn hàng đồ ăn"""
        msg = MessageBox()
        reply = QMessageBox.question(self, "Xác nhận", 
                                   "Bạn có chắc muốn xóa đơn hàng này?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                delete_food_order(order_id)
                self.load_food_orders()
                msg.success_box("Đã xóa đơn hàng!")
            except Exception as e:
                msg.error_box(f"Không thể xóa đơn hàng: {str(e)}")
    
    def delete_trip_order(self, order_id):
        """Xóa chuyến đi"""
        msg = MessageBox()
        reply = QMessageBox.question(self, "Xác nhận", 
                                   "Bạn có chắc muốn xóa chuyến đi này?",
                                   QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                delete_trip_order(order_id)
                self.load_trip_orders()
                msg.success_box("Đã xóa chuyến đi!")
            except Exception as e:
                msg.error_box(f"Không thể xóa chuyến đi: {str(e)}")

    def update_profile(self):
        """Cập nhật thông tin profile"""
        name = self.txt_name.text().strip()
        email = self.txt_email.text().strip()
        password = self.txt_name_2.text().strip()
        gender = self.combo_gender.currentText()
        
        if not name or not email:
            msg = MessageBox()
            msg.error_box("Tên và email không được để trống!")
            return
        
        try:
            # Update user info
            update_user(self.user_id, name, email, gender)
            
            # Update password if changed
            if password and password != self.user.get("password", ""):
                # You might want to add a separate function for password update
                pass
            
            # Reload user data
            self.user = get_user_by_id(self.user_id)
            
            msg = MessageBox()
            msg.success_box("Cập nhật thông tin thành công!")
        except Exception as e:
            msg = MessageBox()
            msg.error_box(f"Không thể cập nhật thông tin: {str(e)}")

    def update_avatar(self):
        file,_ = QFileDialog.getOpenFileName(self,"Select Image","Image files(*.png*.jpg*.jpeg*.bmp)")
        if file:
            self.user['avatar']= file
            self.btn_avatar.setIcon(QIcon(file))
            self.lbl_avatar.setPixmap(QPixmap(file))
            update_user_avatar(self.user_id,file)

    def navMainScreen(self, index):
        self.main_widget.setCurrentIndex(index)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())