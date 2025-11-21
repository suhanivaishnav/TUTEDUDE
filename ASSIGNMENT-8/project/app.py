from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key"

# temporary storage (replace with DB later)
users = []

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # simple validation
        if not name or not email or not password:
            flash("All fields are required!", "error")
            return redirect(url_for("register"))

        # check if email already exists
        for u in users:
            if u['email'] == email:
                flash("Email already registered!", "error")
                return redirect(url_for("register"))

        users.append({
            "name": name,
            "email": email,
            "password": password
        })

        flash("Registration successful!", "success")
        return redirect(url_for("register"))

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
