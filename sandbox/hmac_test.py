import hmac
import hashlib
secret_key = 'btRhtQkaT7Qf1s38Bh/Zgg=='
query_string = 'query=aleve&api_key=d7ea32809a'
hmac.new(secret_key, query_string, digestmod=hashlib.sha256).digest()
