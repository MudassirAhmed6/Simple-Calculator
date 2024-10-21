import streamlit as st

# Title for the app
st.title("Simple Calculator")

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Input fields for numbers
num1 = st.number_input("Enter first number", value=0.0, step=0.1, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, step=0.1, format="%.2f")

# Select operation
operation = st.selectbox("Choose an operation", ("Add", "Subtract", "Multiply", "Divide"))

# Calculate when button is clicked
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
    st.write(f"Result: {result}")

