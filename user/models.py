from flask import Flask, jsonify, request, session, redirect, url_for
from passlib.hash import pbkdf2_sha256
from app import mongo
import uuid
from user import routes


class User:

    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        # print(request.form)

        # Create the user object.
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password.
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address
        if mongo.db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400

        if mongo.db.users.insert_one(user):
            return self.start_session(user)

        # return jsonify(user), 200
        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):
        user = mongo.db.users.find_one({
            "email": request.form.get('email')
        })

        if user:
            return self.start_session(user)
        return jsonify({"error": "Invalid login credentials"}), 401
