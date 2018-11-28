from flask import Flask, request ,render_template , session

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def learning(user=None):
    return render_template('test.html',username=user)

# By default route hadles only GET request. Add methods list to add more support
@app.route('/post/<int:post_id>' , methods=['GET','POST'])
def tweet(post_id):
    if request.method == 'POST':
        return 'POST ID is {}'.format(post_id)
    else:
        return 'You are asking for a GET request'


if __name__ == '__main__':
    app.run(port=8082,debug=True)