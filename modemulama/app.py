from flask import Flask, render_templeta, url_for,request
import joblib




model = joblib.load('')


app = Flask(__name__)

@app.route("/predicts")
def test():
    if request.method =='POST':
        comment = request.form['area']
        predict = model.predict([comment])[0]
    return render_templeta('index.html', prediction ="This is our Prediction {}".format(predict))

if __name__ == "__main__":
    app.run(debug=True)