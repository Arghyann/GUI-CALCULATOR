import requests
from tkinter import *
from tkinter import ttk

previous_result = None
prev_answers = []
memory = None
value=None

#CURRENCY CONVERSION
def convert_currency(amount, from_currency, to_currency):
    # Exchange rates (INR=>USD)
    exchange_rates = {
        'AUD': 0.019,
        'USD': 0.012,
        'EUR': 0.011,
        'INR':  1,
        'BTC': 0.000000187,
        'CAD': 0.016,
        'HUF':  4.40,
        'ETH': 0.0000036,
        'JPY': 1.83,
        'CNY': 0.086,
        'GBP': 0.0095}
    
    try:
        # If currencies are the same, no conversion needed
        if from_currency == to_currency:
            return amount
        
        if(from_currency in exchange_rates and to_currency in exchange_rates):
            exchange_rate=exchange_rates[to_currency]/exchange_rates[from_currency]
            return amount*exchange_rate
        else:
            print(f"Error: Conversion not supported for {from_currency} to {to_currency}")
            return None
    except Exception as e:
        print(f"Error during currency conversion: {e}")
        return None

# Function to open the currency converter window
def open_currency_converter():
    converter_window = Toplevel(window)
    converter_window.title("Currency Converter")

    amount_label = Label(converter_window, text="Amount:",)
    amount_label.grid(row=0, column=0, padx=10, pady=10)

    amount_entry = Entry(converter_window, font=('Helvetica', 16))
    amount_entry.grid(row=0, column=1, padx=10, pady=10)

    from_currency_label = Label(converter_window, text="From Currency:")
    from_currency_label.grid(row=1, column=0, padx=10, pady=10)

    from_currency_var = StringVar()
    from_currency_var.set("INR")  # Default currency is USD

    from_currency_options = ["USD", "EUR", 'INR','AUD','BTC','CAD','HUF','ETH','JPY','CNY','GBP']  # Add more currencies as needed
    from_currency_menu = OptionMenu(converter_window, from_currency_var, *from_currency_options)
    from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

    to_currency_label = Label(converter_window, text="To Currency:")
    to_currency_label.grid(row=2, column=0, padx=10, pady=10)

    to_currency_var = StringVar()
    to_currency_var.set("USD")  # Default currency is USD

    to_currency_options = ["USD", "EUR", 'INR','AUD','BTC','CAD','HUF','ETH','JPY','CNY','GBP']  # Add more currencies as needed
    to_currency_menu = OptionMenu(converter_window, to_currency_var, *to_currency_options)
    to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

    result_label = Label(converter_window, text="")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = Button(converter_window, text="Convert", padx=20, pady=20, font=('Helvetica', 16),
                            command=lambda: perform_conversion(amount_entry.get(), from_currency_var.get(), to_currency_var.get(), result_label))
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform the currency conversion and display the result
def perform_conversion(amount_str, from_currency, to_currency, result_label):
    try:
        amount = float(amount_str)
        converted_amount = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            result_label.config(text=f"Result: {amount} {from_currency} = {converted_amount:.2f} {to_currency}")
            save_to_file(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Error: Please enter a valid number for the amount.")

#TEMPRATURE CONVERSION
def convert_temperature(temperature, from_unit, to_unit):
    try:
        if from_unit == to_unit:
            return temperature
        
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            converted_temperature = (temperature * 9/5) + 32
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            converted_temperature = (temperature - 32) * 5/9
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            converted_temperature = temperature + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            converted_temperature = temperature - 273.15
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            converted_temperature = (temperature + 459.67) * 5/9
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            converted_temperature = temperature * 9/5 - 459.67
        else:
            print(f"Error: Conversion not supported for {from_unit} to {to_unit}")
            return None
        
        return converted_temperature
    except Exception as e:
        print(f"Error during temperature conversion: {e}")
        return None

def open_temperature_converter():
    temp_converter_window = Toplevel(window)
    temp_converter_window.title("Temperature Converter")

    temperature_label = Label(temp_converter_window, text="Temperature:")
    temperature_label.grid(row=0, column=0, padx=10, pady=10)

    temperature_entry = Entry(temp_converter_window, font=('Helvetica', 16))
    temperature_entry.grid(row=0, column=1, padx=10, pady=10)

    from_unit_label = Label(temp_converter_window, text="From Unit:")
    from_unit_label.grid(row=1, column=0, padx=10, pady=10)

    from_unit_var = StringVar()
    from_unit_var.set("Celsius")

    from_unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit_menu = OptionMenu(temp_converter_window, from_unit_var, *from_unit_options)
    from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

    to_unit_label = Label(temp_converter_window, text="To Unit:")
    to_unit_label.grid(row=2, column=0, padx=10, pady=10)

    to_unit_var = StringVar()
    to_unit_var.set("Fahrenheit")

    to_unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
    to_unit_menu = OptionMenu(temp_converter_window, to_unit_var, *to_unit_options)
    to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

    result_label = Label(temp_converter_window, text="")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = Button(temp_converter_window, text="Convert", padx=20, pady=20, font=('Helvetica', 16),
                            command=lambda: perform_temperature_conversion(temperature_entry.get(), from_unit_var.get(), to_unit_var.get(), result_label))
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform the temperature conversion and display the result
def perform_temperature_conversion(temperature_str, from_unit, to_unit, result_label):
    try:
        temperature = float(temperature_str)
        converted_temperature = convert_temperature(temperature, from_unit, to_unit)

        if converted_temperature is not None:
            result_str = f"Result: {temperature} {from_unit} = {converted_temperature:.2f} {to_unit}"
            result_label.config(text=result_str)
            save_to_file(result_str)  # Save the result to calculator history
    except ValueError:
        result_label.config(text="Error: Please enter a valid number for the temperature.")

def open_distance_converter():
    converter_window = Toplevel(window)
    converter_window.title("Distance Converter")

    value_label = Label(converter_window, text="Value:")
    value_label.grid(row=0, column=0, padx=10, pady=10)

    value_entry = Entry(converter_window, font=('Helvetica', 16))
    value_entry.grid(row=0, column=1, padx=10, pady=10)

    from_unit_label = Label(converter_window, text="From Unit:")
    from_unit_label.grid(row=1, column=0, padx=10, pady=10)

    from_unit_var = StringVar()
    from_unit_var.set("Meter")

    from_unit_options = ["Meter", "Kilometer", "Mile"]
    from_unit_menu = OptionMenu(converter_window, from_unit_var, *from_unit_options)
    from_unit_menu.grid(row=1, column=1, padx=10, pady=10)

    to_unit_label = Label(converter_window, text="To Unit:")
    to_unit_label.grid(row=2, column=0, padx=10, pady=10)

    to_unit_var = StringVar()
    to_unit_var.set("Meter")

    to_unit_options = ["Meter", "Kilometer", "Mile"]
    to_unit_menu = OptionMenu(converter_window, to_unit_var, *to_unit_options)
    to_unit_menu.grid(row=2, column=1, padx=10, pady=10)

    result_label = Label(converter_window, text="")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    convert_button = Button(converter_window, text="Convert", padx=20, pady=20, font=('Helvetica', 16),
                            command=lambda: perform_distance_conversion(value_entry.get(), from_unit_var.get(), to_unit_var.get(), result_label))
    convert_button.grid(row=4, column=0, columnspan=2, pady=10)

# Function to perform the distance conversion and display the result
def perform_distance_conversion(value_str, from_unit, to_unit, result_label):
    try:
        value = float(value_str)
        converted_value = convert_distance(value, from_unit, to_unit)

        if converted_value is not None:
            result_str = f"Result: {value} {from_unit} = {converted_value:.2f} {to_unit}"
            result_label.config(text=result_str)
            save_to_file(result_str)  # Save the result to calculator history
    except ValueError:
        result_label.config(text="Error: Please enter a valid number for the distance.")

def convert_distance(value, from_unit, to_unit):
    # Define conversion factors for each unit
    conversion_factors = {
        'Meter': {
            'Meter': 1,
            'Kilometer': 0.001,
            'Mile': 0.000621371,
        },
        'Kilometer': {
            'Meter': 1000,
            'Kilometer': 1,
            'Mile': 0.621371,
        },
        'Mile': {
            'Meter': 1609.34,
            'Kilometer': 1.60934,
            'Mile': 1,
        },
    }
    
    try:
        # Convert value from 'from_unit' to 'to_unit'
        converted_value = value * conversion_factors[from_unit][to_unit]
        return converted_value
    except KeyError:
        print(f"Error: Conversion not supported for {from_unit} to {to_unit}")
        return None
    except Exception as e:
        print(f"Error during distance conversion: {e}")
        return None

def calculate_compound_interest(principal, rate, time, compound_frequency):
    try:
        # Convert rate from percentage to decimal
        rate /= 100

        # Calculate compound interest
        amount = principal * ((1 + rate / compound_frequency) ** (compound_frequency * time))
        interest = amount - principal

        return amount, interest
    except Exception as e:
        print(f"Error during compound interest calculation: {e}")
        return None, None

def open_compound_interest_calculator():
    ci_window = Toplevel(window)
    ci_window.title("Compound Interest Calculator")

    principal_label = Label(ci_window, text="Principal:")
    principal_label.grid(row=0, column=0, padx=10, pady=10)

    principal_entry = Entry(ci_window, font=('Helvetica', 16))
    principal_entry.grid(row=0, column=1, padx=10, pady=10)

    rate_label = Label(ci_window, text="Rate (%):")
    rate_label.grid(row=1, column=0, padx=10, pady=10)

    rate_entry = Entry(ci_window, font=('Helvetica', 16))
    rate_entry.grid(row=1, column=1, padx=10, pady=10)

    time_label = Label(ci_window, text="Time (years):")
    time_label.grid(row=2, column=0, padx=10, pady=10)

    time_entry = Entry(ci_window, font=('Helvetica', 16))
    time_entry.grid(row=2, column=1, padx=10, pady=10)
    compound_frequency_label = Label(ci_window, text="Compound Frequency:")
    compound_frequency_label.grid(row=3, column=0, padx=10, pady=10)

    compound_frequency_var = StringVar()
    compound_frequency_var.set("1")  # Default compound frequency is annually
    compound_frequency_options = ["1 (Annually)", "2 (Semi-Annually)", "4 (Quarterly)", "12 (Monthly)"]
    compound_frequency_menu = OptionMenu(ci_window, compound_frequency_var, *compound_frequency_options)
    compound_frequency_menu.grid(row=3, column=1, padx=10, pady=10)

    result_label = Label(ci_window, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    calculate_button = Button(ci_window, text="Calculate", padx=20, pady=20, font=('Helvetica', 16),
                              command=lambda: perform_compound_interest_calculation(principal_entry.get(), rate_entry.get(), time_entry.get(), compound_frequency_var.get(), result_label))
    calculate_button.grid(row=5, column=0, columnspan=2, pady=10)

def perform_compound_interest_calculation(principal_str, rate_str, time_str, compound_frequency_str, result_label):
    try:
        principal = float(principal_str)
        rate = float(rate_str)
        time = float(time_str)
        compound_frequency = int(compound_frequency_str.split()[0])  # Extract the numerical part of the compound frequency

        amount, interest = calculate_compound_interest(principal, rate, time, compound_frequency)

        if amount is not None and interest is not None:
            result_str = f"Total Amount: {amount:.2f}\nInterest Earned: {interest:.2f}"
            result_label.config(text=result_str)
            save_to_file(result_str)  # Save the result to calculator history
    except ValueError:
        result_label.config(text="Error: Please enter valid numbers for the inputs.")
def const_window():
    global const_window
    const_window = Toplevel(window)
    const_window.title("Scientific constants")

    # Create a Treeview widget for the table
    table = ttk.Treeview(const_window, columns=('const', 'value', 'unit'))
    table.heading("#0", text="ID")
    table.heading("const", text="Constant")
    table.heading("value", text="Value")
    table.heading("unit", text="Unit")

    constants_data = [
        (0, "Speed of Light", "299792458", "m/s"),  # Index 0
        (1, "Gravitational Constant", "0.0000000000667408", "m^3 kg^-1 s^-2"),  # Index 1
        (2, "Planck's Constant", "0.000000000000000000000000000000662607015", "m^2 kg / s"),  # Index 2
        (3, "Avogadro's Number", "602214076", "mol^-1"),  # Index 3
        (4, "Boltzmann Constant", "0.000000000000000000000013806", "m^2 kg s^-2 K^-1"),  # Index 4
        (5, "Electric Constant", "0.000000000008854187817", "F m^-1"),  # Index 5
        (6, "Elementary Charge", "0.0000000000000000001602176634", "C"),  # Index 6
        (7, "Faraday Constant", "96485.33212", "C mol^-1"),  # Index 7
        (8, "Fine-Structure Constant", "0.0072973525693", ""),  # Index 8
        (9, "Gas Constant", "8.314462618", "J mol^-1 K^-1"),  # Index 9
    ]

    for constant in constants_data:
        table.insert("", "end", text=str(constant[0]), values=(constant[1], constant[2], constant[3]))

    table.pack(expand=True, fill="both")
    index_label = Label(const_window, text="Enter Index:")
    index_entry = Entry(const_window)
    index_button = Button(const_window, text="OK", command=lambda: store_index(index_entry.get(),constants_data))

    index_label.pack(pady=5)
    index_entry.pack(pady=5)
    index_button.pack(pady=10)

    def store_index(index,constdata):
        global value,expression
        value=constdata[int(index)][2]
        expression=expression+str(value)
        result_var.set(expression)
        const_window.destroy()

#MAIN WINDOW
window = Tk()

result_var = StringVar()
result_var.set('0')
expression = ''

#window.geometry('300x400')
window.configure(bg='#1e1e1e')
window.title('CALCULATOR')
icon = PhotoImage(file='D:\python project\GUI-CALCULATOR\calc.png')
window.iconphoto(True, icon)

entry = Entry(window, font=('Helvetica', 16), textvariable=result_var, bd=10)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

def create_button(text, row, col):
    # Change color for '=' button
    if text == '=':
        button = Button(window, text=text, padx=20, pady=20, font=('Helvetica', 16),
                        command=lambda t=text: button_click(t), fg='white', bg='#F28C28',
                        activebackground='#FF5733', activeforeground='white')
    elif text == 'C':
        button = Button(window, text=text, padx=20, pady=20, font=('Helvetica', 16),
                        command=lambda t=text: button_click(t), fg='white', bg='#FFBF00',
                        activebackground='#FF5733', activeforeground='white')    
    else:
        button = Button(window, text=text, padx=20, pady=20, font=('Helvetica', 16),
                        command=lambda t=text: button_click(t), fg='white', bg='#5A5A5A',
                        activebackground='white', activeforeground='#5A5A5A')
    button.grid(row=row, column=col)

# Create buttons based on the buttons list
for (text, row, col) in buttons:
    create_button(text, row, col)


ans_button = Button(window, text="ANS", padx=40, pady=20, font=('Helvetica', 16),
                    command=lambda: button_click('ANS'), fg='white', bg='#5A5A5A',
                    activebackground='white', activeforeground='#5A5A5A')
ans_button.grid(row=5, column=0, columnspan=2)  # Set columnspan to 2 for 'ANS' button

del_button = Button(window, text="DEL", padx=40, pady=20, font=('Helvetica', 16),
                    command=lambda: button_click('DEL'), fg='white', bg='#5A5A5A',
                    activebackground='white', activeforeground='#5A5A5A')
del_button.grid(row=5, column=2, columnspan=2)  # Set columnspan to 2 for 'DEL' button


def button_click(text):
    global expression, previous_result
    
    if text == '=':
        try:
            result = str(eval(expression))
            result_var.set(result)
            save_to_file(result)
            previous_result = result  # Store the current result as previous result
            expression = ""
        except Exception as e:
            result_var.set("Error")

    elif text == 'C':
        expression = ""
        result_var.set("0")

    elif text == 'ANS':
        if previous_result is not None:
            expression += str(previous_result)
            result_var.set(expression)

    elif text == 'DEL':
        delete_last_character()

    else:
        expression += text
        result_var.set(expression)

# Function to delete the last character from the expression
def delete_last_character():
    global expression
    if expression:
        expression = expression[:-1]
        result_var.set(expression)

def save_to_file(result):
    global expression
    if expression == 'ANS':  # Check if the expression is 'ANS'
        expression = previous_result  # Set the expression to the previous result
    with open('calculator_history.txt', 'a') as file:
        file.write(f"{expression} = {result}\n")

prev_answers = []

def memory_store():
    global prev_answers
    try:
        value = entry.get()
        memory = float(value)
        prev_answers.append(memory)
    except ValueError:
        pass

def memory_recall():
        global prev_answers
        if len(prev_answers) > 0:
            answer_index = min(len(prev_answers), 1)  # To avoid negative index
            entry.delete(0, END)
            entry.insert(END, str(prev_answers[-answer_index]))
            prev_answers = prev_answers[:-1]
    
currency_converter_button = Button(window, text="CC", padx=12, pady=20, 
                                   font=('Helvetica', 16), command=open_currency_converter,
                                   fg = 'white', bg = '#5A5A5A', activebackground='white', activeforeground= '#5A5A5A')
currency_converter_button.grid(row=6, column=0, )

temperature_converter_button = Button(window, text="TC", padx=12, pady=20,
                                      font=('Helvetica', 16), command=open_temperature_converter,
                                      fg='white', bg='#5A5A5A', activebackground='white', activeforeground='#5A5A5A')
temperature_converter_button.grid(row=6, column=1, )

distance_converter_button = Button(window, text="DC", padx=12, pady=20,
                                      font=('Helvetica', 16), command=open_distance_converter,
                                      fg='white', bg='#5A5A5A', activebackground='white', activeforeground='#5A5A5A')
distance_converter_button.grid(row=6, column=2, )

compound_interest_button = Button(window, text="CI", padx=12, pady=20,
                                  font=('Helvetica', 16), command=open_compound_interest_calculator,
                                  fg='white', bg='#5A5A5A', activebackground='white', activeforeground='#5A5A5A')
compound_interest_button.grid(row=6, column=3, )
memory_store_button = Button(window, text="MS", padx=10, pady=20,
                    font=('Helvetica', 16), command=memory_store,fg='white', bg='#5A5A5A', 
                    activebackground='white', activeforeground='#5A5A5A')
memory_store_button.grid(row = 8, column = 0)

memory_recall_button = Button(window, text="MR", padx=10, pady=20,
                    font=('Helvetica', 16), command=memory_recall,fg='white', bg='#5A5A5A', 
                    activebackground='white', activeforeground='#5A5A5A')
memory_recall_button.grid(row = 8, column = 1)
constant_button = Button(window, text="const", padx=32, pady=20,
                    font=('Helvetica', 16), command=const_window,fg='white', bg='#5A5A5A', 
                    activebackground='white', activeforeground='#5A5A5A')
constant_button.grid(row = 8, column = 2,columnspan=2)

window.mainloop()
