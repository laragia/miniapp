from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'username' : 'Gast'}
    posts = [
        {
            'author' : {'username' : 'Paul' },
            'body' : 'Was fuer ein Tag'
            },
        {
            'author' : {'username' : 'Miriram' },
            'body' : 'Das Wette ist gut!'
            }
    ]
    return render_template('index.html', title='Home', user=user)