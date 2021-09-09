from resumebuilder.models.experiences import Experiences
from resumebuilder.models.profile import Profile
from resumebuilder.util.markdown import MarkdownFormatter


class Resume:
    def __init__(self, file_prefix):
        self.profile = Profile(file_prefix)
        self.experiences = Experiences(file_prefix)
        self.md = MarkdownFormatter()
