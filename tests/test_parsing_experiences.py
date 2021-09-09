import unittest

from resumebuilder.models.experiences import Experiences


class ProfileParsingTestCase(unittest.TestCase):
    TEST_FILE_PREFIX = '../data/sample'

    def setUp(self) -> None:
        self.test_experiences = Experiences(self.TEST_FILE_PREFIX).rows

    def check_experience(self, index, company_id, skills, tech, description):
        self.assertEqual(self.test_experiences[index].company_id, company_id)
        self.assertEqual(self.test_experiences[index].skills, skills)
        self.assertEqual(self.test_experiences[index].technologies, tech)
        self.assertEqual(self.test_experiences[index].description, description)

    def test_experiences(self):
        self.assertEqual(len(self.test_experiences), 6)
        self.check_experience(0, "CJ", "Data Management", "Perl|PHP", "Developed Perl and PHP scripts to translate "
                                                                      "data between applications")
        self.check_experience(1, "CJ", "Automation", "Python", "Developed automation scripts to test storage "
                                                               "appliances in Python")
        self.check_experience(2, "CJ", "Agile Practicing", "", "Practice agile development methodologies and work "
                                                               "with current networking")
        self.check_experience(3, "CJ", "Big Data", "Hadoop",
                              "Used Hadoop to build a scalable distributed data solution")
        self.check_experience(4, "TL", "Web Development", "HTML|CSS|JavaScript|JSP", "Developed HTML, CSS, JavaScript "
                                                                                     "and JSP pages for user "
                                                                                     "interaction")
        self.check_experience(5, "TL", "Data Management", "Python|XML", "Wrote Python scripts to load data and parse "
                                                                        "XML documents")


if __name__ == '__main__':
    unittest.main()
