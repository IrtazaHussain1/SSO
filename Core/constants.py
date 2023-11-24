import os
jwt_secret_key = os.environ.get('JWT_SECRET_KEY', 'jwt-falback-key')
jwt_hash_algo = os.environ.get('JWT_HASH_ALGO', 'HS256')