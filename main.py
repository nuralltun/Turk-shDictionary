dictionary={
    "this": [("zamir", "Bu, Şu")],
    "is": [("fiil", "Olmak")],
    "a": [("belirteç", "Bir")],
    "book":[ ("isim", "Kitap"), ("fiil", "Rezerve etmek")],
    "pen": [("isim", "Kalem")]
}

while True:
    sentence = input ("Bir cümle giriniz: (Çıkmak için ENTER'a basınız)")
    if sentence == "":
        break

    for signCharacter in ".!?,=:-)(":
        sentence = sentence.replace(signCharacter, '')

    words = set(sentence.lower().split())

    wordsMaxLength = 1
    for word in words:
        if wordsMaxLength < len(word):
            wordsMaxLength = len(word)

    for word in words:
        wordDefinitions = dictionary.get(word, "[ANLAMI BULUNAMADI]")
        if len(wordDefinitions) == 1:
            print(f'{word.upper():<{wordsMaxLength}} : ({wordDefinitions[0][0]:^8}) {wordDefinitions[0][1]}')
        elif len(wordDefinitions) > 1:
            print(f'{word.upper():<{wordsMaxLength}} : ', end='')
            for wordDefinition in wordDefinitions:
                print(f'({wordDefinition[0]}) {wordDefinition[1]}   ',end='')
                print()

    print()
print("Kullanıcı çıkışı.")

