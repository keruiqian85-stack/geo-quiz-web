import unittest
from copy import deepcopy
from unittest.mock import patch
import prepare_review as review


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.q = dict(category='自然地理', book='必修一', question='影响河流流量的因素是什么？',
                      options=['降水', '经度', '地名', '行政等级'], answer=0, explanation='解析')

    def test_valid(self):
        self.assertEqual(len(review.validate_candidates([self.q], [], 1)), 1)

    def test_failures(self):
        for incoming in ([], {}, None, [self.q, self.q]):
            with self.subTest(incoming=incoming), self.assertRaises(ValueError):
                review.validate_candidates(incoming, [], 1)

    def test_duplicate(self):
        with self.assertRaises(ValueError):
            review.validate_candidates([self.q], [self.q], 1)
        with self.assertRaises(ValueError):
            review.validate_candidates([self.q, self.q], [], 2)

    def test_invalid_answer(self):
        for answer in (True, 1.0, -1, 4):
            q = deepcopy(self.q)
            q['answer'] = answer
            with self.assertRaises(ValueError):
                review.validate_candidates([q], [], 1)

    def test_escape(self):
        q = dict(self.q, explanation='<script>@someone</script>')
        body = review.review_body([q])
        self.assertNotIn('<script>', body)
        self.assertNotIn('@someone', body)

    def test_failed_generation_never_writes_bank(self):
        with patch('sys.argv', ['prepare_review.py', '--topic', '测试', '--body', 'unused.md']), \
             patch.object(review, 'load_bank', return_value=[]), \
             patch.object(review, 'generate_with_ai', return_value=[]), \
             patch.object(review, 'sync_to_js') as sync:
            with self.assertRaises(ValueError):
                review.main()
            sync.assert_not_called()


if __name__ == '__main__':
    unittest.main()
