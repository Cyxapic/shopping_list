from PyQt5 import QtWidgets

from .purchase_ui import Ui_Dialog
from .help_ui import Ui_Help


class PurchaseDialog(QtWidgets.QDialog):
    '''добавляем покупки'''
    def __init__(self, parent=None, db=None):
        super().__init__(parent)
        self.shopping = db
        self.initUI()

    def initUI(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show_category()
        self.ui.addButton.clicked.connect(self.add_purchase)
        self.ui.cancelButton.clicked.connect(self.close)

    def show_category(self):
        self.ui.category.clear()
        self.category = {shop['category']
                         for shop in self.shopping.db.shopping.find()}
        if self.category:
            self.ui.category.addItems(self.category)
        else:
            alert = QtWidgets.QMessageBox()
            alert.detailedText('''Категорий не существует,
                                  пожалуйста сначала создайте категорию''')
            alert.exec()
            self.close()

    def add_purchase(self):
        '''Добавить покупку'''
        category = self.ui.category.currentText()
        product = self.ui.product_name.text()
        count = int(self.ui.count.text())
        SHOP = {
            'category': category,
            'product': product,
            'count': count
        }
        self.shopping.db.shopping.insert_one(SHOP)
        self.accept()


class HelpDialog(QtWidgets.QDialog):
    '''Помощь'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.ui = Ui_Help()
        self.ui.setupUi(self)