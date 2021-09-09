from resumebuilder.lib.markdown import MarkdownFormatter
from resumebuilder.models.experiences import Experience, Experiences
from resumebuilder.models.profile import Profile, PersonalInfo, School, Employer
from resumebuilder.models.resume import Resume


class StandardLayout:
    def __init__(self, resume: Resume):
        self.resume = resume
        self.md = MarkdownFormatter()

    def __str__(self):
        profile = self.md_profile(self.resume.profile)
        education = self.md_educators(self.resume.profile.educators)
        experience = self.md_experience(self.resume.profile.employers, self.resume.experiences)
        return profile + experience + education

    def md_profile(self, profile: Profile):
        personal_info = self.md_personal_info(profile.personal_info)
        summary = self.md_summary(profile.summary)
        return f"{personal_info}\n" \
               f"{summary}\n"

    # ----------- Personal Info -----------
    def md_personal_info(self, personal_info: PersonalInfo):
        return f"{self.md.header(personal_info.name, 1)}\n" \
               f"{personal_info.email} {self.md.bold('|')} " \
               f"{personal_info.phone} {self.md.bold('|')} " \
               f"{personal_info.city}, {personal_info.state}\n"

    # ----------- Summary -----------
    def md_summary(self, summary):
        return f"{self.md.header('Summary', 2)}\n" \
               f"{summary}\n"

    # ----------- Education -----------
    def md_educators(self, educators: [School]):
        result = f"{self.md.header('Education', 2)}\n"
        for school in educators:
            result += f"{self.md.header(school.name, 3)}, {school.graduated}\n" \
                      f"{school.degree}\n\n"
        return result

    # ----------- Experience -----------
    def md_experience(self, employers: [Employer], experiences: Experiences):
        result = f"{self.md.header('Experience', 2)}\n"
        for employer in employers:
            result += self.md_employer(
                employer,
                experiences.get_experience_for_employer(employer.id)
            )
        return result + "\n"

    def md_employer(self, employer: Employer, experiences: [Experience]):
        header = f"{employer.name} ({employer.start_date} - {employer.end_date})"
        result = f"{self.md.header(header, 3)}\n" \
                 f"{self.md.italic(employer.position)}\n"
        for experience in experiences:
            result += f"{self.md.bullet_list_item(experience.description)}\n"
        return result
