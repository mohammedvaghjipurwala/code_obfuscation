# -*- coding: utf-8 -*-

import connexion
from flask import request, jsonify

from src.solver import Solver

EQ = Solver()

APP = connexion.App(__name__, specification_dir='./')

@APP.route("/v1/ping")
def ping():
    """
    ping-pong method

    Function to test the health of flask application

    Parameters: None

    Returns:
    string: "Pong"

    """
    return "Pong"

@APP.route("/v1/evaluate", methods=['POST'])
def evaluate():
    """
    Route to evaluate & solve the equation
    """
    return jsonify(EQ.solve(request.json))

