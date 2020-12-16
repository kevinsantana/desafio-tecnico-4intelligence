import unittest

from tests.unit import client


class TestHealthCheck(unittest.TestCase):
    def setUp(self):
        self.response_health_check = client.get("/v1/health")

    def test_health_check(self):
        self.assertEqual(self.response_health_check.status_code, 200)
        self.assertIn("result", self.response_health_check.json())
        self.assertIs(type(self.response_health_check.json().get("result")), list)


if __name__ == "__main__":
    unittest.main()
