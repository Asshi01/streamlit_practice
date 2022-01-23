import imp
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("Streamlist 超入門")
st.write("プログレスバーの表示")
"start!"
latest_iteration =st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)
"Done!"

left_column, right_column =st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

expandar1 = st.expander("問い合わせ1")
expandar1.write("問い合わせ1の回答")

expandar2 = st.expander("問い合わせ2")
expandar2.write("問い合わせ2の回答")

expandar3 = st.expander("問い合わせ3")
expandar3.write("問い合わせ3の回答")


# インタラクティブなウィジェット（チェックボックス、セレクトボックス、テキスト入力、スライダー）の作成方法

#チェックボボックス
# if st.checkbox("Show Image"):
#     img = Image.open("img/2.jpg")
#     st.image(img, caption="ocean",use_column_width=True)#use_column_width=Trueは、実際のWebのレイアウトの横幅に合わせて、表示してくれる

#セレクトボックス
# option = st.selectbox(
#     "あなたの好きな数字をおしえてください",
#     list(range(1,11)),
# )
# "あなたの好きな数字は、",option,"です"



# text = st.text_input("あなたの趣味を教えてください")
# condition = st.slider("あなたの今の調子は？",0,100,50)

# "あなたの趣味は",text,"です"
# "コンディション：",condition

# img = Image.open("img/2.jpg")
# st.image(img, caption="ocean",use_column_width=True)#use_column_width=Trueは、実際のWebのレイアウトの横幅に合わせて、表示してくれる

# st.write("DataFrame")

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns =["lat","lon"]
#     )

# st.map(df)

#st.table(df.style.highlight_max(axis=0))#静的な表を使用する場合は、.tableを使用し、動的な表を使用する場合は、.dataframeを使用する




"""
# 章
## 説
#### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
``` 
"""
#""": Markdown形式で記載ができる
#```: Code形式で記載ができる
