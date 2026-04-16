import pandas as pd
import os


class DataReader:
    CACHE = {}

    @staticmethod
    def get(sheet, scenario_id, test_case_id):
        if sheet not in DataReader.CACHE:
            path = os.path.join("data", "test_data.xlsx")
            df = pd.read_excel(path, sheet_name=sheet, dtype=str)
            df.columns = df.columns.str.lower()
            DataReader.CACHE[sheet] = df

        df = DataReader.CACHE[sheet]

        row = df[
            (df["scenario_id"] == scenario_id) &
            (df["test_case_id"] == test_case_id)
        ]

        if row.empty:
            raise Exception("Data not found")

        return row.iloc[0].to_dict()