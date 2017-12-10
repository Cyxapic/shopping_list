import sys

from PyQt5 import QtWidgets, Qt

from db.connector import ShoppingDB
from ui.gui import ShoppingList


app = QtWidgets.QApplication(sys.argv)
shopping_db = ShoppingDB()
shopping = ShoppingList(db=shopping_db)

if __name__ == '__main__':
    shopping.show()
    sys.exit(app.exec_())
