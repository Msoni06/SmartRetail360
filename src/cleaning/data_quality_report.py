import pandas as pd
from pathlib import Path

CLEAN_PATH = Path(
    "data/cleaned"
)

FILES = list(
    CLEAN_PATH.glob("*.csv")
)

for file in FILES:

    df = pd.read_csv(file)

    print("\n" + "=" * 50)
    print(file.name)

    print(
        f"Rows: {df.shape[0]}"
    )

    print(
        f"Columns: {df.shape[1]}"
    )

    print(
        "\nMissing Values:"
    )

    print(
        df.isnull().sum()
    )