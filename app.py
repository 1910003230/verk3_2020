from flask import Flask, render_template
import urllib.request, json # þurfum þennan til að sækja JSON object yfir netið og til að höndla json í py skránni
app = Flask(__name__)


# rútínan hérna fyrir neðan fer á url, sækir JSON object og setur í url breytuna
# json.loads hendir JSON obect yfir í dictionary sem við vinnum með í .py skrá
with urllib.request.urlopen("http://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

Info=data
Info2=data['results'][0]['company']
Info3=data['results']
count=len(Info3)
Info4=[]
Info5=[]
ben=[]
die=[]
for x in range(count):
    addar=data['results'][x]['company']
    sin=data['results'][x]['bensin95']
    sel=data['results'][x]['diesel']
    ben.append(sin)
    die.append(sel)
    if addar not in Info4:
        Info4.append(addar)
for x in Info4:
    addar=str(x+'.png')
    Info5.append(addar)

    
@app.route('/')
def test():
    minnstaB=min(ben)
    minnstaD=min(die)
    bestB=[]
    for x in Info3:
        if x['bensin95'] == minnstaB:
            bestB.append(x)
    bestD=[]
    for x in Info3:
        if x['diesel'] == minnstaD:
            bestD.append(x)
    return render_template('home.html', Info4=Info4, Info5=Info5, bestB=bestB, bestD=bestD)

@app.route('/<id>')
def fyrirtæk(id):
    stadur=[]
    fjoldi=0
    for y in Info3:
        if y['company'] == id:
            stadur.append(y)
            fjoldi=fjoldi+1
    return render_template("upply.html", id=id, data=data, stadur=stadur, fjoldi=str(fjoldi))

@app.route('/olia/<id>')
def olia(id):
    verd=[]
    for y in Info3:
        if y['key'] == id:
            verd.append(y)
    return render_template("olia.html", id=id, data=data, verd=verd)

	# print(type(data)) debug, sjáum hvaða týpa data er = dict

if __name__ == "__main__":
	app.run(debug=True)