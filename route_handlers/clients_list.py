from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy


def clientsListHandler(ClientModel, db: SQLAlchemy, autorization, basket):

    if request.method == 'POST':
        clientId = request.form.get('id')

        client = ClientModel.query.filter_by(id=clientId).first()

        if (client != None):
            db.session.delete(client)
            db.session.commit()

    ClientsFromQuery = ClientModel.query.all()

    clients = []

    for client in ClientsFromQuery:

        clients.append({
            'id': client.id,
            'name': client.name,
            'login': client.login
        })

    return render_template('clients_list.html', clients=clients, autorization=autorization, basket=basket)
