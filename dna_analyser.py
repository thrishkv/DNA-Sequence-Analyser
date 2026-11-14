# Validates a DNA sequence by checking for invalid characters and making sure it is not empty.
def validate_sequence(sequence):
    # Remove any whitespace and convert the sequence to uppercase.
    sequence = sequence.strip().upper()

    # Reject an empty sequence.
    if not sequence:
        raise ValueError("DNA sequence cannot be empty.")

    # Define the valid nucleotide bases for DNA.
    valid_bases = "ACGT"

    # Check each character in the sequence to ensure it is a valid nucleotide.
    for base in sequence:
        if base not in valid_bases:
            raise ValueError(f"Invalid DNA nucleotide: {base}")

    # Return the validated sequence for further processing.
    return sequence


# Counts how many times each nucleotide appears in the sequence.
def count_nucleotides(sequence):
    # Validate the sequence before processing it.
    sequence = validate_sequence(sequence)

    # Create a dictionary to store the count of each nucleotide.
    counts = {"A": 0, "C": 0, "G": 0, "T": 0}

    # Increment the count for each nucleotide found in the sequence.
    for base in sequence:
        counts[base] += 1

    # Return the completed nucleotide counts.
    return counts


# Calculates the length of the DNA sequence.
def sequence_length(sequence):
    # Validate the sequence before calculating its length.
    sequence = validate_sequence(sequence)

    # Return the number of nucleotides in the sequence.
    return len(sequence)


# Calculates the percentage of nucleotides in the sequence that are either guanine (G) or cytosine (C).
def gc_content(sequence):
    # Get the number of each nucleotide in the sequence.
    counts = count_nucleotides(sequence)

    # Calculate the total length of the sequence.
    length = sequence_length(sequence)

    # Add together the number of guanine (G) and cytosine (C) bases.
    gc_count = counts["G"] + counts["C"]

    # Divide the number of G and C bases by the total length
    # then multiply by 100 to convert the result into a percentage.
    return (gc_count / length) * 100


# Produces the reverse complement of a DNA sequence by replacing each nucleotide with its complementary base and reversing the order of the sequence.
def reverse_complement(sequence):
    # Validate the sequence before generating its reverse complement.
    sequence = validate_sequence(sequence)

    # Define the complementary base pairs for DNA.
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    # Create an empty string to store the complementary sequence.
    complementary_sequence = ""

    # Replace each nucleotide in the original sequence with its complementary base.
    for base in sequence:
        complementary_sequence += complement[base]

    # Reverse the complementary sequence to produce the final reverse complement and return it.
    return complementary_sequence[::-1]


# Converts a DNA sequence into an mRNA sequence by replacing thymine (T) with uracil (U).
def transcribe_dna(sequence):
    # Validate the sequence before transcribing it into mRNA.
    sequence = validate_sequence(sequence)

    # Replace thymine (T), found in DNA, with uracil (U), found in RNA.
    return sequence.replace("T", "U")


# Repeatedly asks the user for a DNA sequence until a valid one is provided, then returns the validated sequence.
def get_valid_sequence():
    while True:
        # Ask the user to input a DNA sequence, specifying the valid nucleotide bases.
        dna_sequence = input("\nEnter a DNA sequence (A, C, G, T): ")

        try:
            # Validate the input and return it if it is valid.
            return validate_sequence(dna_sequence)

        # Handle invalid input by displaying an error message and prompting the user to try again.
        except ValueError as error:
            print(f"Invalid input: {error}")
            print("Please try again.")


# Displays all the available analyses for a given DNA sequence, including nucleotide counts, sequence length, GC content, reverse complement, and mRNA transcription.
def display_all_results(sequence):
    # Display a heading and the original DNA sequence.
    print("\n--- DNA Sequence Analysis ---")
    print("DNA sequence:", sequence)

    # Display the total number of nucleotides.
    print("Sequence length:", sequence_length(sequence))

    # Display the count of each individual nucleotide.
    print("\nNucleotide counts:")
    counts = count_nucleotides(sequence)

    # Loop through A, C, G, T in order to display their counts in a consistent format.
    for base in "ACGT":
        print(f"{base}: {counts[base]}")

    # Display GC content rounded to two decimal places.
    print(f"\nGC content: {gc_content(sequence):.2f}%")

    # Display the reverse complement and transcribed mRNA sequence.
    print("Reverse complement:", reverse_complement(sequence))
    print("mRNA transcription:", transcribe_dna(sequence))


# Contains the main menu for the DNA Sequence Analyser program, allowing users to select analyses and input DNA sequences.
def main():
    # Welcome the user to the DNA Sequence Analyser program.
    print("Welcome to the DNA Sequence Analyser!")

    # Keep displaying the menu until the user chooses to exit.
    while True:
        print("\n--- Main Menu ---")
        print("1. Count nucleotides")
        print("2. Sequence statistics")
        print("3. Reverse complement")
        print("4. DNA transcription to mRNA")
        print("5. Run all analyses")
        print("0. Exit")

        # Read the user's menu choice and remove surrounding whitespace.
        choice = input("Choose an option: ").strip()

        # Exit the program if the user selects option 0.
        if choice == "0":
            print("Thank you for using the analyser!")
            break

        # Reject menu options that are not valid and prompt the user to try again.
        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid menu option. Please try again.")
            continue

        # Ask for a valid DNA sequence from the user before performing any analysis.
        dna_sequence = get_valid_sequence()

        # Option 1: display the count of each nucleotide.
        if choice == "1":
            print("\nNucleotide counts:")
            counts = count_nucleotides(dna_sequence)

            # Display the nucleotide counts in A, C, G, T order.
            for base in "ACGT":
                print(f"{base}: {counts[base]}")

        # Option 2: display the sequence length and GC content.
        elif choice == "2":
            print("\nSequence statistics:")
            print("Length:", sequence_length(dna_sequence))
            print(f"GC content: {gc_content(dna_sequence):.2f}%")

        # Option 3: display the reverse complement.
        elif choice == "3":
            print("Reverse complement:", reverse_complement(dna_sequence))

        # Option 4: transcribe the DNA sequence into mRNA.
        elif choice == "4":
            print("mRNA sequence:", transcribe_dna(dna_sequence))

        # Option 5: display every available analysis.
        elif choice == "5":
            display_all_results(dna_sequence)


# Run main() only when this file is executed directly
if __name__ == "__main__":
    main()
    