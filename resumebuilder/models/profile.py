import json


class Profile:
    FILENAME = "profile.json"

    summary = ""
    personal_info = None
    educators = []
    employers = []

    def __init__(self, file_prefix):
        full_filename = f"{file_prefix}.{self.FILENAME}"
        with open(full_filename, 'r') as json_file:
            data = json.load(json_file)
            self.personal_info = self.PersonalInfo(data['personal_info'])
            self.summary = data['summary']
            self.educators = [self.School(school_json) for school_json in data['educators']]
            self.employers = [self.Employer(employer_json) for employer_json in data['employers']]

    class PersonalInfo:
        def __init__(self, personal_json):
            self.name = personal_json['name']
            self.email = personal_json['email']
            self.city = personal_json['city']
            self.state = personal_json['state']
            self.phone = personal_json['phone']

    class School:
        def __init__(self, school_json: dict):
            self.name = school_json['name']
            self.degree = school_json['degree']
            self.graduated = school_json['graduated']

    class Employer:
        def __init__(self, employer_json: dict):
            self.id = employer_json['id']
            self.name = employer_json['name']
            self.position = employer_json['position']
            self.start_date = employer_json['start_date']
            self.end_date = employer_json['end_date']
