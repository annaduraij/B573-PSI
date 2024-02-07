# Establish Metadata
metadata = {
    'Author      ': 'Jay Annadurai',
    'Date        ': '4 Feb 2024',
    'Project     ': 'A2-SeqReader',
    'Version     ': 1.1,
    'Description ': 'Reads a DNA sequence from a FASTA file and gets counts of Bases per Kilobase and answers questions'
}

# Print Metadata
for field in metadata:
    print(str(field) + ": " + str(metadata[field]))


# 1. Open Chromosomal Sequence with Python
def read_file_wo(relative_filepath: str, skipped_character: str) -> str:
    # Function: Read File WithOut
    # Reads a file into a string but skips any lines that start with the skip character
    # Example Usage is for a FASTA header in a sequence file

    # Initialize an empty string to store the concatenated string
    result = ''

    # 'With' is a method to elegantly implement exception handling in resource streams
    with open(relative_filepath, 'r') as file:
        # Iterate through the lines in the file
        for line in file:
            if not line.startswith(skipped_character):
                # Concatenate line into the result string
                # Remove leading/trailing whitespace with strip()
                result += line.strip()

    return result


# Establish the Path of the Sequence File
seq_filepath = "Data/chr1_GL383518v1_alt.fa"

# Read the Sequence File
seq = read_file_wo(seq_filepath, '>')
# print(seq)

# 1a. Print the 10th letter of this sequence.
question = "\n 1a) 10th Letter of Sequence Chr1_GL383518v1"
# Remember, Arrays are 0-Based so 10th letter is index 9
answer = seq[9]
print(question+": \n "+answer)

# 1b. Print the 758th letter of this sequence.
question = "\n 1b) 758th Letter of Sequence Chr1_GL383518v1"
answer = seq[757]
print(question+": \n "+answer)


# 2a.  Write a Python program to create the reverse complement of the encoded DNA molecule used in Part 1.
# Remember to reverse the sequence, and substitute the bases with their Watson-Crick-Franklin pair.

def complementary_sequence(sequence: str, dna=True, reverse=False) -> str:
    # Function intakes a sequence and generates a complementary sequence
    # Outputs either in DNA or RNA bases in straight or reverse directions

    # Create a translation table for DNA complements and RNA complements
    dna_translation_table = str.maketrans('aAtTcCgG', 'tTaAgGcC')
    rna_translation_table = str.maketrans('aAtTcCgG', 'uUaAgGcC')

    # If the Reverse flag is enabled, reverse the sequence using a negative slice
    if reverse:
        sequence = sequence[::-1]

    if dna:
        return sequence.translate(dna_translation_table)
    else:
        return sequence.translate(rna_translation_table)


# Bind the Reverse Complement of Sequence Chr1_GL383518v1
reverse_complement_seq = complementary_sequence(seq, reverse=True)

# 2a. Print the 79th letter of the reverse complementary sequence.
question = "\n 2a) 79th Letter of the Reverse Complement of Sequence Chr1_GL383518v1"
# Remember, Arrays are 0-Based so 79th letter is index 78
answer = reverse_complement_seq[78]
print(question+": \n "+answer)

# 2b. Print the 500th to 800th letters of the reverse complementary sequence.
question = "\n 2b) 500th to 800th Letters of the Reverse Complement of Sequence Chr1_GL383518v1"
# Remember, in Slicing Arrays from string[posA,posB], posA is inclusive and posB is exclusive
answer = reverse_complement_seq[499:800]
print(question+": \n "+answer)

# 3. Read the Original Sequence
# 3a. Create a nested dictionary that contains the number of times each letter appears in the downloaded sequence
#     as a function of which kilobase of the sequence you are looking at.
# HINT: “my_dict”[5000] should contain a dictionary that has a separate key for each of the different nucleotides.
# “my_dict”[5000][“A”] should contain the number of times each A appears in the sequence between pos 5000 and pos 6000.


def interval_splitter(sequence: str, interval_length=1000) -> dict:
    # Splits a Sequence into a Dictionary of Pre-Defined Intervals
    # The Key is the endpoint of the stored interval

    # Initialize the Dictionary
    intervals_dict = {}

    # Start Point of the Interval
    i = 0
    # End Point of the Interval
    j = interval_length

    # Loop to iterate through the Sequence
    while i < len(sequence):

        # If the end point exceeds the max length of the sequence
        # Simply take the remainder of the sequence for that final interval
        if j > len(sequence):
            # Bind the interval under the key of the interval end point
            intervals_dict[str(j)] = sequence[i:len(sequence)]
        else:
            # Bind the interval under the key of the interval end point
            intervals_dict[str(j)] = sequence[i:j]

        # Increment both the start point and the end point by the interval scale to move to the next interval
        i += interval_length
        j += interval_length

    # Return the Intervals Dictionary
    return intervals_dict


def base_reader(sequence: str, dna=True) -> dict:
    # Function to iterate through a DNA or RNA

    # Capitalize the Sequence as to make it Case-Insensitive
    sequence = sequence.upper()

    # Get the count of Kilobases and round up
    # kilobases = (len(sequence)/1000) +

    # For DNA
    if dna:
        bases = {
            'A': 0,
            'C': 0,
            'G': 0,
            'T': 0,
        }
    # For RNA
    else:
        bases = {
            'A': 0,
            'C': 0,
            'G': 0,
            'U': 0,
        }

    # Iterate through the Bases in the Sequence
    for base in sequence:
        # Use whichever base is read as the key to its respective count and increment that count
        bases[base] += 1

    # Return the Dictionary of Bases for the Given Sequence
    return bases


def kilobase_reader(sequence: str, dna=True) -> dict:
    # Function reads the quantity of bases per each kilobase

    # Split the Sequence into Intervals of 1000, i.e. kilobases
    kilobases = interval_splitter(sequence, 1000)

    # Iterate through each kilobase of the sequence
    for kilobase in kilobases:
        # kilobases[kilobase] accesses the sequence with the key of that specific kilobase
        # Overwrite the sequence with the dictionary of base counts under the key of the specific kilobase
        kilobases[kilobase] = base_reader(kilobases[kilobase], dna)

    # Return the dictionary of kilobases with each kilobase containing a dictionary of its base count
    return kilobases


# Bind the Kilobase Reads
kilobase_reads_seq_dict = kilobase_reader(seq, dna=True)
# print(kilobase_reader(seq))

# 4. Write a Python program to read the dictionary in Part 3.

# 4a. Create a list with 4 elements with the count of each nucleotide (A,C,G,T) in the first 1000 base pairs


def dict_to_list(dictionary: dict) -> list:
    # Function to Recursively Convert any Dictionaries into Lists
    temp_list = []

    # Iterate through the Dictionary
    for key in dictionary:
        # Get the Value of the Key-Value pair
        value = dictionary[key]

        # If the value itself is a dictionary, recursively call the same function
        if type(value) is dict:
            value = dict_to_list(value)

        # Append the Value to the List
        temp_list.append(value)

    # Return the Converted List
    return temp_list


# Convert the Kilobase Reads Dictionary into a List and Bind it
kilobase_reads_seq_list = dict_to_list(kilobase_reads_seq_dict)

# 4a. Create a list with 4 elements with the count of each nucleotide (A,C,G,T) in the first 1000 base pairs
question = "\n 4a) Create a list with 4 elements with each nucleotide (A,C,G,T) count in the first 1000 base pairs"
# The first element, index 0, in the list is the Reads of the 1st Kilobase
answer = kilobase_reads_seq_list[0]
print(question+": \n"+str(answer))

# 4b. Repeat part 4a for each kilobase contained in the dictionary.
# 4c. Create a list containing each individual list from the part 4b.
question = "\n 4b/c) Create a list containing each individual list for each kilobase contained in the dictionary"
# The first element, index 0, in the list is the Reads of the 1st Kilobase
answer = kilobase_reads_seq_list
print(question+": \n"+str(answer))

# 4d. Calculate the sum of each list.


def sum_list(list_to_sum: list) -> int:
    # Function to iterate through lists and sum any integers or floats
    temp_sum = 0

    # Iterate through the Elements
    for element in list_to_sum:
        # If the element itself is a list, recursively call the sum_list function and rebind it
        if type(element) is list:
            element = sum_list(element)

        # Only consider the element if it is a number
        if type(element) is int or type(element) is float:
            # Accumulate the element's value into the sum
            temp_sum += element

    # Return the Sum of all numbers within the list
    return temp_sum


def list_of_sums(list_of_lists_to_sum: list) -> list:
    # Function to iterate through the lists of lists and sum the internal lists
    temp_list = []

    # Iterate through the List
    for list_to_sum in list_of_lists_to_sum:
        # Only consider the element if it is a list itself
        if type(list_to_sum) is list:
            # Accumulate the sum of the list
            temp_list.append(sum_list(list_to_sum))

    # Return the new List of Sums
    return temp_list


# 4d. Calculate the sum of each list from part 4b
question = "\n 4d) Calculate the sum of each list from part 4b"
# The first element, index 0, in the list is the Reads of the 1st Kilobase
answer = list_of_sums(kilobase_reads_seq_list)
print(question+": \n"+str(answer))

# 4e. Using comments in your code answer the following questions:

# 4e1. What is the expected sum for each list?
question = "\n 4e1) What is the expected sum for each list?"
answer = "\n The expected sum is 1000 as each list contains the count of the bases A, C, G, T."
answer += "\n If the source sequence for the counts is actually DNA, it will only be comprised of A, C, G, T bases."
answer += "\n In the sequence (1 kilobase), the individual count of A, C, G, T bases should equal the total bases."
print(question+": "+str(answer))

# 4e2. Are there any lists whose sums are not equal to the expected value?
question = "\n 4e2) Are there any lists whose sums are not equal to the expected value?"
answer = "\n All sums are the length in bases of the read sequences and as such do match the expected value."
answer += "\n If the source sequence for the counts is actually DNA, it will only be comprised of A, C, G, T bases."
answer += "\n As such, per 1 kilobase, the count of the individual A, C, G, T bases should equal the total bases."
print(question+": "+str(answer))

# 4e3. Provide a general explanation for the differences in your expected results and your observed results.
question = "\n 4e3) Provide a general explanation for the differences in the expected results and the observed results."
answer = "\n I did not see any inconsistency between the observed and expected results."
print(question+": "+str(answer))

# End of File

# # Unused Function(s):
# def division_round_up(dividend: int, divisor: int) -> int:
#     # int(expression) converts the float to the nearest integer
#     # (remainder > 0) is a boolean that evaluates to true AKA 1 if true
#     # Combination rounds up
#     return int(dividend/divisor) + (dividend % divisor > 0)
