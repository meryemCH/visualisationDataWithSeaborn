
import base64
import io
import pandas as pd
from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)


@app.route('/')
def titanic():
    data = pd.read_csv("titanic.csv")
    fig, ax = plt.subplots(figsize=(10,6))
    sns.set_style("white")
    flatui = ["#26C6DA", "#146A76"]
    sns.scatterplot(x="Pclass", y="Age", data=data,hue="Sex",hue_order=['male','female'],
    palette=sns.color_palette(flatui))
    ax.set_xticks([1,2,3])
    ax.set_yticks([0,10,20,30,40,50,60,70,80,90,100])
    ax.set_xlabel("Pclass",fontsize=14)
    ax.set_ylabel("Age",fontsize=14)
    ax.set_title("Titanic Visualisation",fontsize=18)
    plt.savefig("titanic.png")
    img = io.BytesIO()
    fig.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template("index.html", plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=False)
