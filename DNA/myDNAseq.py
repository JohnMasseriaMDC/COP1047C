# This code is part of myDNAseq.py and is used to compare known DNA sequences with unknown ones.
# It reads known sequences from a file, checks each unknown sequence against them,
# and prints whether each unknown sequence is known or not, along with its name if it is known.
# The code uses lists to store names and sequences, and it reads from two text files.
names = []
known_sequences = []

with open("known_sequences.txt", "r") as file:
    for line in file:
        name, sequence = line.strip().split()
        names.append(name)
        known_sequences.append(sequence)

with open("unknown_sequences.txt", "r") as file:
    for line in file:
        seq = line.strip()
        for sequence in known_sequences:
            if seq in sequence:
                index = known_sequences.index(sequence)
                print(f"Sequence '{seq}' is known as '{names[index]}'.")
                break
        else:
            print(f"Sequence '{seq}' is unknown.")
