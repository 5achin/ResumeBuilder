import csv


class Experiences:
    FILENAME = 'experiences.csv'

    experiences = []

    def __init__(self, file_prefix):
        full_filename = f"{file_prefix}.{self.FILENAME}"
        with open(full_filename, 'r') as csv_file:
            data = csv.DictReader(csv_file)
            self.experiences = [self.Experience(experience_entry) for experience_entry in data]

    class Experience:
        def __init__(self, entry: dict):
            self.company_id = entry['Company']
            self.skills = entry['Skills']
            self.technologies = entry['Technologies']
            self.description = entry['Description'].replace('"', '')
