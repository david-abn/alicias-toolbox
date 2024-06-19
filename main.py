from typing import Dict
import click

from helpers.file_helper import write_template_file
from helpers.template_helper import format_template, get_options

APP_VERSION = "0.1"


@click.command()
@click.option('--student', prompt="Student's Name",
              help='The student you are grading.')
@click.option('--team-name', prompt="Team Name",
              help='The student\'s team name.')
@click.option('--tutor', prompt="Tutor's Name",
              help='The tutor who is creating the response.')


def toolbox_start(student, team_name, tutor):
    """."""
    click.clear()
    click.pause(f"Hello, {tutor}! Welcome to Alicia's Toolbox (version {APP_VERSION}).\n\n"
                f"You will be creating a response for student {student} part of team {team_name}.\n"
                "You can cancel any time by closing this application.\n\n"
                "Press any key to continue...")
    click.clear()
    click.echo(f"Student: {student} // Team: {team_name} // Tutor: {tutor}\n"
    "Please choose a value (left side) for each ::Section:: of the template.")
    options = get_options()
    if not options:
        click.echo("No options found. Please check template_text file or reach out for help.")
        return
    user_input = get_input_for_options(options, student)
    create_output(user_input, student, team_name, tutor)
    
        
def get_input_for_options(options: Dict, student: str):
    selections = {}
    for section, values in options.items():
        click.secho(f"\n::{section}::", fg='yellow')
        
        for value, text in values.items():
            click.echo(f"{value}: {text} \n")
            
        while True:
            input = click.prompt(section, type=str)
            try:
                selections[section] = values[input]
                break
            except KeyError as e:
                click.secho(f"Invalid input for {section}: {input}", fg='red')
                expected_values = [val for val in values]
                click.secho(f"Expected input(s): {', '.join(expected_values)}", fg="red")
        
        click.secho("-" * 80, fg='green')
    
    return selections

def create_output(user_input, student, team_name, tutor):
    template_kwargs = {
        "Student": student,
        "Tutor": tutor,
        "Team Name": team_name,
        **user_input
    }
    formatted_template = format_template(template_kwargs)
    write_template_file(formatted_template, student)
    
    click.pause("\n\nPress any key to go again!!")
    toolbox_start()

def main():
    toolbox_start()

if __name__ == "__main__":
    main()