import psycopg2


conn = psycopg2.connect(database="PyCharm", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()

class MenuManager:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price


    def get_by_name(self):
        try:
            cursor.execute("SELECT item_name FROM Menu_Items WHERE item_name = %s", (self.name,))
            item = cursor.fetchone()
            if item:
                return ''.join(item)
            else:
                return None
        finally:
            cursor.close()
            conn.close()

    @classmethod
    def all_items(self):
        try:
            cursor.execute("SELECT item_name FROM Menu_Items")
            items = cursor.fetchall()
            return items
        finally:
            cursor.close()
            conn.close()


item2 = MenuManager('Veggie Burger')
print(item2.get_by_name())
items = MenuManager.all_items()
print(items)