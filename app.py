from flask import Flask, render_template, request, jsonify
import re


from util import Image, contents

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/query',methods=['post'])
def query():
    query = request.form.get("query")
    image = Image(query)
    image.get_image()
    url = image.save_image()

    content = contents(query+'marketing copy')
    content = re.sub('[\u4e00-\u9fa5]', '', str(content))

    result = {}
    result['url'] = url
    result['content'] = content
    return jsonify(result)


if __name__ == '__main__':
    app.run()
