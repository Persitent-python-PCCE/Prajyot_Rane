from config.database import get_connection


class OrderDao:
    def create_order(self, u_id, total_amount):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO orders (u_id, total_amount)
            VALUES (%s, %s)
        """
        cursor.execute(query, (u_id, total_amount))
        order_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return order_id

    def add_order_item(self, order_id, p_id, quantity, price):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO order_items
            (order_id, p_id, quantity, price)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (order_id, p_id, quantity, price))
        conn.commit()
        cursor.close()
        conn.close()

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

    def get_order_history(self, u_id):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT
                o.order_id,
                o.order_date,
                o.total_amount,
                oi.p_id,
                p.p_name,
                oi.quantity,
                oi.price,
                (oi.quantity * oi.price) AS item_total
            FROM orders o
            JOIN order_items oi
                ON o.order_id = oi.order_id
            JOIN products p
                ON oi.p_id = p.p_id
            WHERE o.u_id = %s
            ORDER BY o.order_date DESC
        """
        cursor.execute(query, (u_id,))
        orders = cursor.fetchall()
        cursor.close()
        conn.close()
        return orders
