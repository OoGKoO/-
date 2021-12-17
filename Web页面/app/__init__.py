from flask import Blueprint

regist_blue = Blueprint('regist', __name__, url_prefix='/regist')
admin_blue = Blueprint('admin', __name__, url_prefix='/admin')

from . import regist,admin