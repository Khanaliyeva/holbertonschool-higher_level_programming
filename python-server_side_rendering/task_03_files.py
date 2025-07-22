import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        return data
    except Exception as e:
        return []

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
    except Exception as e:
        return []

@app.route('/products')
def display_products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    products = []
    error = None

    if source == "json":
        products = read_json("products.json")
    elif source == "csv":
        products = read_csv("products.csv")
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    # Filtrləmə (id varsa)
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if p["id"] == product_id]
            if not filtered:
                error = "Product not found"
                products = []
            else:
                products = filtered
        except ValueError:
            error = "Invalid ID format"
            products = []

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
