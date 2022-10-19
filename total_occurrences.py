def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    >>> total_occurrences(1, [1, 2], 'b')
    """
    if isinstance(s1, str) and isinstance(s2, str) and isinstance(ch, str):
        list_s1 = list(s1)
        list_s2 = list(s2)
        count_ch = list_s1.count(ch) + list_s2.count(ch)
        return count_ch
    return None

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())