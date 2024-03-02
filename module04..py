def find_max_vowels(text):
    vowels = 'aeiouy'

    for character in text:
        if character.lower() not in vowels:
            text = text.replace(character, ".")

    chains = text.split(".")
    chains.sort(key=len)
    max_chain = chains[-1]
    return max_chain, len(max_chain)

text = 'aefdsfe yiawussd awwfhkeeasdd Oleeeeekuuyu'

chain, l = find_max_vowels(text)
print(chain, ":", l)






def is_flush(cards):
    res = set()
    for card in cards:
        mark = card[-1]
        res.add(mark)
        


    return len(res) == 1




cards = ["AD", "4S", "7H", "KS", "10S"]
is_flush(cards)
print(is_flush(cards))