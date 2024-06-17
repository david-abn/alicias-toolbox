from selections import selections
from errors import MissingSelection

import time

def main():
    tutor_selections: list = selections()
    for selection in tutor_selections:
        tutor_template = TutorTemplate(**selection)
        template = tutor_template.create_template_str()
        
        filename = generate_filename()
        with open(f"template_output/{filename}", 'a') as file:
            file.write(template)

def generate_filename() -> str:
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{timestamp}.txt"
    return filename


class TutorTemplate:
    def __init__(self, **selections):
        self.selections = selections
        self.check_selections_valid()
        
    def check_selections_valid(self):
        expected_values = ["student", "body_language", "voice", "speed", "interactions", "recall", "q_and_a", "tutor"]
        missing_values = [value for value in expected_values if value not in self.selections]
        
        if missing_values:
            error = f"The following expected values are missing from selections.py: {missing_values}"
            raise MissingSelection(error)
        
    def create_template_str(self): 
        return (f"Dear {self.selections['student']}, \n\n"
        f"Well done on the delivery of your individual content during the (team name) pitch. It is suggested you watch back the recording to note these features to make a goal for your next verbal presentation. \n\n"
        f"Within the presentation you {self.selections['body_language']}, {self.selections['voice']} & {self.selections['speed']}. To engage the audience {self.selections['interactions']} and overall {self.selections['recall']}.\n\n"
        f"Further within the Q&A {self.selections['q_and_a']}.\n\n"
        f"Your hard work on developing this skill is noted, and I wish you all the best in your next pitch!\n\n"
        f"Best, {self.selections['tutor']}\n\n"
        )
    
if __name__ == "__main__":
    main()