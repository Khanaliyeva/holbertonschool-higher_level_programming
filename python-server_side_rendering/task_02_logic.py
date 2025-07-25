import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get('items', [])
    except Exception as e:
        items_list = []
        print(f"Error reading JSON file: {e}")
    
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
