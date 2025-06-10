import sqlite3

try:
    with sqlite3.connect("../db/lesson.db") as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor
    
    Q1 = """
    SELECT o.order_id, SUM(p.price*l.quantity) FROM orders o
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON p.product_id = l.product_id
    GROUP BY o.order_id
    ORDER BY order_id LIMIT 5;
    """
    cursor.execute(Q1)
    result = cursor.fetchall()
    for row in result:
        print(row)

    Q2 = """
    SELECT o.order_id, l.line_item_id, p.product_name
    FROM orders o JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON p.product_id = l.product_id
    WHERE o.order_id IN (SELECT order_id FROM orders ORDER BY order_id LIMIT 5);
    """
    cursor.execute(Q2)
    result = cursor.fetchall()
    for row in result:
        print(row)

    Q2 = """
    SELECT customers.customer_name, AVG(order_totals.total_price) AS average_total_price
    FROM customers LEFT JOIN
    (SELECT orders.customer_id AS customer_id_b, SUM(products.price * line_items.quantity) AS total_price)
    FROM orders JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON line_items.product_id = products.product_id GROUP BY orders.orders_id
    ) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
    GROUP BY customers.customer_id;
    """
    cursor.execute(Q2)
    result = cursor.fetchall()
    for row in result:
        print(row)

    Q3 = """
    SELECT customer_id FROM customers WHERE customer_name = 'Perez' AND customer_name = 'Sons'
    """
    cursor.execute(Q3)
    result = cursor.fetchone()
    customer_id = result[0]

    Q3 = """
    SELECT product_id FROM products ORDER BY price DESC LIMIT 5
    """
    cursor.execute(Q3)
    result = cursor.fetchall()
    product_result = result

    Q3 = """
    SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'
    """
    cursor.execute(Q3)
    result = cursor.fetchone()
    employee_id = result[0]

    Q3 = """
    INSERT INTO orders (customer_id, employee_id, date) VALUES (?, ?, DATETIME('now)) RETURNING order_id
    """
    cursor.execute(Q3, (customer_id, employee_id))
    result = cursor.fetchone()
    order_id = result[0]
    for i in range(5):
        Q3 = """
            INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)
            """
        cursor.execute(Q3)
        conn.commit
        Q3 = """
            SELECT l.line_item_id, l.quantity, p.product_name FROM line_items l JOIN products p ON l.product_id = p.product_id WHERE l.order_id = ?;
            """
        cursor.execute(Q3, (order_id))
        result = cursor.fetchall()
        for row in result:
            print(row)

    Q4 = """
        SELECT first_name, last_name, COUNT(order_id) FROM employees e JOIN orders o
        ON e.employee_id = o.employee_id
        GROUP BY e.employee_id
        HAVING COUNT(order_id) > 5;
        """
    cursor.execute(Q4)
    result = cursor.fetchall()
    for row in result:
        print(row)

except sqlite3.Error as e:
    print(f"An error occured: {e}")