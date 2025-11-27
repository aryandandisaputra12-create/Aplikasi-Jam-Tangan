from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

jam_tangan = [
    {"id": 1, "nama": "Casio G-Shock", "harga": 1500000, "stok": 5},
    {"id": 2, "nama": "Rolex Submariner", "harga": 120000000, "stok": 2},
    {"id": 3, "nama": "Seiko 5 Automatic", "harga": 2500000, "stok": 10}
]

@app.route('/')
def index():
    return render_template('index.html', data=jam_tangan)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        id_baru = len(jam_tangan) + 1
        nama = request.form['nama']
        harga = int(request.form['harga'])
        stok = int(request.form['stok'])
        jam_tangan.append({"id": id_baru, "nama": nama, "harga": harga, "stok": stok})
        return redirect(url_for('index'))
    return render_template('tambah.html')

@app.route('/hapus/<int:id>')
def hapus(id):
    global jam_tangan
    jam_tangan = [j for j in jam_tangan if j["id"] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
