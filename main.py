from flask import Flask
import random
app = Flask(__name__) #app = application

cumle1 = 'Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.'
cumle2 = '2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor.'
cumle3 = 'Teknolojik bağımlılık çalışması, modern bilimsel araştırmanın en ilgili alanlarından biridir.'

liste = [cumle1, cumle2, cumle3]

@app.route("/")
def hello_world():
    return f'<h1>{random.choice(liste)}</h1>'


app.run(debug=True)