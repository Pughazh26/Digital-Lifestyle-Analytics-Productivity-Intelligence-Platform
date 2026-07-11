from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = ROOT / "data" / "cleaned" / "digital_lifestyle_features.csv"
OUTPUT_FILE = ROOT / "sql" / "insert_data.sql"


def sql_value(value) -> str:
    if pd.isna(value):
        return "NULL"
    if isinstance(value, str):
        return "'" + value.replace("'", "''") + "'"
    return str(value)


def build_insert_sql(df: pd.DataFrame) -> str:
    columns = list(df.columns)
    lines = ["-- Generated insert statements for digital_lifestyle_metrics"]

    for _, row in df.iterrows():
        values = ", ".join(sql_value(row[column]) for column in columns)
        column_list = ", ".join(columns)
        lines.append(f"INSERT INTO digital_lifestyle_metrics ({column_list}) VALUES ({values});")

    return "\n".join(lines) + "\n"


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Missing input file: {INPUT_FILE}. Run feature_engineering.py first.")

    df = pd.read_csv(INPUT_FILE)
    OUTPUT_FILE.write_text(build_insert_sql(df), encoding="utf-8")
    print(f"Saved SQL inserts to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
