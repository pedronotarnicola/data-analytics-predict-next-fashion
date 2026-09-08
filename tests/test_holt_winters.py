from nbresult import ChallengeResultTestCase


class TestHoltWinters(ChallengeResultTestCase):

    def test_holt_winters_exists(self):
        """Created Holt-Winters model"""
        self.assertTrue(
            self.result.hw_exists,
            "Hint: Create ExponentialSmoothing model with trend and seasonal parameters")

    def test_holt_winters_predictions(self):
        """Made Holt-Winters predictions"""
        self.assertEqual(
            self.result.hw_pred_length,
            52,
            "Hint: Predict 52 weeks with Holt-Winters model")

    def test_holt_winters_better_than_naive(self):
        """Holt-Winters MASE is better than naive (< 1.0)"""
        self.assertLess(
            self.result.hw_mase,
            1.0,
            "Hint: Check your trend and seasonal settings - MASE should be less than 1.0")
