def searchfunc(word_list, user_word):
    temp_result = False
    for word in word_list:
        if user_word == word:
            temp_result = True
        else:
            pass
    if temp_result == True:
        return True
    else:
        return False

textfile = open('usa_words.txt', 'r')
word_list = textfile.read().split('\n')

while 1 ==1:
    user_word = input('Enter a word: ')

    result = searchfunc(word_list, user_word)
    if result == True:
        print('Your Word is valid')
    elif result == False:
        print('Your Word isn\'t on the list or is mispelled')

    user_resp = input('Try another word Y or N: ')
    if user_resp == 'Y':
        pass
    elif user_resp == 'N':
        break






