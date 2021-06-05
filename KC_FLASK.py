#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
app= Flask(__name__)
@app.route('/')
def hello():
    return "This is my first flask app."
if __name__== '__main__':
    app.run(debug= True)


# In[ ]:




