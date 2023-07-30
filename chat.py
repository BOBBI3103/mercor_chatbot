#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from nltk.chat.util import Chat, reflections
#print(reflections)
pairs =[
    [r"hi|hello|namaste",
    ["hello","hey there","hi, nice to meet you"]],
   [ r"good morning",
    ["great morning"]],
    [r"i am (.*)",
    ["how are you %1?"]],
    [
        r"what do you do?",
        ["i chat with you"]
    ],
    [
        r"how are you?",
        ["I am fine. What about you"]
    ],
    [
        r"(.*)(good|fine)",
        ["greate to hear","wow that's nice"]
    ],
    
]
def bot():
    print("HI I AM CHATBOT  ......... wHAT IS YOUR NAME")
    chat= Chat(pairs,reflections)
    chat.converse()
if __name__ == "__main__":
    bot()

    
    


# In[ ]:




