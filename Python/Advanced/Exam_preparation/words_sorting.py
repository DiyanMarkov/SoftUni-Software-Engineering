def words_sorting(*args):
    words = {}
    for word in args:
        current_sum = 0
        for l in word:
            current_sum += ord(l)

        words[word] = current_sum

    if sum(words.values()) % 2 != 0:
        return "\n".join([f"{x} - {v}" for x,  v in sorted(words.items(), key=lambda x: -x[1])])


    else:
        return "\n".join([f"{x} - {v}" for x,  v in sorted(words.items(), key=lambda x: x[0])])



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))