from flask import Flask, render_template, request
import random

app = Flask(__name__)

def calculate_house_price(kota, luas_tanah, jumlah_kamar, jumlah_kamar_mandi, garasi, jumlah_lantai):
    kota_coef = 30
    luas_tanah_coef = 10
    jumlah_kamar_coef = 4
    jumlah_kamar_mandi_coef = 2
    garasi_coef = 2
    jumlah_lantai_coef = 4

    # Nilai kota
    kota = kota.lower()
    if kota in ['jakarta', 'surabaya']:
        kota_value = 20
    elif kota in ['semarang', 'yogyakarta', 'malang', 'bandung', 'bekasi']:
        kota_value = 15
    elif kota in ['bogor', 'depok', 'cirebon', 'tasikmalaya', 'solo', 'magelang']:  # Jawa
        kota_value = 10
    else:
        kota_value = random.randint(1, 5)

    price = ((kota_value * kota_coef + int(luas_tanah) * luas_tanah_coef) +
             int(jumlah_kamar) * jumlah_kamar_coef +
             int(jumlah_kamar_mandi) * jumlah_kamar_mandi_coef +
             int(garasi) * garasi_coef +
             int(jumlah_lantai) * jumlah_lantai_coef) * 1_000_000
    return price

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'kota': request.form['kota'],
            'luas_tanah': request.form['luas_tanah'],
            'jumlah_kamar': request.form['jumlah_kamar'],
            'jumlah_kamar_mandi': request.form['jumlah_kamar_mandi'],
            'garasi': 1 if 'garasi' in request.form else 0,
            'jumlah_lantai': request.form['jumlah_lantai']
        }
        harga = calculate_house_price(**data)
        return render_template('end.html', harga=harga, data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
