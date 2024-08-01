import argparse
import sys

def extract_specific_taxa_sequences(input_file, output_file, summary_file, target_taxon):
    """
    Extracts sequences from a FASTA file that belong to a specific taxon.

    Parameters:
        input_file (str): Path to the input FASTA file.
        output_file (str): Path to the output file.
        summary_file (str): Path to the summary file.
        target_taxon (str): The taxon to search for.

    Returns:
        None
    """
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile, open(summary_file, 'w') as summaryfile:
            current_sequence = ''
            current_header = ''
            count = 0
            sequence_names = []

            for line in infile:
                line = line.strip()
                if line.startswith('>'):
                    # Header line
                    if current_sequence and target_taxon in current_header:
                        # Write the sequence to the output file for the previous taxon
                        outfile.write(f"{current_header}\n{current_sequence}\n")
                        count += 1
                        sequence_names.append(current_header.split(' ')[0][1:])  # Extract the sequence name

                    # Reset for the new sequence
                    current_sequence = ''
                    current_header = line  # Store the entire header line
                else:
                    # Sequence line
                    current_sequence += line

            # Process the last sequence in the file
            if current_sequence and target_taxon in current_header:
                outfile.write(f"{current_header}\n{current_sequence}\n")
                count += 1
                sequence_names.append(current_header.split(' ')[0][1:])  # Extract the sequence name

            # Write summary file
            summaryfile.write(f"Number of sequences found: {count}\n")
            summaryfile.write("Names of the sequences:\n")
            for name in sequence_names:
                summaryfile.write(f"{name}\n")
    
    except FileNotFoundError:
        sys.stderr.write(f"Error: The file '{input_file}' was not found.\n")
    except IOError:
        sys.stderr.write(f"Error: An I/O error occurred while processing the file '{input_file}'.\n")
    except Exception as e:
        sys.stderr.write(f"An unexpected error occurred: {str(e)}\n")

def main():
    parser = argparse.ArgumentParser(description='Extract sequences belonging to a specific taxon from a FASTA file.')
    parser.add_argument('-f', '--input_file', type=str, required=True, help='Path to the input FASTA file containing sequences with taxonomic information in headers.')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='Path to the output file where sequences of the specified taxon will be written.')
    parser.add_argument('-s', '--summary_file', type=str, required=True, help='Path to the summary file where the count and names of the sequences will be written.')
    parser.add_argument('-t', '--target_taxon', type=str, required=True, help='The taxon to search for in the headers of the input sequences.')

    args = parser.parse_args()

    extract_specific_taxa_sequences(args.input_file, args.output_file, args.summary_file, args.target_taxon)

    # Show how to use the script if the user provides incorrect arguments or needs help
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
