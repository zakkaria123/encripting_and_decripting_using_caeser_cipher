def caeser_cipher():
    user_input=''
    while user_input !='no':
        encript=input('Encript/Decript: ').upper()
        word=input('Enter word: ').upper()
        result=''
        key=input('enter Key: ')
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        try:
            key=int(key)
            if encript=='ENCRIPT':
                for i in word:
                    if i.isalpha():
                        value=alphabet.index(i)
                        value+=key
                        value%=26
                        result+=alphabet[value]
                    else:
                        result+=i
                print('encripted data: ',result)
            elif encript=='DECRIPT':
                for i in word:
                    if i.isalpha():
                        value=alphabet.index(i)
                        value-=key
                        if value<0:
                            value+=26
                            result+=alphabet[value]
                        else:
                            result+=alphabet[value]
                    else:
                        result+=i
                print('decripted data: ',result)
            else:
                print('enter correct spelling of encript/decript')
            user_input=input('play again: ')
        except:
            print('opps!! key must be an integer only')
    print('\n******************************')
    print('thanks for viewing caeser cipher by ZACK')
