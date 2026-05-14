"""
------------------------------------------------------------------------
DNA Sequence Search
------------------------------------------------------------------------
Author: Jan Zika
Date: 7/23/2025
Course: Introduction to Python Programming
Assignment: DNA Sequence Search
------------------------------------------------------------------------

Description:
This program reads a set of known DNA sequences labeled by species,
and compares them to a list of unknown DNA sequences to determine
whether any known sequence contains each unknown as a substring.
If a match is found, the program outputs which species contain it.
If no match is found, the program states that clearly.
All matches are sorted alphabetically, and results are printed in
both sentence and tabular format.

------------------------------------------------------------------------
Input files:

- known_sequences.txt
- unknown_sequences.txt

Outputs:

Unknown sequence 'AGTCAGTCAG' found in a known sequence of Human.
Unknown sequence 'GGTACCAGGTAC' NOT FOUND in any known sequences.

(The wording of the output messages has been intentionally adapted
by the author to enhance human readability.)

------------------------------------------------------------------------
Error Handling:
Displays an appropriate error message if a file is missing,
locked, or inaccessible, and exits the program with an error code.

Error Codes:
1 - Cannot open known_sequences.txt for reading
    (missing or inaccessible)
2 - Cannot open unknown_sequences.txt for reading
    (missing or inaccessible)
3 - Cannot write to CSV file (locked or permission issue)
4 - Cannot read from CSV file (missing, locked, or permission issue)
------------------------------------------------------------------------
"""

# Import necessary modules
import os
import sys
import csv

# Define error message templates for file operations
ERROR_FILE_READ = (
    "Error: Cannot open '{}' for reading. File may be missing, locked, "
    "or inaccessible."
    )
ERROR_CSV_WRITE_LOCKED = (
    "Error: Cannot write to '{}' because it is open in another program "
    "(e.g., Excel). Please close the file and try again."
    )
ERROR_CSV_WRITE_FAIL = (
    "Error: Unable to write to file '{}'. Reason: {}"
    )
ERROR_CSV_READ_LOCKED = (
    "Error: Cannot read from '{}' because it is open in another program. "
    "Please close the file and try again."
    )
ERROR_CSV_READ_FAIL = (
    "Error: Unable to read from file '{}'. Reason: {}"
    )
ERROR_CSV_EMPTY = "Error: The CSV file is empty."

# Get the absolute path to the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct paths to input files relative to the script's folder
known_file = os.path.join(script_dir, 'known_sequences.txt')
unknown_file = os.path.join(script_dir, 'unknown_sequences.txt')

'''
1. Read all the known names and DNA sequences into two parallel lists.
The first list contains the name of the known sequence,
the other list contains the DNA sequence as a string.
'''
known_names = []
known_sequences = []

try:
    # open the file containing known sequences and read its contents
    with open(known_file, 'r') as file:  
        for line in file:
            name, sequence = line.strip().split(" ", 1)
            known_names.append(name)
            known_sequences.append(sequence)
except OSError:
    print(ERROR_FILE_READ.format(known_file))
    sys.exit(1)  # Exit the program with error code 1

'''
2. Read each unknown DNA sequence from the unknown_sequences.txt file.
'''
unknown_sequences = []

try:
    # open the file containing unknown sequences and read its contents
    with open(unknown_file, "r") as file:
        for line in file:
            unknown_sequences.append(line.strip())
except OSError:
    print(ERROR_FILE_READ.format(unknown_file))
    sys.exit(2)  # Exit the program with error code 2

'''
3. Search through the known sequences to determine if the "unknown sequence"
is contained in any of the known DNS sequences.
'''
# Create a dictionary of strings to lists of strings
# where each key is an unknown sequence and the value is a list of names 
# results = {"unknown_sequence": ["known_name1", "known_name2", ...]}
results = {}

for unknown in unknown_sequences:
    matches = []
    for i in range(len(known_names)):  # iterate through known sequences
        if unknown in known_sequences[i]:  # check if unknown is a substring
            matches.append(known_names[i])  # add the name of the known sequence to matches
    results[unknown] = matches  # add matches to results dictionary

'''
4. Print results:
   If found, show which known sequence (by name) contains the unknown.
   If not found, display a "NOT FOUND" message.
'''
# Iterate through results and print matches
for unknown, matches in results.items():
    prefix = f"Unknown sequence '{unknown}' "
    if matches:  # if matches is not an empty list
        sorted_matches = sorted(matches)  # create a sorted list of matches
        if len(sorted_matches) == 1:  # only one match
            detail = f"found in a known sequence of {sorted_matches[0]}."
        elif len(sorted_matches) == 2:  # two matches
            formatted_matches = f"{sorted_matches[0]} and {sorted_matches[1]}"
            detail = f"found in known sequences of {formatted_matches}."
        else:  # more than two matches
            formatted_matches = (
                f"{', '.join(sorted_matches[:-1])}, and {sorted_matches[-1]}")
            detail = f"found in known sequences of {formatted_matches}."
    else:  # no matches found
        detail = "NOT FOUND in any known sequences."
    print(prefix + detail)

'''
For major extra credit (at least 15 points),
I could display the matches not only alphabetically,
but also in a fancy ASCII table for viewing pleasure.
The docstring was clearly crafted by a superhuman intelligence,
so I won't attempt to ruin it with primate scribbles.
'''
# Define a reusable function to print any table given headers and rows
def print_table(headers, rows):
    """
    Print a formatted ASCII table with aligned columns.

    Adjusts column widths based on the longest value in each column and
    ensures proper alignment. Includes a header row, horizontal separators,
    and left-aligned cell values.

    Args:
        headers (list[str]): Column names for the table header.
        rows (list[list[str]]): Table rows, each a list of cell values.

    Notes:
        - Pads rows with empty strings if they have fewer columns than headers.
        - Handles extra columns by expanding widths dynamically.

    Example:
        >>> headers = ["Name", "Age"]
        >>> rows = [["Alice", "30"], ["Bob", "25"]]
        >>> print_table(headers, rows)
        +-------+-----+
        | Name  | Age |
        +-------+-----+
        | Alice | 30  |
        | Bob   | 25  |
        +-------+-----+
    """
    # Calculate column widths
    col_widths = [len(header) for header in headers]
    for row in rows:
        for i, cell in enumerate(row):  # iterate through each cell in the row
            if i < len(col_widths):  # ensure column index is within bounds
                col_widths[i] = max(col_widths[i], len(cell))  # update width if cell is wider
            else:
                # If row has more columns than headers, extend col_widths
                col_widths.append(len(cell))

    # Function to create a separator line
    def make_separator():
        return "+" + "+".join("-" * (w + 2) for w in col_widths) + "+"
    
    # Row format: | value1 | value2 | ... |
    row_format = "| " + " | ".join(f"{{:<{w}}}" for w in col_widths) + " |"

    # Print table
    print(make_separator())
    print(row_format.format(*headers))
    print(make_separator())
    for row in rows:
        # Ensure each row has the same number of columns as headers
        # by padding with empty strings if necessary
        padded_row = row + [""] * (len(col_widths) - len(row))
        print(row_format.format(*padded_row))
    print(make_separator())

# Prepare results for tabular format
rows = []
for unknown, matches in results.items():
    sorted_matches = sorted(matches)
    match_text = "—" if not sorted_matches else ", ".join(sorted_matches)
    rows.append([unknown, match_text])

# Print results table
print("\nFormatted Results Table:")
print_table(["Unknown DNA", "Matched Species"], rows)

'''
For an absurd amount of extra extra credit,
I could export the results to a CSV, reload them,
and display them for dramatic verification
using the same reusable print_table() function.
'''
output_file = os.path.join(script_dir, "dna_matches_output.csv")

# Write results to CSV, with error handling
try:
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Unknown DNA", "Matched Species"])
        for unknown in sorted(results):  # sort by DNA string
            matches = sorted(results[unknown])
            if matches:
                for name in matches:
                    writer.writerow([unknown, name])
            else:
                writer.writerow([unknown, ""])  # empty string for NOT FOUND
    print(f"\nResults written to: {output_file}\n")
except PermissionError:
    print(ERROR_CSV_WRITE_LOCKED.format(output_file))
    sys.exit(3)  # Exit the program with error code 3
except OSError as e:
    print(ERROR_CSV_WRITE_FAIL.format(output_file, e))
    sys.exit(3)  # Exit the program with error code 3

# Read CSV and display for verification, with error handling
try:
    with open(output_file, newline="") as csvfile:
        reader = list(csv.reader(csvfile))
        if not reader:
            print("Error: The CSV file is empty.")
            sys.exit(4)
        headers = reader[0]
        data_rows = reader[1:]
        print("CSV Verification Table:")
        print_table(headers, data_rows)
except PermissionError:
    print(ERROR_CSV_READ_LOCKED.format(output_file))
    sys.exit(4)  # Exit the program with error code 4
except OSError as e:
    print(ERROR_CSV_READ_FAIL.format(output_file, e))
    sys.exit(4)  # Exit the program with error code 4