def percentage_change(after_value, before_value):
    change = ((after_value-before_value)/before_value)*100
    return round(change, 2)