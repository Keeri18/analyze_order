#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
import pandas as pd
from data_processing import (
    compute_total_revenue_by_month,
    compute_total_revenue_by_product,
    compute_total_revenue_by_customer,
    identify_top_10_customers,
)

class TestDataProcessing(unittest.TestCase):
    def test_compute_total_revenue_by_month(self):
        # Test if the function runs without errors
        # You can create a sample DataFrame and call the function with it
        data = pd.DataFrame({
            'Order Date': pd.to_datetime(['2022-01-01', '2022-02-01', '2022-02-15']),
            'Unit Price': [10, 20, 30]
        })
        result = compute_total_revenue_by_month(data)
        expected_result = pd.Series([10, 50], name='Unit Price', dtype='float64', index=pd.PeriodIndex(['2022-01', '2022-02'], freq='M'))
        pd.testing.assert_series_equal(result, expected_result)

    # Add similar test methods for other functions

if __name__ == '__main__':
    unittest.main()

