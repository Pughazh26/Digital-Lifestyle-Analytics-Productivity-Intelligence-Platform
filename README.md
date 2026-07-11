# Digital Lifestyle Analytics

An analytics project for studying digital lifestyle habits, productivity, screen time, sleep, exercise, and related wellbeing signals.

## Project Structure

```text
Digital-Lifestyle-Analytics
├── data
│   ├── raw
│   └── cleaned
├── notebooks
├── sql
├── powerbi
├── reports
├── images
└── src
```

## Workflow

1. Generate sample data:

   ```powershell
   py -3.12 src/generate_data.py
   ```

2. Clean the raw data:

   ```powershell
   py -3.12 src/clean_data.py
   ```

3. Create engineered features:

   ```powershell
   py -3.12 src/feature_engineering.py
   ```

4. Export SQL insert statements:

   ```powershell
   py -3.12 src/export_sql.py
   ```

5. Run SQL scripts from the `sql` folder and connect Power BI to the cleaned data or database.

## Main Outputs

- `data/raw/digital_lifestyle_dataset.csv`
- `data/cleaned/digital_lifestyle_cleaned.csv`
- `data/cleaned/digital_lifestyle_features.csv`
- `sql/insert_data.sql`
- `powerbi/Digital_Lifestyle_Dashboard.pbix`
