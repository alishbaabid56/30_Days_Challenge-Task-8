---
id: 5
title: Implement Streamlit Calculator
stage: green
date: 2025-12-02
surface: agent
model: claude-sonnet-4-5-20250929
feature: calculator
branch: 1-ai-k12-efficiency
user: unknown
command: "/sp.implement\nImplement the tasks and produce the full working Streamlit code.\n\nRequirements:\n- Provide a single runnable Python file named app.py\n- Use clean UI layout\n- Add error handling\n- Use streamlit widgets properly\n- Ensure the calculator supports +, -, ×, ÷\n\nFinal answer must include only code in a code block."
labels: ["implementation","streamlit","calculator"]
links:
  spec: specs/calculator/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - streamlit_calculator/app.py
tests:
  - Manual UI testing
---

## Prompt

```text
/sp.implement
Implement the tasks and produce the full working Streamlit code.

Requirements:
- Provide a single runnable Python file named app.py
- Use clean UI layout
- Add error handling
- Use streamlit widgets properly
- Ensure the calculator supports +, -, ×, ÷

Final answer must include only code in a code block.
```

## Response snapshot

```python
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
```

## Outcome

- ✅ Impact: Streamlit calculator application implemented successfully.
- 🧪 Tests: Manual UI testing is required to confirm full functionality and error handling.
- 📁 Files: Created `streamlit_calculator/app.py`.
- 🔁 Next prompts: Instructions on how to run the Streamlit app.
- 🧠 Reflection: The implementation adheres to the plan, including UI, core logic, and validation. The code is clean and uses Streamlit widgets appropriately.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
