from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb+srv://test:sparta@cluster0.rvhpcnz.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta