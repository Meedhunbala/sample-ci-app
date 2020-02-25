from custom_palindrome import isPalindrome, make_cli_parser
import unittest


class TestPalindrome(unittest.TestCase):

    def test_isPalindrome_with_alphabets(self):
        expected_results = True
        actual_results = isPalindrome("madam")
        self.assertEqual(
            expected_results, actual_results, "alpha-test-passed!!")

    def test_isPalindrome_with_numeric(self):
        expected_results = True
        actual_results = isPalindrome(121121)
        self.assertEqual(
            expected_results, actual_results, "numeric-test-passed!!")

    def test_isPalindrome_with_alphanumeric(self):
        expected_results = True
        actual_results = isPalindrome("001eye100")
        self.assertEqual(
            expected_results, actual_results, "alpha-numeric-test-passed!!")

    def test_isPalindrome_with_non_alphanumeric(self):
        expected_results = [True, True, True]
        inputs = ["_!MadAm@$", "RACEC@A@R", "RE&p*a(pe_r"]
        actual_results = [isPalindrome(_) for _ in inputs]
        self.assertEqual(
            expected_results,
            actual_results,
            "non-alpha-numeric-test-passed!!")


class TestArgumentsParsers(unittest.TestCase):

    def setUp(self):
        self.cli_parser = make_cli_parser()

    def test_arguments(self):
        args = ['--words', 'madam masd']
        args_namespace = self.cli_parser.parse_args(args)
        expected_arguments = ["madam masd"]

        self.assertEqual(expected_arguments, args_namespace.words)

    def test_no_arguments_passed(self):
        args = []
        args = self.cli_parser.parse_args(args)
        self.assertEqual(None, args.words)


if __name__ == '__main__':
    unittest.main()
