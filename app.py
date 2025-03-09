from flask import Flask, request, render_template, send_file
import pandas as pd
import os

app = Flask(__name__)
FILE_PATH = "fertilizer_data.xlsx"

def initialize_excel():
    if not os.path.exists(FILE_PATH):
        df = pd.DataFrame(columns=["Customer", "Date", "Fertilizer", "Quantity (kg)", "Cost (INR)"])
        df.to_excel(FILE_PATH, index=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_entry():
    try:
        customer = request.form.get('customer')
        date = request.form.get('date')
        fertilizer = request.form.get('fertilizer')
        quantity = float(request.form.get('quantity', 0))
        cost = float(request.form.get('cost', 0))

        if not (customer and date and fertilizer):
            return "Missing required fields", 400

        df = pd.read_excel(FILE_PATH, engine="openpyxl")

        new_entry = pd.DataFrame([[customer, date, fertilizer, quantity, cost]], columns=df.columns)
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_excel(FILE_PATH, index=False, engine="openpyxl")


        return "Entry added successfully!"
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/report')
def generate_report():
    return send_file(FILE_PATH, as_attachment=True)

if __name__ == '__main__':
    initialize_excel()
    app.run(debug=True)
