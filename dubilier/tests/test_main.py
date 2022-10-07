# pylint: disable=missing-docstring


import unittest
import unittest.mock
import dubilier.__main__


class TestMain(unittest.TestCase):

    @unittest.mock.patch("dubilier.cli.main")
    def test_main_cli(self, mock: unittest.mock.Mock) -> None:
        dubilier.__main__.main()
        mock.assert_called()
