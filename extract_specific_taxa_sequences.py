"""
extract_specific_taxa_sequences.py

This script extracts sequences from a FASTA file that belong to a specific taxon and writes them to a new file.

Usage:
    python extract_specific_taxa_sequences.py

Parameters:
    input_file (str): Path to the input FASTA file containing sequences with taxonomic information in headers.
    output_file (str): Path to the output file where sequences of the specified taxon will be written.
    target_taxon (str): The taxon to search for in the headers of the input sequences.

Example:
    python extract_specific_taxa_sequences.py --input_file your_input.fasta --output_file output_rhizobium.fasta --target_taxon Rhizobium
"""

def extract_specific_taxa_sequences(input_file, output_file, target_taxon):
    """
    Extracts sequences from a FASTA file that belong to a specific taxon.

    Parameters:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output file.
        target_taxon (str): The taxon to search for.

    Returns:
        None
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_sequence = ''
        current_taxon = ''

        for line in infile:
            line = line.strip()
            if line.startswith('>'):
                # Header line
                if current_sequence and target_taxon in current_taxon:
                    # Write the sequence to the output file for the previous taxon
                    outfile.write(f">{current_taxon}\n{current_sequence}\n")

                # Reset for the new sequence
                current_sequence = ''
                current_taxon = line.split(';')[-1].strip()  # Extracting the taxon from the header
            else:
                # Sequence line
                current_sequence += line

        # Process the last sequence in the file
        if current_sequence and target_taxon in current_taxon:
            outfile.write(f">{current_taxon}\n{current_sequence}\n")

# Example usage
fasta_input_file = 'your_input.fasta'
output_file_for_specific_taxon = 'output_rhizobium.fasta'
target_taxon = 'Rhizobium'

extract_specific_taxa_sequences(fasta_input_file, output_file_for_specific_taxon, target_taxon)
