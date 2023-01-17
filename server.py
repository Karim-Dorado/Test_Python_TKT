import json
from change_calculator import percentage_change
from flask import Flask, render_template


def load_companies():
    with open('test python.json') as f:
        list_of_companies = json.load(f)
        return list_of_companies


app = Flask(__name__)
app.secret_key = 'my_secret_key'

companies = load_companies()


@app.route("/")
def index():
    return render_template('index.html', companies=companies)


@app.route('/detail/<company>')
def detail(company):
    try:
        found_company = [c for c in companies if c['name'] == company][0]

        ca_change = percentage_change(found_company['results'][0]['ca'],
                                      found_company['results'][1]['ca'])

        margin_change = percentage_change(found_company['results'][0]['margin'],
                                          found_company['results'][1]['margin'])

        ebitda_change = percentage_change(found_company['results'][0]['ebitda'],
                                          found_company['results'][1]['ebitda'])

        loss_change = percentage_change(found_company['results'][0]['loss'],
                                        found_company['results'][1]['loss'])

        return render_template('detail.html',
                               company=found_company,
                               ca_change=ca_change,
                               margin_change=margin_change,
                               ebitda_change=ebitda_change,
                               loss_change=loss_change)
    except IndexError:
        return render_template('index.html',
                               companies=companies,
                               message="Unkwnon company")


if __name__ == '__main__':
    app.run(debug=True)
