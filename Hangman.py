
import random,re
from hangmanImage import image
from time import sleep, strftime

alph=[chr(i) for i in range(97,97+26)]  #list of small alphabet





def compword():     #funtion -- computer create a 8 letter word
    c_word=""
    for i in range(8):
        ran=random.randint(0,26)
        c_word+=alph[ran-1]+' '
    return c_word


def update(o,ii,cc):  # funtion ---- update the result list 
    a=list(o)
    for i in range(len(o)):
        if cc[i]==ii:
            a[i]=ii  
    o=''
    for i in a:
        o+=str(i)
    return o



def game_rules():   # to show game rules 
    print('''
    1. Computer ne 8 leeter ka ek word generate kiya apko us word ko letter by letter guess karna h.
    2. Apko letter guess karna h . Shi letter guess karne per wo letter apne word ke shi place per show karne lagega.
    3. Agar apka letter galt h to apne total 8 life line mese ek loss kar doge aur aap ek man hoga jo rope pe hang hona suru ho jayega.
    4. Apko life line rehte hua use word  ke sabhi lette ko guess karna aour appne man ko hang hone se bachana h. 
    5. Agar aap guess kar paye to ap WINNNER honge nhi to aap game LOSS kar denge .
    ''')

print("\n########------------------------------------------WELCOME TO HANGMAN GAME ---------------------------------------########\n\n")

def manu():


    a=int(input('\n-------READY FOR PLAY..................\n\n   1. START\n   2. RULES\n   3. EXIT   :'))  #manu choice
    print()
    if a==1:
    
        cWord=compword()            #computer generate the the words
        print('LETs START\ncomputer genrating the word')
        sleep(2)
        print('Computer genrated  the word.....\n\n')

        ll=["_ " for f in range(8)]        #blank result list
        oo=""
        for t in ll:
            oo+=t


        print(cWord)
        print()
        lifeuse=0
        liferem=8


        while liferem>=0:
            print(f'you have {liferem} life line remain.                            complet the word  ------    {oo}\n')
            


            if lifeuse>0:              #GAME OVER SIGNAL  WHEN YOU LOSS
                doSomething = getattr(image, f'img{lifeuse}')
                doSomething()
                if liferem==0:
                    print("\n--------GAME OVER---------\n---YOU LOSS.............\n")
                    break
                
            gs=input('pls.. guess the letter of word : ').lower()  #guess letter
            


            if gs in cWord  :
                if gs not in oo:
                    print('\n correct guess--..')
                    oo=update(oo,gs,cWord)
                   
                    if oo==cWord:
                        print('congratulation you win..        you completed the word-----  ',oo)
                        break
                    sleep(1)
                else:
                    print('you chossen it .  pls.. tyr another letter ...')
                    continue
            else:
                print('Wrong guess ..')
                sleep(1)
                lifeuse+=1
                liferem-=1

            
            print()

    elif a==2:
        game_rules()
        while True:
            back=input('Press b to go back : ')
            if back=="b":
                return manu()
            


    else:
        print(" Ok bye.........\n see you next time ........")
manu()
  
