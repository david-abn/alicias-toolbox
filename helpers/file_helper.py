import time
import os
import sys

from helpers.logger_helper import get_logger

logger = get_logger(__name__)

def generate_filename(student) -> str:
    timestamp = time.strftime("%Y-%m-%d")
    filename = f"output_{student}_{timestamp}.txt"
    return filename

def get_lines():
    if getattr(sys, 'frozen', False):
        # Running as a standalone executable
        cwd = os.path.dirname(sys.executable)
    else:
        # Running as a script
        cwd = os.getcwd()
    
    template_file_path = os.path.join(cwd, 'template_text')
    with open(template_file_path, 'r') as file:
        lines = file.readlines()
        return lines

def write_template_file(template_content, student):
    filename = generate_filename(student)
    # script_dir = os.path.dirname(os.path.abspath(__file__))
    # relative_path = os.path.join(script_dir, "template_output")
    relative_path = "template_output"
    
    full_path = os.path.join(relative_path, filename)
    print(full_path)
    try:
        os.makedirs(relative_path, exist_ok=True)
        
        with open(full_path, 'w') as file:
            file.write(template_content)
        logger.info(f"Template file '{filename}' created successfully.")
    except IOError as e:
        logger.error(f"Error writing to file '{filename}': {e}")