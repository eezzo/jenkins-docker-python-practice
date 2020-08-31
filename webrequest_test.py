import unittest
import webrequest


class TestGetWebPage(unittest.TestCase):

    def test_200_response_status(self):
        url = "https://anilist.co/home"
        req = webrequest.get_web_page(url)
        self.assertEqual(req.status_code, 200)


if __name__ == '__main__':
    unittest.main()
