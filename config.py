import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'articlecmsstorage'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'x77jArbNmPMGpDlH0CmWg1jWt4gTTQui5OTpXjfZWpI8JHif/iZQxgLdnAn0ODgXwwgYLtRsdd1Z+AStm1T5oA=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'articlecmsstorage'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'articlecms-dbserver.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'articlecms'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'articlecms'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Admin123'
    # Below URI may need some adjustments for driver version, based on your OS, if running locally
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE  + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ### Info for MS Authentication ###
    ### As adapted from: https://github.com/Azure-Samples/ms-identity-python-webapp ###
    CLIENT_SECRET = "5Bl8Q~NQH15wAqh2mU1F~kKL6b_fX1NEgewT1cKa"
    # In your production app, Microsoft recommends you to use other ways to store your secret,
    # such as KeyVault, or environment variable as described in Flask's documentation here:
    # https://flask.palletsprojects.com/en/1.1.x/config/#configuring-from-environment-variables
    # CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    # if not CLIENT_SECRET:
    #     raise ValueError("Need to define CLIENT_SECRET environment variable")

    AUTHORITY = "https://login.microsoftonline.com/common"  # For multi-tenant app, else put tenant name
    # AUTHORITY = "https://login.microsoftonline.com/Enter_the_Tenant_Name_Here"

    CLIENT_ID = "6e2294d6-a09d-4125-b612-57eb8f7ac4ae"

    REDIRECT_PATH = "/getAToken"  # Used to form an absolute URL; must match to app's redirect_uri set in AAD

    # You can find the proper permission names from this document
    # https://docs.microsoft.com/en-us/graph/permissions-reference
    SCOPE = ["User.Read"] # Only need to read user profile for this app

    SESSION_TYPE = "filesystem"  # Token cache will be stored in server-side session