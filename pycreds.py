import os
import hashlib
import getpass
import hmac

import botocore.session
import botocore.exceptions

# def _hash_original(value):
#     # test_key = bytes(os.environ["TEST_KEY"], "utf-8").decode('unicode_escape')
#     return hmac.new(os.environ["TEST_KEY"], value, digestmod=hashlib.sha256).hexdigest()

def _hash(data):
  key = os.environ["TEST_KEY"] # Defined as a simple string.
  key_bytes= bytes(key , 'latin-1')
  data_bytes = bytes(data, 'latin-1') # Assumes `data` is also a string.
  return hmac.new(key_bytes, data_bytes , digestmod=hashlib.sha256).hexdigest()

def main():
    access_key = getpass.getpass("Access Key: ").strip()
    secret_access_key = getpass.getpass("Secret Access Key: ").strip()
    print("AKID   hash: %s" % _hash(access_key))
    print("AKID length: %s" % len(access_key))
    print("\nSAK    hash: %s" % _hash(secret_access_key))
    print("SAK  length: %s" % len(secret_access_key))
    session = botocore.session.get_session()
    sts = session.create_client('sts', aws_access_key_id=access_key,
                                aws_secret_access_key=secret_access_key)
    try:
        response = sts.get_caller_identity()
        print("Successfuly made an AWS request with the "
              "provided credentials.\n")
    except botocore.exceptions.ClientError as e:
        print("Error making AWS request: %s\n" % e)


if __name__ == '__main__':
    main()
