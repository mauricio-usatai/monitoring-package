import boto3

class Database:
  def __init__(self, config):
    self.db_access_key_id = config.db_access_key_id
    self.db_secret_access_key = config.db_secret_access_key

  def connect(self):
    resource = boto3.resource(
      'dynamodb',
      aws_access_key_id = self.db_access_key_id,
      aws_secret_access_key = self.db_secret_access_key,
      region_name='sa-east-1',
    )
    return resource

  def put_item(self, item):
    self.connect().Table('monitoring').put_item(Item=item)
