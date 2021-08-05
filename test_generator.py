import unittest
from generator import *

class Test (unittest.TestCase):
    file = read_all_lines("test.txt")
    source = Solution(file[0], file[1], file[3:])

    def test_get_title(self):
        result = self.source.get_title()
        expect = "## Insert Interval"
        self.assertEqual(result, expect)

    def test_get_contents(self):
        result = self.source.get_contents()
        expect = "+ [Insert Interval](#insert-interval)\n\n[comment]: <> (Stop)\n"
        self.assertEqual(result, expect)

    def test_get_code(self):
        result = self.source.get_code()
        expect = "``` python\ndef insert():\n    text\n```"
        self.assertEqual(result, expect)

    def test_get_solution(self):
        result = self.source.get_solution()
        expect = "+ [Insert Interval](#insert-interval)\n\n[comment]: <> (Stop)\n\n## Insert Interval\n\n" \
                 "https://leetcode.com/problems/insert-interval/\n\n``` python\ndef insert():\n    text\n```"
        self.assertEqual(result, expect)

    def test_read_all_lines(self):
        result = read_all_lines("test.txt")
        expect = ['57. Insert Interval\n',
                  'https://leetcode.com/problems/insert-interval/\n',
                  'class Solution:\n',
                  '    def insert():\n',
                  '        text']
        self.assertEqual(result, expect)

    def test_merge(self):
        old = 'old_start \n[comment]: <> (Stop)\nold_end'
        new = 'new_start \n[comment]: <> (Stop)\nnew_end'
        result = merge(old, new)
        expect = 'old_start new_start \n[comment]: <> (Stop)\nold_endnew_end'
        self.assertEqual(result, expect)

if __name__ == '__main__':
    unittest.main()