#!/usr/bin/env python
from PyQt5 import QtWidgets, QtGui, Qt

from .main_ui import Ui_MainWindow
from .add_dialog import PurchaseDialog, HelpDialog


class ShoppingList(QtWidgets.QMainWindow):
    '''Основной класс'''
    def __init__(self, parent=None, db=None):
        super().__init__()
        self.shopping = db
        self.initUI()
        self.ui.category.currentIndexChanged.connect(self.show_shops)
        self.ui.add_pushcase.clicked.connect(self.add_purchase)
        self.ui.del_purchase.clicked.connect(self.del_purchase)
        self.ui.action.triggered.connect(self.create_categry)
        self.ui.action_help.triggered.connect(self.get_help)

    def initUI(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.table_setup()
        self.get_category()
        self.show_shops()

    def table_setup(self):
        self.ui.tableShops.horizontalHeader().setSectionResizeMode(
                                                QtWidgets.QHeaderView.Fixed)
        self.ui.tableShops.setColumnWidth(0, 145)
        self.ui.tableShops.setColumnWidth(1, 150)
        self.ui.tableShops.setColumnWidth(2, 80)

    def get_category(self):
        '''вывести все категории'''
        self.ui.category.clear()
        category = {shop['category'] 
                        for shop in self.shopping.db.shopping.find()}
        category.add('Все')
        if category:
            self.ui.category.addItems(category)

    def show_shops(self):
        '''отобразить список'''
        # Очистка таблицы - не нашел как иначе
        self.ui.tableShops.setRowCount(0)
        # Создаем список согласно выбранной категории или Все
        category = self.ui.category.currentText()
        if category == 'Все':
            shops = self.shopping.db.shopping.find()
        else:
            shops = self.shopping.db.shopping.find({'category': category})
        row = 0
        for shop in shops:
            if shop['product'] != '' and shop['count'] != 0:
                self.ui.tableShops.insertRow(row)
                col = 0
                for key, vol in shop.items():
                    if key == '_id':
                        continue
                    item = QtWidgets.QTableWidgetItem()
                    self.ui.tableShops.setItem(row, col, item)
                    item = self.ui.tableShops.item(row, col)
                    item.setText('{}'.format(vol))
                    col += 1
                row += 1

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
        purchase = purchase_dialog.exec()
        if purchase == QtWidgets.QDialog.Accepted:
            self.show_shops()
    
    def del_purchase(self):
        '''Удалить покупку'''
        col = self.ui.tableShops.currentColumn()
        product = self.ui.tableShops.currentItem().text()
        if product and col == 1:
            self.shopping.db.shopping.delete_one({'product': product})
            self.show_shops()

    def get_help(self):
        help_dialog = HelpDialog()
        help_dialog.exec()
