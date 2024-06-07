import io

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from flask import Flask, jsonify, send_file

app = Flask(__name__)


# 读取数据
def read_data():
    df = pd.read_csv('data/movies.csv')
    return df


# 计算类型总数
def calculate_genre_counts(df):
    genres = df['genres'].str.split('|').explode().value_counts()
    return genres


# 生成图表
def generate_pie_chart(genres):
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    colors = sns.color_palette("pastel")
    plt.pie(genres, labels=genres.index, autopct='%1.1f%%', startangle=140, colors=colors)
    plt.title('Movie Genres Distribution')
    plt.axis('equal')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


def generate_bar_chart(genres):
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    ax = sns.barplot(x=genres.index, y=genres.values, palette="viridis")
    ax.set_title('Movie Genres Count')
    ax.set_xlabel('Genre')
    ax.set_ylabel('Count')
    plt.xticks(rotation=45)
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


@app.route('/api/genres', methods=['GET'])
def genres():
    df = read_data()
    genres = calculate_genre_counts(df)
    return jsonify(genres.to_dict())


@app.route('/api/genres/pie-chart', methods=['GET'])
def pie_chart():
    df = read_data()
    genres = calculate_genre_counts(df)
    buf = generate_pie_chart(genres)
    return send_file(buf, mimetype='image/png')


@app.route('/api/genres/bar-chart', methods=['GET'])
def bar_chart():
    df = read_data()
    genres = calculate_genre_counts(df)
    buf = generate_bar_chart(genres)
    return send_file(buf, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
