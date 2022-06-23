from flask import Flask, render_template, request
from backendDesktopbased import *
app = Flask(__name__, static_url_path='')

@app.route("/")
@app.route("/index", methods=['POST', 'GET'])
def index():
    data = None
    if request.method == 'POST':
        orderno = request.form.get('orderno')
        consigneeid = request.form.get('consigneeid')
        consigneename = request.form.get('consigneename')
        shippingaddress = request.form.get('shippingaddress')
        consigneecontact = request.form.get('consigneecontact')
        packageweight = request.form.get('packageweight')
        insert(orderno, consigneeid, consigneename, shippingaddress, consigneecontact, packageweight)
        data = view()
    return render_template('index.html', data = data)

if __name__ == "__main__":
    app.run()