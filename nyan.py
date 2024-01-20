import string
import random

nyanlang = {
    "hello" : "nyanayn",
    "hi" : "nyanayn",
    "pain" : "ouchy-nyaouchy",
    "angry" : "hiss",
    "hate" : "hiss",
    "hungry" : "wrrrao",
    "happy" : "purr",
    "you" : "nyu",
    "small" : "tinyi",
    "cute" : "kanyaii",
    "kill" : "scratch nya~",
    "cat" : "nekyon",
    "fight" : "battle of the nya~",
    "no" : "nyo",
    "not" : "mewot",
    "y'all" : "ny'all",
    "the" : "nye",
    "okay" : "oki-doki",
    "ok" : "oki-doki",
    "catgirl" : "nekyongurl",
    "catboy" : "nekyonboi",
    "girl" : "gurl",
    "now" : "maow",
    "good night" : "Nyaight~ Nyaight~",
    "huh" : "nyaa nyaa~",
    "stupid" : "snyupid",
    "sorry" : "sowwy~",
    "kid": "kittyen",
    "child" : "kittyen",
    "children" : "kittyens",
    "please" : "pwease",
    "what" : "meowhat",
    "war" : "nyar~",
    "mistress" : "meowstress",
    "master" : "meowster",
    "mother" : "meowther",
    "mama" : "meowameowa",
    "enough" : "enyagh",
    "can" : "nyan",
    "can't" : "nyan't",
    "year" : "nyear nyof nye nekyons",
    "month" : "meownth",
    "day" : "nayn",
    "night" : "nyight",
    "chips" : "nyips",
    "crisps" : "nyips",
    "die" : "nyie",
    "dying" : "nying",
    "died" : "nyied",
    "perfect" : "nyerfect",
    "perfection" : "nyerfection",
    "!" : "meow~!",
    "?" : "nya~?",
}

def nyan_translate(message):
    if (int(random.random() * 100) >= 69):
        return "Nyan nyu nyimyaginye myean nyimyaginyary mewnnyagerie myanyager myagining myanyaging myean nyimyaginyary mewnnyagerie nya~?"
    words = []
    punctuation_used = []

    for char in message:
        if char in string.punctuation:
            punctuation_used.append(char)
        else:
            words.append(char)

    words = ''.join(words).split()
    output = ""
    for word in words:
        if word.lower() in nyanlang.keys():
            nyan_word = nyanlang.get(word.lower())
        else: 
            nyan_word = word.replace("ma","mya")
            nyan_word = word.replace("na","nya")
            nyan_word = word.replace("me","mewn")

        output = output + " " + nyan_word

    if (len(punctuation_used) != 0):
        nyan_punctuation = nyanlang.get(punctuation_used[-1])
        output = output + " " + nyan_punctuation
    else:
        output = output + " " + "nya~"

    return output

print(nyan_translate("nani"))