from flask import Flask, render_template, request
import numpy as np
from bmi import bmi_calculator
from unit_converter import unit_converter
from currency_converter import convert_currency

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        operation = request.form.get("operation")

        
        
        
        # Get inputs safely for scientific operations
        num1_raw = request.form.get("num1")
        num2_raw = request.form.get("num2")
        angle_raw = request.form.get("angle")
        # converting the inputs in float if they are not empty
        num1 = float(num1_raw) if num1_raw else None
        num2 = float(num2_raw) if num2_raw else None
        angle = float(angle_raw) if angle_raw else None

        # Basic operations
        if operation == "add":
            if num1 is not None and num2 is not None:
             result = num1 + num2
            else:
             result = "Error: Please enter both numbers."

        elif operation == "subtract":
            if num1 is not None and num2 is not None:
                result = num1 - num2
            else:
                result = "Error: Please enter both numbers."

        elif operation == "multiply":
            if num1 is not None and num2 is not None:
                result = num1 * num2
            else:
                result = "Error: Please enter both numbers."

        elif operation == "divide":
            if num1 is not None and num2 is not None:
                result = "Error: Division by zero" if num2 == 0 else num1 / num2
            else:
                result = "Error: Please enter both numbers."

        elif operation == "power":
            if num1 is not None and num2 is not None:
                result = np.power(num1, num2)
            else:
                result = "Error: Please enter both numbers."
        elif operation == "sqrt":
            if num1 is not None:
                result = "Error: Negative number" if num1 < 0 else np.sqrt(num1)
            else:
                result = "Error: Please enter a number."

        # Trigonometry operations
        elif operation == "sin":
            result = np.sin(np.radians(angle))
            return render_template("index.html", angle_result=result)
        elif operation == "cos":
            result = np.cos(np.radians(angle))
            return render_template("index.html", angle_result=result)
        elif operation == "tan":
            result = np.tan(np.radians(angle))
            return render_template("index.html", angle_result=result)
        # Bmi calculator operations section
        height_raw = request.form.get("height")
        weight_raw = request.form.get("weight")

        height = float(height_raw) if height_raw else None
        weight = float(weight_raw) if weight_raw else None
        
        
        if operation == 'bmi':
            result= bmi_calculator(weight, height)
            return render_template("index.html", bmi_result=result)
        # Unit converter operation section

        value_raw = request.form.get("value")
        value = float(value_raw) if value_raw else None
        convertion_type = request.form.get("unit_conversion")
        if operation == 'convert_unit':
            result= unit_converter(value, convertion_type)
            return render_template("index.html", converter_result=result)
        
        # Currency Converter operation section
        amount_raw= request.form.get('amount')
        amount = float(amount_raw) if amount_raw else None
        from_currency = request.form.get('from_currency')
        to_currency = request.form.get('to_currency')
        if operation == "convert_currency":
            result= convert_currency(amount, from_currency, to_currency)
            return render_template("index.html", convert_amount=result)


    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
