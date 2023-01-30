import unittest
import soccer

class TestSoccer(unittest.TestCase):

    def test_get_config(self):
        self.assertEqual(
            soccer.load_configs("default"),
            [
                ["id", False],
                ["points_total", True]
            ]
        )

    def

if __name__ == '__main__':
    unittest.main()