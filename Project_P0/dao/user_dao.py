from config.database import get_connection
import hashlib


class UserDao:
    def get_user(self, username, password, email):
        conn = get_connection()
        cursor = conn.cursor()

        q = "INSERT INTO users(username,password,email) values(%s,%s,%s)"
        values = [username, password, email]
        cursor.execute(q, values)
        conn.commit()
        cursor.close()
        conn.close()

    def get_login_details(self, email):
        conn = get_connection()
        cursor = conn.cursor()
        q = "select * FROM users WHERE email=%s"
        cursor.execute(q, (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return user

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
