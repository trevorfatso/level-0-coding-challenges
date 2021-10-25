#task7
def convert_celsius(celsius):
    fah = (celsius * (9/5)) + 32 
    return f'{fah:,.1f} °F.'

def convert_fahrenheit(fahrenheit):
    cels = (fahrenheit - 32) * (5/9)
    return f'{cels:,.1f} °C'