from flask import Flask, redirect, render_template, flash, request, url_for

app = Flask(__name__)
app.secret_key = "BAjwqcwdvjfdk"

# name="User"
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method=="POST":
        nm = request.form['nm']
        return redirect(url_for('greet', nm=nm))
    flash("What's Your Name?")
    return render_template('index.html')

@app.route("/greet/<nm>", methods=['POST', 'GET'])
def greet(nm):
    if request.method=="POST":
        nm = request.form['nm']
        return redirect(url_for('greet', nm=nm))
    flash(f"Hi, {nm} Welcome to my page.")
    return render_template('index.html', name=nm)

if __name__=="__main__":
    app.run(debug=True)