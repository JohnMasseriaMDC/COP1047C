"""
-------------------------------------------------------
DNA Sequence Search
-------------------------------------------------------
Author: Anthony Bartelemi
Date: [07/30/2025]
Course: Introduction to Python Programming
Assignment: DNA Sequence Search
-------------------------------------------------------

Description:
This program reads known DNA sequences and compares unknown DNA sequences
to see if any are substrings of the known ones. It prints out where each
unknown sequence is found or not found.

-------------------------------------------------------
Input files:

- known_sequences.txt
- unknown_sequences.txt

Outputs:

Unknown sequence 'AGTCAGTCAG' found in 'Human'.
Unknown sequence 'GGTATGCAGTAC' NOT found in known sequences.

-------------------------------------------------------
Error Handling:
- Displays appropriate error message if any file does
  not exist

-------------------------------------------------------
"""

def read_known_sequences(filename):
    """Reads known sequences from a file into parallel lists."""
    names = []
    sequences = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(maxsplit=1)
                    if len(parts) == 2:
                        names.append(parts[0])
                        sequences.append(parts[1])
        return names, sequences
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None, None

def read_unknown_sequences(filename):
    """Reads unknown sequences from a file into a list."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

def search_sequences(unknowns, known_names, known_sequences):
    """Searches for each unknown DNA sequence in known sequences."""
    for unknown in unknowns:
        found = False
        for i in range(len(known_sequences)):
            if unknown in known_sequences[i]:
                print(f"Unknown sequence '{unknown}' found in '{known_names[i]}'.")
                found = True
                break
        if not found:
            print(f"Unknown sequence '{unknown}' NOT found in known sequences.")
def main():
    """Main function to execute the DNA sequence search."""
    known_file = 'known_sequences.txt'
    unknown_file = 'unknown_sequences.txt'

    known_names, known_sequences = read_known_sequences(known_file)
    if known_names is None or known_sequences is None:
        return

    unknowns = read_unknown_sequences(unknown_file)
    if unknowns is None:
        return

    search_sequences(unknowns, known_names, known_sequences)

if __name__ == "__main__":
    main()
