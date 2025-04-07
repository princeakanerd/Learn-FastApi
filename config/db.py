from pymongo import MongoClient
from pymongo.server_api import ServerApi

MONGO_URI = "mongodb+srv://imt2022041:A78WJQTCMXKvwyo5@fastapi-cluster.dtqtpi6.mongodb.net/?retryWrites=true&w=majority&appName=Fastapi-cluster"


conn = MongoClient(
    MONGO_URI,
    server_api=ServerApi('1'),
    tls=True,
    tlsAllowInvalidCertificates=True,
    tlsAllowInvalidHostnames=True
)