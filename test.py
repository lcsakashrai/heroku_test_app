#importing Translator from googletrans.
from googletrans import Translator
translator = Translator()
translation = translator.translate('mein english me hindi likh raha hoon', dest='en')
print(translation.text)
