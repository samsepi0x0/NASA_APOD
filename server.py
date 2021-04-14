from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

api = "<YOUR API GOES HERE>"

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        inp = request.form
        date = inp['date']
        month = inp['month']
        year = inp['year']
        if date == "" or month == "" or year == "":
            return render_template('index.html')
        date = year + "-" + month + "-" + date
        json_data = image(date)
        if json_data == 404:
            return render_template('404-not-found.html')
        explanation = json_data['explanation']
        url = json_data['url']
        title = json_data['title']
        return render_template('images.html', date=date, title=title, exp=explanation, url=url)
    return render_template('index.html') 

def image(date):
    global api
    print(date)
    url = "https://api.nasa.gov/planetary/apod?api_key=" + api + "&date=" + date
    print(url)
    r = requests.get(url)
    print(r.status_code)
    if not r:
        return 404
    data = r.content
    print(data)
    return json.loads(data)


if __name__ == '__main__':
    app.run(debug=False) 