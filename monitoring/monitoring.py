from datetime import datetime
from flask import jsonify
import requests

from monitoring.database import Database

class Monitoring:
  def __init__(self, monitoring_config):
    self.config = monitoring_config
    self.database = Database(monitoring_config)
  
  def register(self, _type, app=None):
    # Save service configuration to database
    self.database.put_item(self.config.get_as_dict())
    # If _type is active, then create a /monitoring route
    # to be accessed by the monitoring agent
    if _type == 'active':
      @app.route('/monitoring')
      def monitoring():
        return jsonify({ 'status': 'ok' }), 200

  def send_keepalive(self):
    # Send keep alive to local monitoring agent
    try:
      requests.get(f'{self.config.monitoring_agent_endpoint}?name={self.config.name}')
    except Exception:
      return
