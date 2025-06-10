import pandas as pd
import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    sql = """
    SELECT l.line_item_id, l.quantity, l.product_id, p.product_name, p.price FROM line_items l JOIN products p ON l.product_id = p.product_id
    """
    df = pd.read_sql_query(sql, conn)
    print(df.head())

    df = df.groupby("product_id").agg({"line_item_id": "count", "total": "sum", "product_name": "first" })
    print(df.head())

    df = df.sort_values(by="product_name")
    print(df.head())

    df.to_csv("./order_sumary.csv")