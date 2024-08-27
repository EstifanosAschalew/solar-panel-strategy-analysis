import unittest
import pandas as pd
import os
from scripts.data_processing import load_data, clean_data, calculate_correlation, prepare_time_series

class TestDataProcessing(unittest.TestCase):
    file_paths = [
        'C:\\Users\\Go a Head Bro\\Documents\\10Academy-AIM-Journey\\solar-panel-strategy-analysis\\data\\benin-malanville.csv',
        'C:\\Users\\Go a Head Bro\\Documents\\10Academy-AIM-Journey\\solar-panel-strategy-analysis\data\\sierraleone-bumbuna.csv',
        'C:\\Users\\Go a Head Bro\\Documents\\10Academy-AIM-Journey\\solar-panel-strategy-analysis\\data\\togo-dapaong_qc.csv'
        ]

    # Test if data loading works correctly for all datasets
    def test_load_data(self):
        for file_path in self.file_paths:
            df = load_data(file_path)
            self.assertFalse(df.empty, f"{file_path} should not be empty")
    
    # Test if data cleaning works correctly for all datasets
    def test_clean_data(self):
        for file_path in self.file_paths:
            df = load_data(file_path)
            cleaned_df = clean_data(df)
            self.assertFalse(cleaned_df.isnull().values.any(), f"{file_path} should not have any null values after cleaning")

    # Test if correlation calculation works correctly
    def test_calculate_correlation(self):
        for file_path in self.file_paths:
            df = load_data(file_path)
            cleaned_df = clean_data(df)
            corr_matrix = calculate_correlation(cleaned_df)
            self.assertEqual(corr_matrix.shape, (8, 8), f"{file_path} correlation matrix should be 8x8")

    # Test if time series preparation works correctly
    def test_prepare_time_series(self):
        for file_path in self.file_paths:
            df = load_data(file_path)
            prepared_df = prepare_time_series(df)
            self.assertTrue(pd.api.types.is_datetime64_any_dtype(prepared_df.index), f"{file_path} should have datetime index after preparation")

if __name__ == '__main__':
    unittest.main()
