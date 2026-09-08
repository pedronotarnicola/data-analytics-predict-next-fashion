from nbresult import ChallengeResultTestCase


class TestDataLoading(ChallengeResultTestCase):

    def test_data_loaded(self):
        """Loaded dataset successfully"""
        self.assertGreater(
            self.result.n_rows,
            200,
            "Hint: Load the tendances.csv dataset")

    def test_index_converted(self):
        """Converted index to period type"""
        self.assertTrue(self.result.index_is_period,
                        "Hint: Convert index to period with .to_period()")

    def test_train_test_split_done(self):
        """Split into train and test sets"""
        self.assertEqual(
            self.result.test_size,
            52,
            "Hint: Use temporal_train_test_split with test_size=52")
