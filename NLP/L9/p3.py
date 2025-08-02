from nltk.chat.util import Chat 

conv = [
    ["hi|hello|hey",["hi","hello","hey", "how can i help you"]],
    ["batches|courses",["python","java","js"]],
    ["location|address",["thane/borivali"]],
    ["thane|thane location| thane address",["404, ishan arcade-2, thane west"]]
]

chat = Chat(conv)
print("welcome to kc --> chityy, enter your question and press q for quit")
while True:
    qts = input("qts --> " )
    if qts == "q":
        print("chitty --> bye ")
        break
    elif chat.respond(qts) == None:
        print("chitty --> srry i dont understand")
    else:
        print("chitty --> ", chat.respond(qts))

