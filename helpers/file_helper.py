import time
import os
import sys

import click

from helpers.logger_helper import get_logger

logger = get_logger(__name__)

def generate_filename(student) -> str:
    timestamp = time.strftime("%Y-%m-%d")
    filename = f"output_{student}_{timestamp}.txt"
    return filename

def get_cwd():
    if getattr(sys, 'frozen', False):
        # Running as a standalone executable
        cwd = os.path.dirname(sys.executable)
    else:
        # Running as a script
        cwd = os.getcwd()
    return cwd


def get_lines():
    cwd = get_cwd()
    template_file_name = 'template_text'
    
    template_file_path = os.path.join(cwd, template_file_name)
    template_file_path_with_txt = os.path.join(cwd, f"{template_file_name}.txt")
    
    def open_template_file(path):
        try: 
            with open(path, 'r') as file:
                lines = file.readlines()
                return lines
        except FileNotFoundError:
            return None
    
    template_contents = open_template_file(template_file_path)
    if template_contents is None:
        template_contents = open_template_file(template_file_path_with_txt)
    
    if template_contents:
        return template_contents
    else:
        logger.error("Unable to open template contents file.")
        click.pause("Failed to run script. Please check the template_text file is in the same folder as alicias-toolbox app and try again...")
        raise FileNotFoundError
    
def write_template_file(template_content, student):
    filename = generate_filename(student)
    relative_path = "template_output"
    
    full_path = os.path.join(relative_path, filename)
    print(full_path)
    try:
        os.makedirs(relative_path, exist_ok=True)
        
        with open(full_path, 'w') as file:
            file.write(template_content)
        logger.info(f"Template file '{full_path}' created successfully.")
    except IOError as e:
        logger.error(f"Error writing to file '{filename}': {e}")