import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# JSON oxu
def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

# CSV oxu
def read_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return [
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                } for row in reader
            ]
    except Exception:
        return []

# SQLite oxu
def read_sqlite(db_path, product_id=None):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        return [
            {
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            } for row in rows
        ]
    except Exception:
        return None

# Ana route
@app.route("/products")
def show_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []
    error = None

    if source == "json":
        products = read_json("products.json")
    elif source == "csv":
        products = read_csv("products.csv")
    elif source == "sql":
        try:
            pid = int(product_id) if product_id else None
        except ValueError:
            return render_template("product_display.html", error="Invalid ID format")
        products = read_sqlite("products.db", pid)
        if products is None:
            error = "Database error"
    else:
        error = "Wrong source"

    if product_id and not products and not error:
        error = "Product not found"

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
