def english_caesar(str):
    d = {
        'A' : 'z',
        'B' : 'y',
        'C' : 'x',
        'D' : 'w',
        'E' : 'v',
        'F' : 'u',
        'G' : 't',
        'H' : 's',
        'I' : 'r',
        'J' : 'q',
        'K' : 'p',
        'L' : 'o',
        'M' : 'n',
        'N' : 'm',
        'O' : 'l',
        'P' : 'k',
        'Q' : 'j',
        'R' : 'i',
        'S' : 'h',
        'T' : 'g',
        'U' : 'f',
        'V' : 'e',
        'W' : 'd',
        'X' : 'c',
        'Y' : 'b',
        'Z' : 'a',
        'a' : 'Z',
        'b' : 'Y',
        'c' : 'X',
        'd' : 'W',
        'e' : 'V',
        'f' : 'U',
        'g' : 'T',
        'h' : 'S',
        'i' : 'R',
        'j' : 'Q',
        'k' : 'P',
        'l' : 'O',
        'm' : 'N',
        'n' : 'M',
        'o' : 'L',
        'p' : 'K',
        'q' : 'J',
        'r' : 'I',
        's' : 'H',
        't' : 'G',
        'u' : 'F',
        'v' : 'E',
        'w' : 'D',
        'x' : 'C',
        'y' : 'B',
        'z' : 'A'
    }
    res = ''
    for c in str:
        if c in d:
            res += d[c]
        else:
            res += c
    res += " (Have fun!)"
    return res
