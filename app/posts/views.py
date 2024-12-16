from flask import render_template, redirect, url_for, flash
from . import posts_bp
from .forms import PostForm
import json
import os

POSTS_FILE = os.path.join(os.path.dirname(__file__), "../../posts.json")

def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_posts(posts):
    with open(POSTS_FILE, "w") as file:
        json.dump(posts, file, indent=4)

@posts_bp.route("/")
def home():
    return render_template("home.html")  # Створимо шаблон home.html для головної сторінки

@posts_bp.route("/add_post", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        posts = load_posts()
        new_post = {
            "id": len(posts) + 1,
            "title": form.title.data,
            "content": form.content.data,
            "category": form.category.data,
            "is_active": form.is_active.data,
            "publication_date": form.publication_date.data.strftime("%Y-%m-%d"),
            "author": "Default User"  # Можна замінити на користувача із сесії
        }
        posts.append(new_post)
        save_posts(posts)
        flash(f"Post '{new_post['title']}' added successfully!", "success")
        return redirect(url_for("posts.add_post"))
    return render_template("posts/add_post.html", form=form)

@posts_bp.route("/posts")
def posts_list():
    posts = load_posts()
    return render_template("posts/posts_list.html", posts=posts)
