from lootloadmin import app
from flask import render_template, request, Response, redirect, url_for
from lootloadmin.store.storesdata import get_stores, get_one_store, add_store_data, update_store_data, delete_store_data

@app.route('/stores')
def store():
    alldata, error = get_stores()  # Call the get_stores function to fetch store data
    return render_template('stores.html', stores=alldata.get_json())


@app.route('/stores/add', methods=['GET', 'POST'])
def add_store():
    if request.method == 'POST':
        # Handle form submission
        store_name = request.form.get('store_name')
        icon_url = request.form.get('icon_url')
        # Here you can add logic to save the new store to the database
        # For now, we'll just return a success message
        add_store_data(store_name, icon_url)
        return redirect(url_for('store'))
    return render_template('add-store.html')

@app.route('/stores/update/<store_id>', methods=['GET', 'POST'])
def edit_store(store_id):
    if request.method == 'POST':
        # Handle form submission
        store_name = request.form.get('store_name')
        icon_url = request.form.get('icon_url')
        # Here you can add logic to update the store in the database
        # For now, we'll just return a success message
        update_store_data(store_id, store_name, icon_url)
        return redirect(url_for('store'))
    onedata, error = get_one_store(store_id)  # Call the get_one_store function to fetch store data
    return render_template('edit-store.html', store=onedata.get_json())

@app.route('/stores/delete/<store_id>', methods=['GET', 'POST'])
def delete_store(store_id):
    # Here you can add logic to delete the store from the database
    # For now, we'll just return a success message
    # You can implement the actual deletion logic as needed
    delete_store_data(store_id)
    return redirect(url_for('store'))