import streamlit as st 
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('こんなアプリをサイトアイデアに使えませんか？')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('日本で二番目に高い山は？')
expander.write('北岳')
expander = st.beta_expander('質問があるのですがどうすればいいですか？')
expander.write('はい、問い合わせフォームよりご入力ください。')
expander = st.beta_expander('購入したいですが何だか不安で。')
expander.write('はい、2週間無料お試しができます。')
expander = st.beta_expander('こんなことをしたいのですが、最適なアプリはありますか？')
expander.write('はい、〇〇はどうでしょう？')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味:', text

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)
'あなたが好きな数字は,', option, 'です。'

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:', condition

if st.checkbox('Show Image'):
   img = Image.open('nekobeer.jpg')
   st.image(img, caption='Toshiyuki Okamoto', use_column_width=True)


