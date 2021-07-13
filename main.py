from flask import Flask, url_for
from flask import redirect

app = Flask(__name__)


# user page
@app.route('/user/<username>')
# checks if name is in admin or not and redirects to appropriate page
def check_admin(username):
    admin = ['Godwin', 'Candice', 'Thapelo', 'Jason']
    if username in admin:
        return redirect('/admin/{}'.format(username))
    else:
        return redirect('/guest/{}'.format(username))


# Admin page
@app.route('/admin/<username>')
def admin_message(username):
    return "Welcome admin {}".format(username)


# Guest page
@app.route('/guest/<username>')
def guest_message(username):
    return "Welcome guest {}".format(username)


# Payment page
@app.route('/payment/<float:sal>')
# if salary < 10500.50, redirect to FNB. If not, redirect to sa home loan site
def payment(sal):
    if sal < 10500.50:
        return redirect('https://www.fnb.co.za/index.html')
    else:
        return redirect('https://www.sahomeloans.com/')


if __name__ == '__main__':
    app.debug = True
    app.run()
