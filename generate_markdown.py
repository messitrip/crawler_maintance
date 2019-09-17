

from pandas import DataFrame
import pandas
from tabulate import tabulate

if __name__ == '__main__':
    import json
    with open("mapping.json","r") as f:
        result = json.load(f)
    df = DataFrame.from_dict(result)
    print(df)
    print(tabulate(df.T,tablefmt="pipe",headers="keys"))