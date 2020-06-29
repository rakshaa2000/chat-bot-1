import spacy
spacy.load("en_core_web_sm")
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
 
#creating a new chatbot
chatbot = ChatBot('Groceria')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer1= ListTrainer(chatbot)
 
#getting a response from the chatbot
trainer.train(
    "chatterbot.corpus.english.greetings"
)
response = chatbot.get_response("Hello")
print(response)
print("Please type: 'Take my order' to order or 'I want to see my order' to view order")
items=[]
while(True):
    user=input()
    if(user!='I am done, Thank you.'):
        if(user=='Take my order'):
            print("Sure thing, what do you need?")
            item=input()
            items.append(item)
            #print('Adding to your basket. Anything else?')
            while item!="That is all.":
                print('Adding to your basket. Anything else?')
                item=input()
                items.append(item)
            print('Thank you for using our service')
        elif(user=='I want to see my order'):
            print("Sure thing, What is your order number")
            num=int(input())
            print('Thank you for using our service')
        else:
            print(chatbot.get_response(user))
    else:
        break
