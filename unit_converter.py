def unit_converter(value, convertion_type):

    # to check wether the input are empty
    if value is None :
        return "Error: Please enter your value."

     # temperature conversion
    
    if convertion_type == "c_to_f":
        C = value
        F = (C * 9/5) + 32
        value = F
    elif convertion_type == "f_to_c":
        F = value
        C = (F - 32) * 5/9
        value = C
    # distance converter

    if convertion_type == "km_to_miles":
        Km= value
        Miles = Km * 0.621371
        value = Miles
    elif convertion_type == "miles_to_km":
        Miles = value
        Km = Miles * 1.60934
        value = Km
    # Weight converter

    if convertion_type == "kg_to_lb":
        Kg = value
        Lb = Kg * 2.20462
        value = Lb
    elif convertion_type== "lb_to_kg":
        Lb= value
        Kg = Lb / 2.20462
        value = Kg
    
    return f'Your Convertion type: {convertion_type}, value: {value}'

