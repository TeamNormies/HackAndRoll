def english_to_uwu(str):
    # replace "r" and "l" with "w"
    str = str.replace("r", "w")
    str = str.replace("l", "w")
    # replace "n" with "ny"
    str = str.replace("n", "ny")
    # replace "th" with "d
    str = str.replace("th", "d")
    # add uwu after each exclamation mark
    str = str.replace("!", "!uwu")
    return str
