# 
# BACK
#


from flask import Flask, jsonify
from redis import Redis
from lib.managers.core_manager import CoreManager


app = Flask(__name__)
app.config.from_envvar('APP_CONFIG')


# Register managers
redis = Redis(host=app.config['REDIS_HOST'],
			  port=app.config['REDIS_PORT'])
core_manager = CoreManager(redis)


@app.route('/')
def index():
    return jsonify(result=redis.get('hits'))


@app.route('/business_logic')
def business_logic():
    core_manager.business_logic()
    return jsonify(message='Route: business_logic, OK!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
