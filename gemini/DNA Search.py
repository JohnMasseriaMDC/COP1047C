"""
-------------------------------------------------------
DNA Sequence Search
-------------------------------------------------------
Author: Gabriel A. Diaz
Date: 2024-10-07
Course: Introduction to Python Programming
Assignment: DNA Sequence Search
-------------------------------------------------------

Description:
Reads known DNA sequences and their names from 'known_sequences.txt'
and searches for each unknown DNA sequence from 'unknown_sequences.txt'
within the known sequences. Prints the name of the containing sequence
or 'NOT FOUND' for each unknown sequence.

-------------------------------------------------------
Input files:

- known_sequences.txt
- unknown_sequences.txt

Outputs:

Unknown sequence 'AGTCAGTCAG' found in 'Human'.
Unknown sequence 'GGTACCAGGTAC' NOT found in known sequence

-------------------------------------------------------
Error Handling:
- Displays appropriate error message if any file does
  not exist

-------------------------------------------------------
"""
import os


def read_known_sequences(filename):
    """
    Reads known DNA sequences and names from a file into two parallel lists.

    Args:
        filename (str): The name of the file to read.

    Returns:
        tuple: A tuple containing two lists (names, sequences) or (None, None)
               if the file cannot be opened.
    """
    known_names = []
    known_sequences = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip leading/trailing whitespace and split the line at the first space.
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    name, sequence = parts
                    known_names.append(name)
                    known_sequences.append(sequence)
                # Ignore lines that don't conform to the "Name Sequence" format
        return known_names, known_sequences
    except FileNotFoundError:
        print(f"Error: The input file '{filename}' was not found in the directory.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None, None


def read_unknown_sequences(filename):
    """
    Reads unknown DNA sequences from a file into a list of strings.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of unknown DNA sequences or None if the file cannot be opened.
    """
    unknown_sequences = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Strip leading/trailing whitespace and ensure the sequence is not empty.
                sequence = line.strip()
                if sequence:
                    unknown_sequences.append(sequence)
        return unknown_sequences
    except FileNotFoundError:
        print(f"Error: The input file '{filename}' was not found in the directory.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filename}': {e}")
        return None


def search_dna_sequences(known_names, known_sequences, unknown_sequences):
    """
    Searches each unknown sequence within the known sequences and prints the results.

    Args:
        known_names (list): List of names corresponding to known sequences.
        known_sequences (list): List of known DNA sequence strings.
        unknown_sequences (list): List of unknown DNA sequence strings to search for.
    """
    print("--- Search Results ---")

    # Iterate through each unknown sequence
    for unknown_seq in unknown_sequences:
        found_in = None

        # Iterate through the known sequences using their index
        # We use zip to pair the name and sequence correctly.
        for name, known_seq in zip(known_names, known_sequences):

            # Check if the unknown sequence is a substring of the known sequence
            if unknown_seq in known_seq:
                found_in = name
                # Stop searching once a match is found for the current unknown sequence
                break

        # Print the result based on whether a match was found
        if found_in:
            print(f"Unknown sequence '{unknown_seq}' found in '{found_in}'.")
        else:
            print(f"Unknown sequence '{unknown_seq}' NOT found in known sequence.")


def main():
    """
    Main function to orchestrate reading files and searching sequences.
    """
    KNOWN_FILE = 'known_sequences.txt'
    UNKNOWN_FILE = 'unknown_sequences.txt'

    # 1. Read known sequences
    known_names, known_sequences = read_known_sequences(KNOWN_FILE)

    # Check if reading was successful (i.e., files exist and data was read)
    if known_names is None:
        return  # Exit if known sequences file failed to load

    # 2. Read unknown sequences
    unknown_sequences = read_unknown_sequences(UNKNOWN_FILE)

    if unknown_sequences is None:
        return  # Exit if unknown sequences file failed to load

    # Ensure we have data to search
    if not known_sequences:
        print("Warning: No known sequences were loaded. Cannot perform search.")
        return

    if not unknown_sequences:
        print("Warning: No unknown sequences were loaded. Nothing to search for.")
        return

    # 3. Search and print results
    search_dna_sequences(known_names, known_sequences, unknown_sequences)


if __name__ == "__main__":
    # Ensure the script runs the main function when executed
    main()