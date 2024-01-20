def english_to_owo(str):
    # replace "r" and "l" with "w"
    str = str.replace("r", "w")
    str = str.replace("l", "w")
    # replace "n" with "ny"
    str = str.replace("n", "nya")
    # replace "th" with "d
    str = str.replace("th", "d")
    # add uwu after each exclamation mark
    str = str.replace("!", "!! OwO")
    str += " rawr OwO!"
    return str
