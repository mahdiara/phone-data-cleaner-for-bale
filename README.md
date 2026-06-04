# Phone Data Cleaner For Bale

A simple Python utility for preparing Iranian mobile phone numbers for bulk messaging in Bale.

## Features

- Converts 09xxxxxxxxx to 989xxxxxxxxx
- Removes invalid numbers
- Removes duplicates
- Cleans unwanted characters
- Splits large files into chunks of 9999 rows
- Automatically detects CSV files next to the script

## Input Example

```csv
09123456789
989351234567
test
abc
```

## Output Example

```csv
989123456789
989351234567
```

## Usage

1. Place your CSV file next to the script.
2. Run:

```bash
python phone-data-cleaner-for-bale.py
```

3. The script creates:
   - *_clean.csv
   - *_part1.csv
   - *_part2.csv
   - ...

## Target Use Case

Preparing phone number lists for Bale bot bulk messaging.

## License

MIT
