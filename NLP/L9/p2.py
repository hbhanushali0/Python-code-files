#wapp for simple chatbot
conv  = {

    "hi"            :   "hi",
    "hello"         :   "hi",
    "kamal clases"  :   "yes how can i help you",
    "batches"       :   "python/java/js",
    "python"        :   "15th April",
    "timig"         :   "9pm to 11pm",
    "fees"          :   "10620",
    "any discoount" :   "check with other classes",
    "location"      :   "thane/borivali",
    "thane"         :   "404, ishan arcade-2, thane west",
    "borivali"      :   "301, paras business center, borivali east"

}


print("Welcome to kc -> chitty, enter ur question and q for quit")
while True:
    qts = input("qts --> ")
    if qts == "q":
        print("chitty --> bye")
        break
    elif conv.get(qts) == None:
        print("chitty --> sorry i dont understand that pls call 7498405040 ")
    else:
        print("chitty --> ", conv.get(qts))
