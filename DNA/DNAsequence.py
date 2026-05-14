"""
-------------------------------------------------------
DNA Sequence Search
-------------------------------------------------------
Author: John Masseria
Date: December 4, 2025
Course: Introduction to Python Programming
Assignment: DNA Sequence Search
-------------------------------------------------------

Description:
[ Provide an appropriate description of the program ]

-------------------------------------------------------
Input files:

- known_sequences.txt
- unknown_sequences.txt

Outputs:

Unknown sequence 'AGTCAGTCAG' found in 'Human'.
Unknown sequence 'GGTACCAGGTAC' NOT found in known sequence

-------------------------------------------------------
Error Handling:
- Displays approriate error message if any file does
  not exist
  
-------------------------------------------------------
"""

def main( ):
    
    known_sequences = dict()

    with open("known_sequences.txt", "r") as myfile:
        lines = myfile.readlines()

        for line in lines:
            name, sequence = line.strip().split(" ")
            known_sequences[name] = sequence

    print(f'{known_sequences=}')

    with open("unknown_sequences.txt", "r") as myfile:
        lines = myfile.readlines()

        for line in lines:
            unknown_sequence = line.strip()
            found = False

            for key, value in known_sequences.items():
                if unknown_sequence in value:
                    print(f"Unknown sequence '{unknown_sequence}' found in '{key}'.")
                    found = True
                    break

            if not found:
                print(f"Unknown sequence '{unknown_sequence}' NOT found in known sequences.")

if __name__ == "__main__":
    main( )