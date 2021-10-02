
# import random,re
# from hangmanImage import image
# from time import sleep, strftime

# alph=[chr(i) for i in range(97,97+26)]  #list of small alphabet
# # print(alph)



#ok

# def compword():     #funtion -- computer create a 8 letter word
#     c_word=""
#     for i in range(8):
#         ran=random.randint(0,26)
#         # print(ran)
#         c_word+=alph[ran-1]
#     return c_word

# def update(l,o,ii):  # funtion ---- update the result list 
#     # for i in l:
#     #     o+=i
    
#     return o



# def game_rules():   # to show game rules 
#     print('''
#     1. Computer ne 8 leeter ka ek word generate kiya apko us word ko letter by letter guess karna h.
#     2. Apko letter guess karna h . Shi letter guess karne per wo letter apne word ke shi place per show karne lagega.
#     3. Agar apka letter galt h to apne total 8 life line mese ek loss kar doge aur aap ek man hoga jo rope pe hang hona suru ho jayega.
#     4. Apko life line rehte hua use word  ke sabhi lette ko guess karna aour appne man ko hang hone se bachana h. 
#     5. Agar aap guess kar paye to ap WINNNER honge nhi to aap game LOSS kar denge .
#     ''')

# print("\n########------------------------------------------WELCOME TO HANGMAN GAME ---------------------------------------########\n\n")

# def manu():
#     a=int(input('\n-------READY FOR PLAY..................\n\n   1. START\n   2. RULES\n   3. EXIT   :'))
#     print()
#     if a==1:
#         sleep(2)
#         cWord=compword()
#         print('LETs START')
#         sleep(2)
#         print('Computer created the word.....\n')

#         ll=["_ " for f in range(len(cWord))]  #blank result list
#         oo=""
#         for t in ll:
#             oo+=t


#         print(cWord)
#         print()
#         lifeuse=0
#         liferem=8
#         co={}
#         while liferem>=0:
#             print(f'you have {liferem} life line remain.                            Right word {oo}\n')
#             print(lifeuse)


#             if lifeuse>0:              #GAME OVER SIGNAL
#                 doSomething = getattr(image, f'img{lifeuse}')
#                 doSomething()
#                 if liferem==0:
#                     print("\n--------GAME OVER---------\n---YOU LOSS.............\n")
#                     break
        
#             gs=input('pls.. guess the letter : ')
#             print(gs,cWord)


#             if gs in cWord:
#                 ll,oo=update(ll,oo,gs)
                
#             else:
#                 print('Wrong guess ..')
#                 lifeuse+=1
#                 liferem-=1

            
#             print()

#     elif a==2:
#         game_rules()
#         while True:
#             back=input('Press b to go back : ')
#             if back=="b":
#                 return manu()
            


#     else:
#         print(" Ok bye.........\n see you next time ........")
# manu()








# # f cWord.count(gs)>1:
# #                     try:
# #                         a=co[gs]
# #                     except:
# #                         co[gs]=1
# #                         for i in range(a+1):
# #                             if i==a:
# #                                 gs=cWord[i]

# #                                 ind=cWord.index(f'{gs}')
# #                                 ll[ind]=gs
# #                                 oo=''
# #                                 for t in ll:
# #                                     oo+=t
# #                                 print(co)
# #                                 # co[gs]=co[gs]+1

# #                 else:
# #                     ind=cWord.index(f'{gs}')
# #                     ll[ind]=gs
# #                     oo=''
# #                     for t in ll:
# #                         oo+=t
# #                     co[gs]=1
# #                 print(co)
# #                 # oo=update(ll,oo,ind)
# #                 # print(f' Right word {oo}')
a=list(range(1,3))
print(a)