"""
Tests Online Portfolio Selection (OLPS).
"""
from unittest import TestCase
import os
import numpy as np
import pandas as pd
from mlfinlab.online_portfolio_selection import OLPS


class TestOLPS(TestCase):
    """
    Tests different functions of the OLPS class.
    """

    def setUp(self):
        """
        Set the file path for the tick data csv.
        """

        project_path = os.path.dirname(__file__)
        data_path = project_path + '/test_data/stock_prices.csv'
        self.data = pd.read_csv(data_path, parse_dates=True, index_col="Date")
        self.data = self.data.dropna(axis=1)

    def test_olps_solution(self):
        """
        Test the calculation of OLPS weights.
        """

        olps = OLPS()
        olps.allocate(self.data)
        all_weights = np.array(olps.all_weights)
        for i in range(all_weights.shape[0]):
            weights = all_weights[i]
            assert (weights >= 0).all()
            assert len(weights) == self.data.shape[1]
            np.testing.assert_almost_equal(np.sum(weights), 1)
