# Import libraries
import streamlit as st
import pandas as pd
import tensorflow as tf
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import string
import contractions

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load our previously trained model
model = tf.keras.models.load_model('/Users/jesusb/Final_Project_Streamlit_Ironhack/nn_lstm_5')


def text_cleaner(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = contractions.fix(text)
    stopwords_set = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords_set]

    return " ".join(tokens)


# Define a function to create a dataset from the user input
def df_to_dataset(dataframe, shuffle=False, batch_size=1):
    df = dataframe.copy()
    ds = tf.data.Dataset.from_tensor_slices(df['title_text'].to_list())
    ds = ds.batch(batch_size)
    return ds


# Define a function to make a prediction
def predict_fake_news(title, text):
    title_text = title + " " + text
    title_text = text_cleaner(title_text)
    input_df = pd.DataFrame({'title_text': [title_text]})
    input_data = df_to_dataset(input_df, shuffle=False)
    prediction = model.predict(input_data)
    return prediction[0][0]


# Build a Streamlit app
st.title('Fake News Detector')

# Use Streamlit columns
col1, col2 = st.columns(2)

with col1:
    title = st.text_input('News Title')

with col2:
    text = st.text_area('News Text', height=400)

fake_probability = None

if st.button('Predict'):
    prediction = predict_fake_news(title, text)
    fake_probability = round((prediction * 0.8744012117385864) * 100, 2)

    if fake_probability > 50:
        st.write('This news is likely fake.')
    else:
        st.write('This news is likely true.')

if fake_probability is not None:
    st.write('The model predicts a probability of', fake_probability, '% that this news is fake.')

# Adding disclaimer
st.markdown('---')
st.markdown(
    """
    *Disclaimer:* This prediction is based on a Deep Learning model called LSTM (Long Short-Term Memory). It is based on a variety of recurrent neural networks (RNNs) that are capable of learning long-term dependencies, especially in sequence prediction problems. 
    This is a research project and as such, it may be prone to errors. 
    We recommend doing further research before determining whether a piece of news is true or fake.
    """
)

