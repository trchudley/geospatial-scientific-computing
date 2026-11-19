"""
plot_graphs.py

Plot a daily temperature/precipitation graph for every monthly ERA5 CSV file in
INPUT_DIR, saving the plots to OUTPUT_DIR using the same directory structure.

Run from the terminal using:

    python plot_graphs.py
"""

from pathlib import Path

import pandas as pd
from tqdm import tqdm

from plotting import plot_graph

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------

# Paths are built relative to the location of this script, rather than
# wherever the script happens to be run from
SCRIPT_DIR = Path(__file__).parent

INPUT_DIR = SCRIPT_DIR / "era5_bristol_record"
OUTPUT_DIR = SCRIPT_DIR / "outputs" / "era5_bristol_plots"

# If False, files that have already been processed will be skipped
OVERWRITE = False


# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

def process_file(in_path, out_path):
    """Read a single monthly ERA5 CSV file and save a plot of it."""
    df = pd.read_csv(in_path, parse_dates=["date"])
    plot_graph(df, write_to_file=out_path)


def main():

    filepaths = sorted(INPUT_DIR.glob("*/*/*.csv"))
    print(f"Found {len(filepaths)} files in {INPUT_DIR.name}")

    # Stop early if there is nothing to process
    if len(filepaths) == 0:
        raise FileNotFoundError(f"No CSV files found in {INPUT_DIR}")

    failed = []
    skipped = 0

    for in_path in tqdm(filepaths):

        # Build the output path so it mirrors the input path
        out_path = OUTPUT_DIR / in_path.relative_to(INPUT_DIR).with_suffix(".png")

        # Skip this file if it has already been processed
        if out_path.exists() and not OVERWRITE:
            skipped += 1
            continue

        # Create the output directory (and any parent directories) if needed
        out_path.parent.mkdir(parents=True, exist_ok=True)

        # If processing fails, record the file and the error, and move on
        try:
            process_file(in_path, out_path)
        except Exception as e:
            failed.append((in_path, e))

    print(f"Processed: {len(filepaths) - skipped - len(failed)}")
    print(f"Skipped (already exist): {skipped}")
    print(f"Failed: {len(failed)}")

    for path, error in failed:
        print(f"  {path}: {error}")


if __name__ == "__main__":
    main()
