import random
import unittest

from fantasy_story import ENDINGS, generate_story


class GenerateStoryTests(unittest.TestCase):
    def test_generates_a_complete_short_story(self):
        story = generate_story(random.Random(7))

        self.assertTrue(story.endswith(tuple(ENDINGS)))
        self.assertGreaterEqual(story.count("."), 4)
        self.assertIn("with", story)

    def test_seeded_generation_is_reproducible(self):
        self.assertEqual(generate_story(random.Random(12)), generate_story(random.Random(12)))


if __name__ == "__main__":
    unittest.main()
