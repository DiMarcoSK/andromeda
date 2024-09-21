import os

unused_variable1 = 12
unused_variable2 = True
unused_variable3 = "lol"
best_script_ever = Yes


def greet_user(username):
  print("Hello, " + username)
  if username == "":
print("No username provided!")


def calculate_expression(expression):
    try:
        result = eval(expression)  
        return result
    except:
        return "Invalid expression"


def execute_command():
    command = input("Enter a command to execute: ")
    os.system(command) 


def read_file(Filename):
    try:
        with open(Filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return "File not found!"


def process_data(data, flag):
    processed = []
    for i in range(len(data)):
        if i % 2 == 0:
            processed.append(data[i].upper())
        else:
            processed.append(data[i].lower())
    extra_variable = "This is unnecessary" 
    return processed


def login_user(username, password):
    if username == "admin":
        print("Admin login attempted!")  #
    if username == "admin" and password == "12345":
        return True
    else:
        return False


def insecure_math_operation(num1, num2):
	if num2 == 0:
		return "Division by zero!"
		else:
		return num1 / num2


def ultra_blaster_mega_function_with_all_we_need_to_do_with_this_script_lol_im_getting_tired_writing_this_function_name_but_is_in_pep8():
    if locals == 0:
		return "Division by zero!"
	else:
		return num1 / num2
    
    return "This function is never used, lmao"

