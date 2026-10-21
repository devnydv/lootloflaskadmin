from lootloadmin import app
from flask import render_template, request
from flask import Flask, jsonify
from config import supabase

def get_store_count():
    try:
        response = supabase.table("store").select("*", count="exact", head=True).execute() 
        return response.count or 0
    except Exception as e:
        print(f"Error fetching store count: {e}")
        return 5


@app.route('/')
def index():
    store_count = get_store_count()
    return render_template('index.html', store_count=store_count)

@app.route('/about')
def about():
    return render_template('about.html')
