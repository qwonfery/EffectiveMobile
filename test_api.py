import unittest
import requests

from dotenv import dotenv_values


class TestApi(unittest.TestCase):

    def setUp(self):

        config = dotenv_values()

        self.user = config['GITHUB_ACCOUNT']
        self.repo_name = config['REPOSITORY_NAME']

        self.headers = {
            "Authorization": f"Bearer {config['API_TOKEN']}",
        }

    def test1_create_repo(self):

        URL = "https://api.github.com/user/repos"

        data = {
            "name": self.repo_name
        }

        response = requests.post(URL, headers=self.headers, json=data)
        self.assertEqual(response.status_code, 201)

    def test2_check_repo(self):

        URL = "https://api.github.com/user/repos"

        response = requests.get(URL, headers=self.headers, timeout=10)

        self.assertEqual(response.status_code, 200)
        repos = response.json()
        founded = False
        for repo in repos:
            if repo["name"] == self.repo_name:
                founded = True
                break

        self.assertTrue(founded)

    def test3_delete_repo(self):

        url = f"https://api.github.com/repos/{self.user}/{self.repo_name}"

        response = requests.delete(url, headers=self.headers)
        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
