# 30_DAYS_CHALLENGE_TASK-8

# /sp.constitution
You are an expert Streamlit + Python app engineer.  
Your job is to write clean, simple, beginner-friendly code.  
You must follow my specifications strictly.  
You must avoid unnecessary complexity.  
Always explain decisions clearly and produce production-ready code.


# OUTPUT
● The project constitution has been updated with your guidelines.

  Here's a summary of the key principles:
  - Role: Expert Streamlit + Python app engineer.
  - Goal: Write clean, simple, beginner-friendly code.
  - Constraints: Follow specifications strictly, avoid unnecessary complexity.    
  - Output: Explain decisions clearly and produce production-ready code.

  This update ensures all dependent templates will stay in sync with these new    
   principles.



# /sp.specify
We want to build a simple Streamlit Calculator app.

Features required:
- User will input two numbers.
- User will select an operation from: Add, Subtract, Multiply, Divide.
- When the user clicks a button, the result should appear.
- Layout must be clean and centered.
- Validation:
  - Prevent dividing by zero.
  - Show friendly error if user enters invalid input.
- Code must be simple and easy to understand.

Tech stack:
- Python
- Streamlit

Output expected:
- Clear specification doc.
- Streamlit app structure.


# OUTPUT 
● I have created the specification document for the Streamlit Calculator app.     
  You can find it at specs/calculator/spec.md.

  Here's a summary of the specification:

  Streamlit Calculator App Specification

  Features:
  - User will input two numbers.
  - User will select an operation: Add, Subtract, Multiply, Divide.
  - A button click will display the result.
  - Layout will be clean and centered.

  Validation:
  - Prevent division by zero with a friendly error.
  - Show friendly error for invalid input.

  Tech Stack:
  - Python
  - Streamlit

  Code Quality:
  - Simple, clean, beginner-friendly code.
  - Clear explanations, production-ready.

  Application Structure:
  - streamlit_calculator/app.py
  - streamlit_calculator/README.md (optional)

  I have also recorded this interaction as a Prompt History Record at history/    
  prompts/calculator/2-create-streamlit-calculator-spec.spec.prompt.md.

  Would you like me to proceed with planning the implementation of this
  Streamlit Calculator app?



# /sp.plan
Create a clear step-by-step plan for building the Streamlit Calculator app.

The plan must include:
- Project structure
- Required Python functions
- UI layout plan
- Input validation plan
- Testing approach
- Final integration steps

Keep plan short but complete.


# OUTPUT 
● I have created a clear, step-by-step plan for building the Streamlit
  Calculator app. You can find the plan at specs/calculator/plan.md.

  Summary of the plan:

  - Project Structure: app.py for the main logic.
  - Python Functions: add, subtract, multiply, divide, and a calculate
  dispatcher.
  - UI Layout: Centered layout using st.container(), st.number_input(),
  st.radio()/st.selectbox(), st.button(), and st.write()/st.error() for
  results and messages.
  - Input Validation: try-except for numeric input, and explicit check for        
  division by zero.
  - Testing Approach: Unit tests for arithmetic functions using pytest, and       
  manual UI testing.
  - Final Integration Steps: Develop app.py, run unit tests, perform manual       
  acceptance testing, refine, and optionally update README.md.

  I have also recorded this planning session as a Prompt History Record at his    
  tory/prompts/calculator/3-create-streamlit-calculator-plan.plan.prompt.md.      

  Would you like me to proceed with generating the actionable,
  dependency-ordered tasks based on this plan?



# /sp.tasks
Convert the plan into small actionable tasks.

Tasks should include:
- Setting up Streamlit environment
- Creating UI components
- Writing calculator logic
- Adding validation
- Testing functionality
- Running the final app

Output must be a task list.



# OUTPUT 
● Read(specs\calculator\plan.md)
  ⎿  Read 53 lines

# /sp.implement
Implement the tasks and produce the full working Streamlit code.

Requirements:
- Provide a single runnable Python file named app.py
- Use clean UI layout
- Add error handling
- Use streamlit widgets properly
- Ensure the calculator supports +, -, ×, ÷

Final answer must include only code in a code block.


# OUTPUT
● Bash(mkdir streamlit_calculator)
  ⎿  (No content)

● Write(streamlit_calculator\app.py)
  ⎿  Wrote 1 lines to streamlit_calculator\app.py
     import streamlit as st
     def add(num1, num2):
         return num1 + num2
     def subtract(num1, num2):
         return num1 - num2
     def multiply(num1, num2):

● Read(.specify\templates\phr-template.prompt.md)
  ⎿  Read 46 lines

● Write(history\prompts\calculator\5-implement-streamlit-calculator.green.prompt.m       d)
  ⎿  Wrote 1 lines to history\prompts\calculator\5-implement-streamlit-calcul     
     tor.green.prompt.md
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

● import streamlit as st

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
          number1 = st.number_input("Enter first number:", value=0.0,
  format="%.2f", key="num1")
          number2 = st.number_input("Enter second number:", value=0.0,
  format="%.2f", key="num2")

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

  I have created the streamlit_calculator/app.py file with the full working       
  Streamlit code for the calculator app.

