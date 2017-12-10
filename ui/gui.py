#!/usr/bin/env python
import re
from string import Template

from PyQt5 import QtWidgets, QtGui, Qt

from .main_ui import Ui_MainWindow
from .add_dialog import PurchaseDialog


class ShoppingList(QtWidgets.QMainWindow):
    '''Основной класс'''
    def __init__(self, parent=None, db=None):
        super().__init__()
        self.shopping = db
        self.initUI()
        self.ui.category.currentIndexChanged.connect(self.show_shops)
        self.ui.action.triggered.connect(self.create_categry)
        self.ui.add_pushcase.clicked.connect(self.add_purchase)
        self.ui.del_purchase.clicked.connect(self.del_purchase)

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.get_category()
        self.show_shops()

    def get_category(self):
        '''вывести все категории'''
        self.ui.category.clear()
        category = {shop['category'] for shop in self.shopping.db.shopping.find()}
        category.add('Все')
        if category:
            self.ui.category.addItems(category)

    def show_shops(self):
        self.ui.listWidget.clear()
        s = "Категория: $category;   Продукт: $product;   Количество: $count"
        template = Template(s)
        category = self.ui.category.currentText()
        if category == 'Все':
            shops = self.shopping.db.shopping.find()
        else:
            shops = self.shopping.db.shopping.find({'category': category})
        for shop in shops:
            if shop['product'] != '' and shop['count'] != 0:
                self.ui.listWidget.addItem(template.substitute(shop))

    def create_categry(self):
        '''добавить категорию'''
        category, ok = QtWidgets.QInputDialog.getText(self, 'Новая категория',
                                                      'Название категории:')
        if ok:
            self.shopping.new_category(category)
            self.get_category()

    def add_purchase(self):
        '''Диалог - добавлние покупки'''
        purchase_dialog = PurchaseDialog(parent=self, db=self.shopping)
        purchase_dialog.exec()
        if purchase_dialog == QtWidgets.QDialog.Accepted:
            self.show_shops()
    
    def del_purchase(self):
        '''Удалить покупку'''
        item = self.ui.listWidget.currentIndex().data()
        if item:
            pattern = r'(Продукт:) ((\w+.){1,10})'
            product = re.search(pattern, item).group(2).rstrip(';')
            self.shopping.db.shopping.delete_one({'product': product})
            self.show_shops()
