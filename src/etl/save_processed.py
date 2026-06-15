from pathlib import Path

PROCESSED_PATH = Path(
    "data/processed"
)

def save_dataframe(
    df,
    file_name
):

    output_path = (
        PROCESSED_PATH /
        file_name
    )

    df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Saved -> {output_path}"
    )