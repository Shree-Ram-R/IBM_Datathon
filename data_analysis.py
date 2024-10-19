import pandas as pd
class DataAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze(self):
        print("\nDataset Overview:")
        print(f"\nNumber of Rows: {self.data.shape[0]}")
        print(f"Number of Columns: {self.data.shape[1]}")
        print("\nColumn-wise Data Types and Null Value Counts:\n")
        print(self.data.info())
        print("\nNull Values in each Column:\n")
        print(self.data.isnull().sum())
