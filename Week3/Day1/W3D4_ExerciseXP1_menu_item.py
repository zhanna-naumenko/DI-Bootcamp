import virtualenv
import psycopg2


conn = psycopg2.connect(database="PyCharm", user='postgres', password='jannetj0388', host='localhost', port='5432')
conn.autocommit = True
cursor = conn.cursor()


class MenuItem:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def save(self):
        '''insert the values in table'''
        query = "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)"
        val = (self.name, self.price)
        cursor.execute(query, val)
        conn.commit()


    def delete(self, value):
        '''deleted the values in table'''
        try:
            if value == self.name:
                query = "DELETE FROM Menu_Items WHERE item_name = %s"
                cursor.execute(query, (value,))
            elif value == self.price:
                query = "DELETE FROM Menu_Items WHERE item_price = %s"
                cursor.execute(query, (value,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def update(self, new_name, new_price):
        '''updates values in table'''
        try:
            if new_name and new_price:
                query = "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s"
                val = (new_name, new_price, self.name)
                cursor.execute(query, val)
            elif new_name == self.name:
                query = "UPDATE Menu_Items SET item_name = %s WHERE item_name = %s"
                val = (new_name, self.name)
                cursor.execute(query, val)
            elif new_price == self.price:
                query = "UPDATE Menu_Items SET item_price = %s WHERE item_name = %s"
                val = (new_price, self.name)
                cursor.execute(query, val)
            conn.commit()
        finally:
            cursor.close()
            conn.close()

if __name__ == '__main__':
    item = MenuItem('Burger', 35)
    item2 = MenuItem('Beef Stew', 75)
    item2.save()
    item3 = MenuItem('COFFEE', 15)
    item3.save()
    # item.delete('Burger')
    # item.update('Veggie Burger', 37)
