import sqlalchemy
import redis


class SQLEngine:
    def __init__(self, conf):
        db = sqlalchemy.engine.url.URL(**conf)
        engine_conf = {
            'isolation_level': 'AUTOCOMMIT',
            'connect_args': {'connect_timeout': 10}
        }
        self.engine = sqlalchemy.create_engine(db, **engine_conf)

    def insert(self, sql, data=()):
        self.engine.execute(sql, data)

    def update(self, sql, data=()):
        self.engine.execute(sql, data)

    def delete(self, sql, data=()):
        self.engine.execute(sql, data)

    def select(self, sql, data=()):
        return self.engine.execute(sql, data).fetchall()

    def execute(self, sql):
        return self.engine.execute(sql)


class RedisEngine:
    def __init__(self, conf):
        self.rds = redis.Redis(**conf)

    def get(self, hash_data, key):
        result = self.rds.hget(hash_data, key)
        return result.decode('utf8') if result else result

    def set(self, hash_data, key, value):
        self.rds.hset(hash_data, key, value)

    def delete(self, hash_data, key):
        self.rds.hdel(hash_data, key)