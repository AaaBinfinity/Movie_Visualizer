import io

import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, jsonify, send_file, render_template

app = Flask(__name__)
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
    genres.plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title('Movie Genres Distribution')
    plt.ylabel('')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    return buf


def generate_bar_chart(genres):
    plt.figure(figsize=(10, 6))
    genres.plot.bar()
    plt.title('Movie Genres Count')
    plt.xlabel('Genre')
    plt.ylabel('Count')
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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
