"""
-------------------------------------------------------
DNA Sequence Search
-------------------------------------------------------
Author: Gemini
Date: 2025-10-09
Course: Introduction to Python Programming
Assignment: DNA Sequence Search
-------------------------------------------------------

Description:
Reads known DNA sequences and names from one file, and unknown
sequences from another. It then searches to see if each unknown
sequence is contained within any of the known sequences, printing
the results clearly.

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

import sys

# --- File Handling Functions ---

def read_known_sequences(filepath):
    """
    Reads known DNA sequences and their corresponding names from a file.
    
    The file is expected to have one name and one sequence per line,
    separated by a space.

    Args:
        filepath (str): The path to the known_sequences.txt file.

    Returns:
        tuple: A tuple containing two parallel lists (names, sequences),
               or (None, None) if the file cannot be read.
    """
    known_names = []
    known_sequences = []
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # Strip whitespace and split the line once by the first space
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    name, sequence = parts
                    known_names.append(name.strip())
                    known_sequences.append(sequence.strip())
        return known_names, known_sequences
    except FileNotFoundError:
        print(f"ERROR: Input file not found: {filepath}", file=sys.stderr)
        return None, None
    except Exception as e:
        print(f"An error occurred while reading {filepath}: {e}", file=sys.stderr)
        return None, None

def read_unknown_sequences(filepath):
    """
    Reads unknown DNA sequences from a file.

    The file is expected to have one DNA sequence per line.

    Args:
        filepath (str): The path to the unknown_sequences.txt file.

    Returns:
        list: A list of unknown DNA sequence strings, or None if the file 
              cannot be read.
    """
    unknown_sequences = []
    
    try:
        with open(filepath, 'r') as file:
            for line in file:
                # Strip whitespace, including the newline character
                unknown_sequences.append(line.strip())
        return unknown_sequences
    except FileNotFoundError:
        print(f"ERROR: Input file not found: {filepath}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An error occurred while reading {filepath}: {e}", file=sys.stderr)
        return None

# --- Core Search Logic ---

def search_dna_sequences(known_names, known_sequences, unknown_sequences):
    """
    Searches for each unknown sequence within the known sequences.

    Prints the result for each unknown sequence (found or not found).

    Args:
        known_names (list): List of names for known sequences.
        known_sequences (list): List of known DNA sequence strings.
        unknown_sequences (list): List of unknown DNA sequence strings to search for.
    """
    
    print("\n--- DNA Sequence Search Results ---")
    
    for unknown_seq in unknown_sequences:
        if not unknown_seq:
            continue # Skip empty lines
            
        found = False
        
        # Iterate through the known sequences using index for parallel access
        for i in range(len(known_sequences)):
            known_name = known_names[i]
            known_seq = known_sequences[i]
            
            # Substring search using the 'in' operator
            if unknown_seq in known_seq:
                print(f"Unknown sequence '{unknown_seq}' found in '{known_name}'.")
                found = True
                break # Stop searching known sequences once a match is found
        
        if not found:
            print(f"Unknown sequence '{unknown_seq}' NOT found in known sequences.")

# --- Main Program Execution ---

def main():
    """
    Main function to coordinate the reading, processing, and searching of DNA sequences.
    """
    KNOWN_FILE = "known_sequences.txt"
    UNKNOWN_FILE = "unknown_sequences.txt"
    
    # 1. Read known sequences
    known_names, known_sequences = read_known_sequences(KNOWN_FILE)
    
    if known_names is None:
        return # Exit if file reading failed

    # 2. Read unknown sequences
    unknown_sequences = read_unknown_sequences(UNKNOWN_FILE)
    
    if unknown_sequences is None:
        return # Exit if file reading failed
        
    # 3. Search and print results
    search_dna_sequences(known_names, known_sequences, unknown_sequences)

if __name__ == "__main__":
    main()

