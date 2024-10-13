# Extract Specific Taxa Sequences

This script is a Python program that extracts sequences from a FASTA file that belong to a specific taxon and writes them to a new file. It also generates a summary file containing the count and names of the sequences that were extracted. The script accepts command-line arguments for the input file, output file, summary file, and target taxon. The script also includes error handling to provide helpful messages in case of incorrect arguments or other errors.

## Usage 

```sh
python extract_specific_taxa_sequences.py -f <input_fasta_file> -o <output_fasta_file> -s <summary_file> -t <target_taxon>

```
## Example
To extract sequences for the genus Pseudomonas from fasta_db.fasta, and write them to output_Pseudomonas.fasta with a summary in summary.txt, run:


```sh
python extract_specific_taxa_sequences.py -f fasta_db.fasta -o output_Pseudomonas.fasta -s summary.txt -t Pseudomonas
```

Note: The fasta_db.fasta file could be a FASTA database containing 16S rRNA full-length sequences from widely used resources such as SILVA or Greengenes.

## Usage instructions

```sh
optional arguments:
  -h, --help            show this help message and exit
  -f INPUT_FILE, --input_file INPUT_FILE
                        Path to the input FASTA file containing sequences with taxonomic information in headers.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        Path to the output file where sequences of the specified taxon will be written.
  -s SUMMARY_FILE, --summary_file SUMMARY_FILE
                        Path to the summary file where the count and names of the sequences will be written.
  -t TARGET_TAXON, --target_taxon TARGET_TAXON
                        The taxon to search for in the headers of the input sequences.
```

Created by Georgios Leventis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.13874732.svg)](https://doi.org/10.5281/zenodo.13874732)


