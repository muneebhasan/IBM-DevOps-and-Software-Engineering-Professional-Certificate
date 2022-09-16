!pip install ibm_watson 
apikey=""
url=""
#import deps
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator=IAMAuthenticator(apikey)
language_translator=LanguageTranslatorV3(version="2018-05-01",authenticator=authenticator)
language_translator.set_service_url(url)

def english_to_french(text1):
  #This translates text to french from english
  frenchtranslation=language_translator.translate(text=text1,model_id="en-fr").get_result()
  print (frenchtranslation.get("translations")[0].get("translation"))
def french_to_english(text1):
  #This translates text to English from French
  englishtranslation=language_translator.translate(text=text1,model_id="fr-en").get_result()
  print( englishtranslation.get("translations")[0].get("translation"))


english_to_french("hello")


