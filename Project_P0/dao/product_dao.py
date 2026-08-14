from config.database import get_connection
from config.database import mysql


class ProductsDao:

    def add_products(self, p_name, p_price, p_stock):
        conn = get_connection()
        curosr = conn.cursor()
        q = """
            INSERT INTO products(p_name,price,stock) VALUES(%s,%s,%s);
            """
        values = [p_name, p_price, p_stock]
        curosr.execute(q, values)
        conn.commit()
        curosr.close()
        conn.close()

    def get_all_products(self):
        conn = get_connection()
        curosr = conn.cursor()
        q = """
            SELECT p_id,p_name,price,stock from products;
            """
        curosr.execute(q)
        products = curosr.fetchall()
        conn.commit()
        curosr.close()
        conn.close()
        return products

    def update_products(self, p_id, p_name, price, stock):
        conn = get_connection()
        cursor = conn.cursor()
        q = """
            UPDATE products set p_name=%s,price=%s,stock=%s
            WHERE p_id=%s
            """
        cursor.execute(q, (p_name, price, stock, p_id))
        conn.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        conn.close()
        return affected_rows

    def get_product_by_id(self, p_id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = """
            SELECT p_id, p_name, price, stock
            FROM products
            WHERE p_id = %s
            """
            cursor.execute(query, (p_id,))
            product = cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Databse Error{e}")
            return None
        finally:
            cursor.close()
            connection.close()
            return product

    def delete_product(self, p_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            q = """
                DELETE FROM products where p_id=%s;
                """
            cursor.execute(q, (p_id,))
            rows_affected = cursor.rowcount
            conn.commit()
        except mysql.connector.Error as e:
            if conn:
                conn.rollback()
            print(f"Database Error:{e}")

        finally:
            cursor.close()
            conn.close()
            return rows_affected

    def reduce_stock(self, p_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE products
            SET stock = stock - %s
            WHERE p_id = %s
        """
        cursor.execute(query, (quantity, p_id))
        conn.commit()
        cursor.close()
        conn.close()
