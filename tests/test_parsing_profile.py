import unittest

from resumebuilder.models.profile import Profile


class ProfileParsingTestCase(unittest.TestCase):
    TEST_FILE_PREFIX = '../data/sample'

    def setUp(self) -> None:
        self.test_profile = Profile(self.TEST_FILE_PREFIX)

    def test_personal_info(self):
        self.assertEqual(self.test_profile.personal_info.name, "Ivy Haddington")
        self.assertEqual(self.test_profile.personal_info.email, "ihaddington@email.com")
        self.assertEqual(self.test_profile.personal_info.city, "Austin")
        self.assertEqual(self.test_profile.personal_info.state, "TX")
        self.assertEqual(self.test_profile.personal_info.phone, "(123)456-7891")
        self.assertEqual(self.test_profile.summary,
                         "Focused and quick-learning Software Engineer "
                         "with 3 years of experience in computer "
                         "science, programming, and UX design for "
                         "various projects and clients.")

    def test_educators(self):
        self.assertEqual(len(self.test_profile.educators), 1)
        self.assertEqual(self.test_profile.educators[0].name, "Hawaii Western")
        self.assertEqual(self.test_profile.educators[0].degree,
                         "Bachelor of Science in Electrical Engineering")
        self.assertEqual(self.test_profile.educators[0].graduated, "May 2014")

    def test_employers(self):
        self.assertEqual(len(self.test_profile.employers), 2)
        self.assertEqual(self.test_profile.employers[0].id, "CJ")
        self.assertEqual(self.test_profile.employers[0].name, "Crane & Jenkins")
        self.assertEqual(self.test_profile.employers[0].position, "Software Engineer")
        self.assertEqual(self.test_profile.employers[0].start_date, "July 2019")
        self.assertEqual(self.test_profile.employers[0].end_date, "Current")
        self.assertEqual(self.test_profile.employers[1].id, "TL")
        self.assertEqual(self.test_profile.employers[1].name, "Tradelot")
        self.assertEqual(self.test_profile.employers[1].position, "Software Developer")
        self.assertEqual(self.test_profile.employers[1].start_date, "August 2015")
        self.assertEqual(self.test_profile.employers[1].end_date, "July 2019")


if __name__ == '__main__':
    unittest.main()
