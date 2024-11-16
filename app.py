from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart-data')
def chart_data():
    # Dapatkan tipe grafik dari parameter query
    chart_type = request.args.get('type', 'line')  # Default: 'line'

    # Contoh data dinamis
    categories = ["January", "February", "March", "April", "May"]
    if chart_type == 'bar':
        series = [
            {"name": "Sales", "data": [random.randint(10, 100) for _ in range(5)]},
            {"name": "Revenue", "data": [random.randint(50, 150) for _ in range(5)]}
        ]
    elif chart_type == 'pie':
        series = [{
            "name": "Share",
            "colorByPoint": True,
            "data": [
                {"name": "Product A", "y": random.randint(10, 50)},
                {"name": "Product B", "y": random.randint(30, 70)},
                {"name": "Product C", "y": random.randint(20, 60)}
            ]
        }]
        categories = []  # Pie chart tidak membutuhkan kategori
    else:  # Default to line chart
        series = [
            {"name": "Dataset 1", "data": [random.randint(0, 100) for _ in range(5)]},
            {"name": "Dataset 2", "data": [random.randint(0, 100) for _ in range(5)]}
        ]

    # Kembalikan data sebagai JSON
    return jsonify({"categories": categories, "series": series, "type": chart_type})

if __name__ == '__main__':
    app.run(debug=True)
