def dyvo_insert(s, flag):
    """
    str, str -> str
    We must insert "диво" before every word which start with flag.\
    if sentence and flag is not str - return None.
    >>> dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті', 'ки')
    'дивоКит кота по хвилях катав - дивокит у воді, кіт на дивокиті'
    >>> dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті', 3)
    >>> dyvo_insert('Босий хлопець сіно косить, роса росить ноги босі.', 'сі')
    'Босий хлопець дивосіно косить, роса росить ноги босі.'
    """
    if isinstance(s, str) and isinstance(flag, str):
        s = " " + s
        if flag.isupper():
            flag_lower = flag.lower()
            flag_upper = flag

        if flag.islower():
            flag_upper = flag.title()
            flag_lower = flag

        s = s.replace(' ' + flag_upper,  " диво"+flag_upper)
        s = s.replace(' ' +flag_lower, " диво"+flag_lower)
        return s[1:]
    return None
if __name__=="__main__":
    import doctest
    print(doctest.testmod())