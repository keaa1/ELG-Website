from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/aboutUs')
def aboutUs():
    return render_template("aboutUs.html", user=current_user)

@views.route('/community')
def community():
    return render_template("community.html", user=current_user)

@views.route('/news')
def news():
    return render_template("news.html", user=current_user)

@views.route('/merch')
def merch():
    return render_template("merch.html", user=current_user)

