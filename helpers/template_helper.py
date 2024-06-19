from typing import Dict

from helpers.file_helper import get_lines

TEMPLATE_STR = "Template"

def get_options() -> Dict[str, str]:
    lines = get_lines()

    options = {}
    current_section = None

    for line in lines:
        line = line.strip()
        if line and line[0:2] == "##":
            # Section is a header
            current_section = line[2:].strip()
            if current_section == TEMPLATE_STR:
                continue
            options[current_section] = {}
        elif line and current_section and current_section != TEMPLATE_STR:
            key, value = line.split(":", 1)
            options[current_section][key.strip()] = value.strip()
    
    return options
            
def get_template_string() -> str:
    lines = get_lines()
    
    template_start = False
    template_end = False
    template_lines = []

    for line in lines:
        if line.strip() == f"## {TEMPLATE_STR}":
            template_start = True
            continue
        elif "##" in line and template_start:
            # Any other named section found
            template_end = True
            break

        if template_start and not template_end:
            template_lines.append(line)

    template_string = ''.join(template_lines)
    return template_string

def format_template(selections):
    template = get_template_string()
   
    formatted_template = template.format(**selections)
    return formatted_template
    