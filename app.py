import streamlit as st


import numpy as np
import pandas as pd

import requests
from bs4 import BeautifulSoup

from pprint import pprint
import re

with st.form(key='website'):
	name = st.text_input(label='Input a website')
	submit = st.form_submit_button(label = "Submit")

def get_name(url):


    response=requests.get(url)
    #print(response.status_code)
    page=response.content
    page=BeautifulSoup(page,'html.parser')
    
    for url in page:
        try:
            url = page.find('meta',property='og:title')
            title = url['content']
            if title != 'Home':
                title = title.split(' |')[0]
            else:
                title =page.find('meta',{'name':'description'})
                title = title['content'].split(',')[0]
                 
        except TypeError:
            title = page.title.get_text()
            if title != 'Home':
                title=title
            else:
                title =page.find('meta',{'name':'description'})
                title = title['content'].split(',')[0]
            
            
        if title!=None: #Not to output many examples of the same result, we are in a loop :D 
            break
    return title
	
    

get_name(name)

st.markdown(f'The name of your website is: {get_name(name)}')