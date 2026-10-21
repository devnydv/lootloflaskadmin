from flask import Flask, jsonify
from config import supabase

def get_stores():
    try:
        response = supabase.table("store").select("*").execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


def get_one_store(store_id):
    try:
        response = supabase.table("store").select("*").eq("id", store_id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def add_store_data(store_name, icon_url):
    try:
        response = supabase.table("store").insert({"store_name": store_name, "store_icon": icon_url}).execute()
        return jsonify(response.data), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_store_data(store_id, store_name, icon_url):
    try:
        response = supabase.table("store").update({"store_name": store_name, "store_icon": icon_url}).eq("id", store_id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_store_data(store_id):
    try:
        response = supabase.table("store").delete().eq("id", store_id).execute()
        return jsonify(response.data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500