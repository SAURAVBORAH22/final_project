import streamlit as st
import pandas as pd
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import numpy as np
def main():
    activities=['About','Toxic Comment Classification System','Developer']
    option=st.sidebar.selectbox('Menu Bar:',activities)
    if option=='About':
        html_temp = """
        <div style = "background-color: yellow; padding: 10px;">
            <center><h1>ABOUT PROJECT</h1></center>
        </div><br>
        """
        st.markdown(html_temp, unsafe_allow_html=True)
        st.title("Problem Statement and Background")
        st.subheader("The background for the problem originates from the multitude of online forums, where-in people participate actively and make comments. As the comments some times may be abusive, insulting or even hate-based, it becomes the responsibility of the hosting organizations to ensure that these conversations are not of negative type. The task was thus to build a model which could make prediction to classify the comments into various categories. Consider the following examples :")
        image=Image.open('1.png')
        st.image(image,use_column_width=True)
        st.header("The exact problem statement was thus as below:")
        st.subheader("Given a group of sentences or paragraphs, used as a comment by a user in an online platform, classify it to belong to one or more of the following categories — toxic, severe-toxic, obscene, threat, insult or identity-hate with either approximate probabilities or discrete values (0/1).")
        st.header("Multilabel vs Multiclass classification ?")
        st.subheader("As the task was to figure out whether the data belongs to zero, one, or more than one categories out of the six listed above, the first step before working on the problem was to distinguish between multi-label and multi-class classification.")
        st.subheader("In multi-class classification, we have one basic assumption that our data can belong to only one label out of all the labels we have. For example, a given picture of a fruit may be an apple, orange or guava only and not a combination of these.")
        st.subheader("In multi-label classification, data can belong to more than one label simultaneously. For example, in our case a comment may be toxic, obscene and insulting at the same time. It may also happen that the comment is non-toxic and hence does not belong to any of the six labels.")
        st.subheader("Hence, I had a multi-label classification problem to solve. The next step was to gain some useful insights from data which would aid further problem solving.")
    elif option=='Toxic Comment Classification System':
        st.title("Toxic Comment Classification System")
        #image=Image.open('Magnify_Monitoring.jpg')
        #st.image(image,use_column_width=True)
        f=open("final_model.pkl", "rb")
        model = pickle.load(f)
        v= pickle.load(f)
        st.write("""final project""")
        st.write('---')

        st.header('Specify Input Parameters')
        text = st.text_input("input text")
        lis=[]
        for i in range(6):
            lis.append(model[i].predict_proba(v.transform([text]))[:, 1])
        list=['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
        st.header('Output')
        for i in range(6):
            st.subheader(list[i])
            st.write(lis[i])
        st.write('---')
    
    elif option=='Developer':
        st.balloons()
        st.title('Prepared by:-')
        st.header('SAURAV BORAH')
        st.subheader('Machine Learning Intern, Technocolab')
        st.subheader('Source Code:-')
        st.write('https://github.com/SAURAVBORAH22/toxic-comment-classifier')




            
if __name__ == '__main__':
    main()
