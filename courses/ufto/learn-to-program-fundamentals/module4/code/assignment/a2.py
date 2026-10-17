def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    ocurrences = 0
    for n in dna:
        if nucleotide == n:
            ocurrences = ocurrences + 1
    return ocurrences

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.find(dna2) != -1


def is_valid_sequence(dna):
    """ (str) -> bool
    Return True if and ony if DNA sequence is valid (that is, it contains no characters other than 'A', 'T', 'C' and 'G')

    >>> is_valid_sequence('AVXGTHA')
    False
    >>> is_valid_sequence('ATCGACT')
    True
    >>> is_valid_sequence('AAAAAAA')
    True
    >>> is_valid_sequence('atgcha')
    False
    """
    is_valid = True
    for nucleotide in dna:
        if not nucleotide in ('ATCG'):
            is_valid = False
            break
    return is_valid


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    Return the DNA sequence obteined by inserting the second DNA sequence into the first DNA sequence at the given index

    >>> insert_sequence('CCGG','AT', 2)
    CCATGG
    >>> insert_sequence('CCGATA','CC', -1)
    CCGATCCA
    >>> insert_sequence('ATCGTA','GA', 0)
    GAATCGTA
    """
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """ (str) -> str
    Return the nucleotide's compliment. If 'A' retuns 'T', if 'T' returns 'A', if 'C' returns 'G' and if 'G' returns 'C'

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return complement[nucleotide]

def get_complementary_sequence(dna):
    """ (str) -> str
    Return the DNA sequence that is complementary to the given DNA sequence

    >>> get_complementary_sequence("ATCGATG")
    "TAGCTAC"
    >>> get_complementary_sequence("CCTGACCG")
    "GGACTGGC"
    """
    complementary = ""
    for nucleotide in dna:
        complementary = complementary + get_complement(nucleotide)
    return complementary
