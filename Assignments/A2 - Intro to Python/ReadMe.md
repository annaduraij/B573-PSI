# A2 - PDA (Parse, Display, Analyze)

## Script Information

- **Name**: Jay Annadurai
- **Title**: A2 - SeqReader
- **Date**: 4 Feb 2024
- **Language**: Python
- **Project Version**: 1.1

## Description

"A2 - SeqReader" is a Python script designed to process DNA sequences from FASTA files, focusing on tasks such as reading sequences, calculating base compositions per kilobase, generating reverse complements, and analyzing nucleotide distributions. It provides functionalities to parse sequence data, display specific nucleotide positions, and perform comprehensive analyses on DNA sequences. This script facilitates detailed genomic analysis and supports bioinformatics research by offering an efficient way to handle and interpret sequence data.

## Requirements

### Hardware

- **Standard PC or Server**: Compatible with systems capable of running Python.

### Software and Libraries

- **Python 3.x**: Ensure Python is installed on your system.
- **No External Libraries Required**: This script uses standard Python libraries only.

### Running the Script

1. **Python Installation**: Verify Python 3.x is installed by running `python --version` or `python3 --version`.
2. **Script Permissions**: Not applicable for Python scripts but ensure the script is accessible.
3. **Directory Permissions**: Ensure the script and FASTA files are in directories where you have read/write permissions.
4. **Input File**: Place the FASTA file in the Data directory as specified in the script and adjust the sequence filepath within the script to match.
5. **Execution**: Run the script using `python JA-SeqReader.py` or `python3 JA-SeqReader.py` from the terminal.


### Modifications for Non-UNIX Systems

This script is platform-independent but ensure Python 3.x is installed and the command line or terminal is properly set up for Python scripts execution.

### Input Files

- **FASTA File**: A `.fa` or `.fasta` file containing the DNA sequence to be analyzed. Ensure the file path and name in the script matches the location of your FASTA file.

### Output (Generated) Files

- **Console Output**: Displays the requested analysis results, such as specific nucleotide positions, reverse complement sequence portions, and nucleotide counts per kilobase.
- **No External Output Files**: All results are printed to the console. Modify the script if file output is required.

## Key Functions and Usage

1. **Reading FASTA Files**: Skips headers and concatenates sequence lines.
2. **Displaying Nucleotide Positions**: Specific functions to extract and display nucleotide positions.
3. **Generating Reverse Complements**: Creates reverse complements of sequences to explore Watson-Crick base pairing.
4. **Analyzing Nucleotide Distribution**: Breaks down sequences into kilobases and calculates nucleotide frequencies.

## Notes

- **Script Adaptability**: Can be modified to analyze different sequences or extended to include additional functionalities such as sequence alignment or mutation detection.
- **Performance Considerations**: For very large sequences, consider optimizing file reading and processing to accommodate system memory limits.
