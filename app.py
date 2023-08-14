import datetime
import os
from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.survzilla
    customers = []

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            city = request.form.get("city")
            phone = request.form.get("phone")
            post = request.form.get("post")

            # Добавляем в базу данных
            app.db.customers.insert_one({
                "first_name": first_name,
                "last_name": last_name,
                "city": city,
                "phone": phone,
                "post": post
            })

            print("Entry added:", first_name, last_name, city, phone, post)

            return redirect("index3.html")
        
        return render_template("index2.html")

    if __name__ == "__main__":
        app.run(debug=True)

    @app.route("/index3.html")
    def page1():
        return render_template("index3.html")

    return app