# Dataset Titanic
- Download Data : https://www.kaggle.com/c/titanic/data

Project ini menggunakan Dataset Titanic

Total data yang digunakan adalah 1309

![alt text](https://i.imgur.com/wqIgo3e.jpg)

# Predict

Dalam melakukan prediksi, saya mencoba menggunakan 4 metode yaitu :
- Logistic Regression
- K Nearest Neighbors
- Tree Decision
- Random Forest

Pemilihan metode yang terbaik dilakukan dengan melakukan confusion matrix dan melihat F1-Score tertinggi yaitu : **Tree Decision**

![alt text](https://i.imgur.com/tqrFCRp.jpg)

## Data Insight
- Pclass = Kelas Tiket
- SibSp = Jumlah Sibling
- Parch = Jumlah Orang Tua ( Yang Kenal )

![alt text](https://i.imgur.com/PvZN7H5.jpg)


# Hasil Prediksi
User dapat melakukan prediksi dengan model yang terbaik ( dalam kasus ini yaitu **Tree Decision** ), ada 4 model yang disediakan dan user dapat memilih dalah satu metode yang ada.

## Tampilan website sederhana untuk melakukan prediksi
- Dapat dilihat di FlaskWeb.py. Apabila user ingin mengganti model prediksi, user dapat mengedit joblib yang ada.

![alt text](https://i.imgur.com/5Y0tJiJ.jpg)


## Tampilan Hasil Prediksi
![alt text](https://i.imgur.com/TpXpVIv.jpg)


# Selamat Mencoba
# Terimakasih !
