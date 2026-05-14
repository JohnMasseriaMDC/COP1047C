def load_known_sequences(filename):
    names = []
    sequences = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # skip empty lines
                parts = line.strip().split(maxsplit=1)
                if len(parts) == 2:
                    name, sequence = parts
                    names.append(name)
                    sequences.append(sequence)
    return names, sequences

def search_unknowns(known_names, known_sequences, unknown_file):
    with open(unknown_file, 'r') as file:
        for line in file:
            unknown = line.strip()
            if not unknown:
                continue  # skip empty lines
            found = False
            for i in range(len(known_sequences)):
                if unknown in known_sequences[i]:
                    print(f"Unknown sequence '{unknown}' found in '{known_names[i]}'.")
                    found = True
                    break
            if not found:
                print(f"Unknown sequence '{unknown}' NOT FOUND in any known sequence.")

def main():
    known_names, known_sequences = load_known_sequences("known_sequences.txt")
    search_unknowns(known_names, known_sequences, "unknown_sequences.txt")

if __name__ == "__main__":
    main()

