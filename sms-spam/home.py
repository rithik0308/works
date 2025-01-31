import pickle
import streamlit as st
import string
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
ps  = PorterStemmer()

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the Message ")

def converter (obj):
    obj = obj.lower()
    obj = nltk.word_tokenize(obj)
    res = [word for word in obj if word.isalnum()] 
    obj = res
    res = [ i  for i in obj  if i not in stopwords.words('english') and  i not in string.punctuation]
    obj = res 
    res = [ ps.stem(i)  for i in obj ]
    return " ".join(res)

if st.button('Predict'):
    transform_sms = converter(input_sms)
    vectors  = tfidf.transform([transform_sms])
    result = model.predict(vectors)[0]

    if result == 1 :
        st.header('Spam')
    else :
        st.header('Not Spam')