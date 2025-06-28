# Webpages for ml and data projects
# python lib
# no requirements of html and css
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st  
import altair as alt
#page configuration
st.set_page_config(page_title='Streamlit function demo',
                     page_icon='😁',
                     layout='centered',)



## title and  text elements
st.title('Hello World')
st.header('1. Text elements')
st.subheader('markdown,code,latex')
st.markdown('**bold text**,*italic tect*,`code`text')
st.code("print('Hello everyone')",language="python")
st.latex(r"a^2+b^2=c^2")

st.divider()

##metrics and messages
st.header("2. Metrics and messages")
st.metric(label="Revenue", value=1234, delta="10%",delta_color="inverse")
st.error("This is an error message")
st.warning("This is a warning message")
st.info("This is an info message")
st.success("This is a success message")
st.exception(ValueError("This is an exception message"))

st.divider()



##data display

st.header("3. Data display")
df =pd.DataFrame(np.random.randn(10, 2), columns=["a", "b"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())

st.divider()

##chart
st.header("4. Chart")
#df = pd.DataFrame(np.random.randn(10, 2), columns=["a", "b"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x='index', y='a')
st.altair_chart(chart, use_container_width=True)
fig , ax = plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()