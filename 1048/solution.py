def find_middle_person(s_ab, s_ac, s_bc):
    """""
    Finds the middle brother (second oldest) among three brothers A, B, and C,
    given their age relationships.

    Args:
        s_ab: Character representing the age relationship between A and B ('<' or '>').
        s_ac: Character representing the age relationship between A and C ('<' or '>').
        s_bc: Character representing the age relationship between B and C ('<' or '>').

    Returns:
        The letter representing the middle brother ('A', 'B', or 'C').
    """

    ages = {'A': 0, 'B': 0, 'C': 0}

    if s_ab == '<':
        ages['A'] += 1
    else:
        ages['B'] += 1

    if s_ac == '<':
        ages['A'] += 1
    else:
        ages['C'] += 1

    if s_bc == '<':
        ages['B'] += 1
    else:
        ages['C'] += 1

    for brother, age in ages.items():
        if age == 1:
            return brother


