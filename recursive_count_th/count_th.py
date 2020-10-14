'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    th_wordies = word.find('th')
    if th_wordies == -1:
        return 0
    return 1 + count_th((word[th_wordies + 2:]))
    
    # TBC
    
    pass
