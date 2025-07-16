def bmi_calculator(weight, height):
    # Check for missing inputs
    if weight is None or height is None:
        return "Error: Please enter both weight and height."

    if height == 0:
        return "Error: Height cannot be zero."

    # Convert height to meters
    height_in_m = height / 100

    # Calculate BMI
    BMI = weight / (height_in_m ** 2)

    # Determine category
    if BMI < 18.5:
        category = "Underweight"
    elif BMI <= 24.9:
        category = "Normal Weight"
    elif BMI <= 29.9:
        category = "Over Weight"
    else:
        category = "Obese"

    return f'Body Mass Index: {BMI:.2f}, Category: {category}'
