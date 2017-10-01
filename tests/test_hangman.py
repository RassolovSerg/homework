from Hangman import hangman

def test_hangman():
    assert hangman.check_letter('h','hovanskiy',['h', 'o', 'v', 'a', 'n', 's', 'k', 'i', 'y'],0,[]) == (0, ['h'])
    assert hangman.check_letter('a','tinkoff',['t', 'i', 'n', 'k', 'o', 'f'],0,[]) == (1, [])
    a,b = hangman.choose_word()
    assert (len(a)<=len(b))