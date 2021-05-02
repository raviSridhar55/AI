from nltk.chat.util import Chat,reflections
pairs = [
         ['hi|hello|hii',['hey there!']],
         ['my name is (.*)', ['how r u %1']],
         ['fine|m fine u',['cool as always']],
         ['(.*) created u?',['Sahil created me']],
         ['(.*) name?',['My name is J.A.R.V.I.S']]
]
chat = Chat(pairs, reflections)
chat.converse()
#print(reflections)