import base64
import io
import pandas as pd
from flask import Flask, render_template, send_file
import matplotlib.pyplot as plt
import seaborn as sns
                              
app = Flask(__name__)


@app.route('/')
def titanic():
    data = pd.read_csv('titanic.csv')
    fig, ax = plt.subplots(figsize=(6, 6))
    sns.set_style("darkgrid")
    flatui = ["#26C6DA","#B824C3","#1C97A8","#595959", "#146A76"]
    sns.countplot(x='survived', hue='sex',data=data,palette=sns.color_palette(flatui))

    img = io.BytesIO()
    fig.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template("titanic.html", plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=False)
