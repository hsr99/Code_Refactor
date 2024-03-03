from flask import Flask, render_template, request

app = Flask(__name__)

notes = []

@app.route('/', methods=["GET", "POST"])  
def index():
    if request.method == "POST":
        note = request.form.get("note")
        if note:
            notes.append(note)
    return render_template("home.html", notes=notes)

@app.route('/delete/<int:index>', methods=["POST"])
def delete(index):
    if index < len(notes):
        del notes[index]
    return render_template("home.html", notes=notes)

@app.route('/update/<int:index>', methods=["POST"])
def update(index):
    if index < len(notes):
        new_note = request.form.get("new_note")
        if new_note:
            notes[index] = new_note
    return render_template("home.html", notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
