from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        operation = request.form.get("operation")

        
        
        
        # Get inputs safely
        num1_raw = request.form.get("num1")
        num2_raw = request.form.get("num2")
        angle_raw = request.form.get("angle")

        num1 = float(num1_raw) if num1_raw else None
        num2 = float(num2_raw) if num2_raw else None
        angle = float(angle_raw) if angle_raw else None


        if num1: num1 = float(num1)
        if num2: num2 = float(num2)
        if angle: angle = float(angle)

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

        # Trigonometry operations
        elif operation == "sin":
            result = np.sin(np.radians(angle))
        elif operation == "cos":
            result = np.cos(np.radians(angle))
        elif operation == "tan":
            result = np.tan(np.radians(angle))

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
