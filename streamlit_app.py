import pandas as pd
import streamlit as st
import plotly.express as px

# ファイルの読み込み
file_path = '20230818_choka.csv'  # 必要に応じてパスを修正
data = pd.read_csv(file_path)

# 日付をdatetime型に変換し、月列を追加
data['date'] = pd.to_datetime(data['date'])
data['month'] = data['date'].dt.month

# Streamlitアプリ
st.title("魚種別・月別の釣果数可視化")

# ユーザーが選択できるフィルタ
fish_names = st.multiselect(
    "表示する魚種を選択してください:",
    options=data['fishname'].unique(),
    default=data['fishname'].unique()
)

# データフィルタリング
filtered_data = data[data['fishname'].isin(fish_names)]

# 月別・魚種別に集計
summary = filtered_data.groupby(['month', 'fishname'], as_index=False)['results'].sum()

# グラフの作成
fig = px.bar(
    summary,
    x='month',
    y='results',
    color='fishname',
    title="月別・魚種別の釣果数",
    labels={'month': '月', 'results': '釣果数', 'fishname': '魚種'},
    barmode='group'
)

# グラフを表示
st.plotly_chart(fig)

st.title("データ可視化サンプル")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
