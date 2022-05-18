import json

import requests
from flask import Flask, render_template, request
app = Flask(__name__)

url = "https://main-gpt2-large-jeong-hyun-su.endpoint.ainize.ai/gpt2-large/long"
data = {
    "text": "Hi my name is hyeonwoong and",
    "num_samples": 5,
    "length": 20
}

models = {
    "gpt2-large": "http://main-gpt2-large-jeong-hyun-su.endpoint.ainize.ai/gpt2-large/long",
    "gpt2-cover-letter": "http://main-gpt2-cover-letter-jeong-hyun-su.endpoint.ainize.ai/gpt2-cover-letter/long",
    "gpt2-reddit": "http://master-gpt2-reddit-woomurf.endpoint.ainize.ai/gpt2-reddit/long",
    "gpt2-story": "http://main-gpt2-story-gmlee329.endpoint.ainize.ai/gpt2-story/long",
    "gpt2-ads": "http://main-gpt2-ads-psi1104.endpoint.ainize.ai/gpt2-ads/long",
    "gpt2-business": "http://main-gpt2-business-leesangha.endpoint.ainize.ai/gpt2-business/long",
    "gpt2-film": "http://main-gpt2-film-gmlee329.endpoint.ainize.ai/gpt2-film/long",
    "gpt2-trump": "http://main-gpt2-trump-gmlee329.endpoint.ainize.ai/gpt2-trump/long"
}

@app.route("/gpt2", methods=["POST"])
def gpt2():
    context = request.form['context']

    length = request.form['length']
    if length == "short":
        length = 32
    else:
        length = 64

    test2021 = 'https://train-bfwduo1j45469v5ok3wc-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune'
    test = 'https://train-3nr65znaojjnwlcl4jx4-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune'
    r = requests.post(
        test2021,
        headers={
            'Content-Type': 'application/json'
        },
        data=json.dumps({
            'text': context,
            'num_samples': 5,
            'length': length
        })
    )
    result = {'0': '', '1': '', '2': '', '3': '', '4': ''}
    i = 0
    for line in r.json():
        num = str(i)
        result[num] = line
        i += 1
        # print(line)
        # print(i)

    return result

# @app.route("/gpt2", methods=["POST"])
# def gpt2():
#     context = request.form['context']
#
#     model = request.form['model']
#     length = request.form['length']
#
#     url = models[model]
#
#     if length == "short":
#         length = random.randrange(2, 6)
#     else:
#         length = 20
#
#     data = {
#         "text": context,
#         "num_samples": 5,
#         "length": length
#     }
#
#     response = requests.post(url, data=data)
#     res = response.json()
#
#     print(res)
#
#     return res

def main():
    response = requests.post(url, data=data)

    if response.status_code == 200:
        res = response.json()
        print(res)
    else:
        print("Failed Request")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return 'About 페이지'

if __name__ == "__main__":

    main()
    app.run(host='0.0.0.0', port=5000)


