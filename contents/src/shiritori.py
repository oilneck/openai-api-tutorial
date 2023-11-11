import funcs

def shiritori(start_word:str, n:int=5):

    CMD1 = 'What animal is this? Please answer in a single word.'
    CMD2 = lambda word: f"Please answer with the name of an animal that starts \
                        with the last letter of 「{word}, in a single word."
    word = start_word

    for i in range(n):
        path2img = lambda i, word: f'./../data/image{i}_{word}.jpg'

        funcs.text2image(word, path2img(i, word))
        word = funcs.image2text(path2img(i, word), CMD1)
        word = funcs.chat(CMD2(word))
        print(word)

shiritori('dog')