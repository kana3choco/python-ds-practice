def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    friend1_hobby_set = set(a[2])
    friend2_hobby_set = set(b[2])
    if friend1_hobby_set & friend2_hobby_set:
        return True
    return False

# elmo = ('Elmo', 5, ['hugging', 'being nice'])
# sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
# gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])