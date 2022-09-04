import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_homepage")
def get_homepage():
    return render_template("index.html")


@app.route("/")
@app.route("/get_partners")
def get_partners():
    return render_template("partners.html")


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipe=recipes)


# search function
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipe=recipes)


# code is based on mini project tutorial
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # adding new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# code is based on mini project tutorial
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# loads users profile function
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    recipes = list(mongo.db.recipes.find({"created_by": username}))
    if session["user"]:
        return render_template(
            "profile.html", username=username,
            recipe=recipes
        )

    return redirect(url_for("login"))


# log out user function
# code is based on mini project tutorial
@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# add new recipe to database
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if 'user' not in session:
        flash('You need to log in to add a recipe.')
        return redirect(url_for('login'))

    if request.method == "POST":
        recipe = {
            "dish_name": request.form.get("dish_name"),
            "category_name": request.form.get("category_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "ingredients": request.form.get("ingredients"),
            "preparation_steps": request.form.get("preparation_steps"),
            "image_url": request.form.get("image_url"),
            "tools": request.form.get("tools"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe is Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    cuisine = mongo.db.cuisine.find().sort("cuisine_name", 1)
    return render_template(
        "add_recipe.html", categories=categories,
        cuisine=cuisine
    )


# edit recipe function
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if 'user' not in session:
        flash('You need to log in to edit a recipe.')
        return redirect(url_for('login'))

    if request.method == "POST":
        submit = {
            "dish_name": request.form.get("dish_name"),
            "category_name": request.form.get("category_name"),
            "cuisine_name": request.form.get("cuisine_name"),
            "ingredients": request.form.get("ingredients"),
            "preparation_steps": request.form.get("preparation_steps"),
            "image_url": request.form.get("image_url"),
            "tools": request.form.get("tools"),
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    cuisine = mongo.db.cuisine.find().sort("cuisine_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe,
        categories=categories, cuisine=cuisine
    )


# get single recipe
@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipe.html", recipe=recipe)


# delete recipe function
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe is Successfully Deleted")
    return redirect(url_for("get_recipes"))


# get categories from database
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


# adding category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if 'user' not in session:
        flash('You need to log in to add a category.')
        return redirect(url_for('login'))

    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category is Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if 'user' not in session:
        flash('You need to log in to edit a category.')
        return redirect(url_for('login'))

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category was Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    if 'user' not in session:
        flash('You need to log in to delete a category.')
        return redirect(url_for('login'))

    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category is Successfully Deleted")
    return redirect(url_for("get_categories"))


# get cuisines from database
@app.route("/get_cuisines")
def get_cuisines():
    cuisines = list(mongo.db.cuisine.find().sort("cuisine_name", 1))
    return render_template("cuisines.html", cuisines=cuisines)


# adding cuisine
@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if 'user' not in session:
        flash('You need to log in to add a cuisine.')
        return redirect(url_for('login'))

    if request.method == "POST":
        cuisine = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisine.insert_one(cuisine)
        flash("New Cuisine is Added")
        return redirect(url_for("get_cuisines"))

    return render_template("add_cuisine.html")


# edit cuisine
@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if 'user' not in session:
        flash('You need to log in to edit a cuisine.')
        return redirect(url_for('login'))

    if request.method == "POST":
        submit = {
            "cuisine_name": request.form.get("cuisine_name")
        }
        mongo.db.cuisine.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine was Successfully Updated")
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisine.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


# delete cuisine
@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    if 'user' not in session:
        flash('You need to log in to delete a cuisine.')
        return redirect(url_for('login'))

    mongo.db.cuisine.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine is Successfully Deleted")
    return redirect(url_for("get_cuisines"))


# calls contact us page
@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact_us.html")


# get stats page
@app.route("/")
@app.route("/get_stats")
def get_stats():
    stats_dict = {}
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    all_recipes = list(mongo.db.recipes.find())
    length_list = len(all_recipes)

    for category in categories:
        recipes = list(mongo.db.recipes.find(
            {"category_name": category["category_name"]})
            )
        num = 0

        for recipe in recipes:
            if recipe["category_name"]:
                num += 1
            temp_name = recipe["category_name"]
            temp_num = num * 100 / length_list
            stats_dict[temp_name] = round(temp_num, 2)

    return render_template(
        "stats.html", stats_dict=stats_dict, length_list=length_list)


# runs 404 page
@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404


# runs 500 page
@app.errorhandler(500)
def error500(e):
    flash('Server Error 500.')
    return render_template('404.html'), 500


# runs application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
