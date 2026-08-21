from models.cart import Cart
from config.database import get_connection


class cartDao:

    def add_to_cart(self, u_id, p_id, quantity):
        conn = get_connection()
        cursor = conn.cursor()
        q = """
        INSERT INTO cart(u_id,p_id,quantity) values(%s,%s,%s);
            """
        cursor.execute(q, (u_id, p_id, quantity))
        conn.commit()
        cursor.close()
        conn.close()

    def get_cart(self, u_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT c.c_id,
                c.p_id,
                p.p_name,
                p.price,
                c.quantity,
                (p.price * c.quantity) AS total
            FROM cart c
            JOIN products p ON c.p_id = p.p_id
            WHERE c.u_id = %s
        """
        cursor.execute(query, (u_id,))
        cart_items = cursor.fetchall()
        cursor.close()
        conn.close()
        return cart_items

    def clear_cart(self, u_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            DELETE FROM cart
            WHERE u_id = %s
        """
        cursor.execute(query, (u_id,))
        conn.commit()
        cursor.close()
        conn.close()

    def remove_product_from_cart(self, p_id):
        conn = get_connection()
        cursor = conn.cursor()
        q = """
        DELETE FROM cart where p_id=%s;
            """
        cursor.execute(q, (p_id,))
        conn.commit()
        cursor.close()
        conn.close()
