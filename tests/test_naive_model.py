from nbresult import ChallengeResultTestCase


class TestNaiveModel(ChallengeResultTestCase):

    def test_naive_model_exists(self):
        """Created naive model"""
        self.assertTrue(self.result.naive_exists,
                        "Hint: Create and fit a NaiveForecaster model")

    def test_naive_predictions_made(self):
        """Made naive predictions"""
        self.assertEqual(
            self.result.naive_pred_length,
            52,
            "Hint: Predict 52 weeks with naive_model.predict(fh=list(range(1,53)))")

    def test_naive_metrics_calculated(self):
        """Calculated naive model metrics"""
        self.assertIsNotNone(
            self.result.naive_mae,
            "Hint: Calculate MAE for naive model")
