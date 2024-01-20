mclang = {    
    "A": "ᔑ",
    "B": "ʖ",
    "C": "ᓵ",
    "D": "↸",
    "E": "ᒷ",
    "F": "⎓",
    "G": "⊣",
    "H": "⍑",
    "I": "╎",
    "J": "⋮",
    "K": "ꖌ",
    "L": "ꖎ",
    "M": "ᒲ",
    "N": "リ",
    "O": "𝙹",
    "P": "!¡",
    "Q": "ᑑ",
    "R": "∷",
    "S": "ᓭ",
    "T": "ℸ",
    "U": "⚍",
    "V": "⍊",
    "W": "∴",
    "X": "̇/",
    "Y": "||",
    "Z": "⨅",
}

def mcelTranslate(message): 
    userInput = message
    output = ""
    for c in userInput:
        mcChar = mclang.get(c.upper())
        output = output + mcChar
    return output