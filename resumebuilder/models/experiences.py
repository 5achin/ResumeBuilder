import csv


class Experiences:
    FILENAME = 'experiences.csv'

    def __init__(self, file_prefix):
        full_filename = f"{file_prefix}.{self.FILENAME}"
        with open(full_filename, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            self.rows = [Experience(experience_entry) for experience_entry in data]

    def get_experience_for_employer(self, employer_id):
        return [experience for experience in self.rows if experience.company_id == employer_id]


class Experience:
    def __init__(self, entry: dict):
        self.company_id = entry['company']
        self.skills = entry['skills']
        self.technologies = entry['technologies']
        self.description = entry['description'].replace('"', '')
