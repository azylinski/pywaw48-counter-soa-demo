# 
# BACK
#

class CoreManager(object):
    def __init__(self, redis):
        self._redis = redis

    def business_logic(self):
        print 'Very complicated business logic'
        self._redis.incr('hits')
        return
