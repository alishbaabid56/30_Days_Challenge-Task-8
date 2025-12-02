
import streamlit as st

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2

def calculate(num1, num2, operation):
    if operation == "Add":
        return add(num1, num2)
    elif operation == "Subtract":
        return subtract(num1, num2)
    elif operation == "Multiply":
        return multiply(num1, num2)
    elif operation == "Divide":
        return divide(num1, num2)
    else:
        raise ValueError("Invalid operation selected.")

st.set_page_config(layout="centered", page_title="Simple Calculator")

st.title("Simple Streamlit Calculator")

# Centering the content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.header("Perform Operations")

    try:
        number1 = st.number_input("Enter first number:", value=0.0, format="%.2f", key="num1")
        number2 = st.number_input("Enter second number:", value=0.0, format="%.2f", key="num2")

        operation = st.radio(
            "Select an operation:",
            ("Add", "Subtract", "Multiply", "Divide"),
            key="operation",
            horizontal=True
        )

        if st.button("Calculate", key="calculate_button"):
            result = calculate(number1, number2, operation)
            st.success(f"Result: {result}")

    except ZeroDivisionError as e:
        st.error(f"Error: {e}")
    except ValueError as e:
        st.error(f"Invalid input: {e}. Please enter valid numbers.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
