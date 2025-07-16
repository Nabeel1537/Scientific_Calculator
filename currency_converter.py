def convert_currency(amount, from_currency, to_currency):

    rates = {
  "USD": {"PKR": 280, "EUR": 0.9},
  "PKR": {"USD": 1/280, "EUR": 0.0032},
  "EUR": {"USD": 1.1, "PKR": 300}
}
    if amount==None:
        return "Error: Enter your amount"
    elif from_currency == to_currency:
        return amount
    else:
       result =  amount*rates[from_currency][to_currency]

    return result