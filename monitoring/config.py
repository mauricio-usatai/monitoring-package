class MonitoringConfig:
  def __init__(self, _type=None, name=None, machine=None,
    monitoring_endpoint=None, frequency=None, db_access_key_id=None, 
    db_secret_access_key=None, monitoring_agent_endpoint=None):

    self._type = _type
    self.name = name
    self.machine = machine
    self.monitoring_endpoint = f'{monitoring_endpoint}/monitoring'
    self.monitoring_agent_endpoint = f'{monitoring_agent_endpoint}/monitoring'
    self.frequency = frequency

    self.db_access_key_id = db_access_key_id
    self.db_secret_access_key = db_secret_access_key

  def get_as_dict(self):
    config = {
      '_type': self._type,
      'name': self.name,
      'machine': self.machine,
    }

    if self._type == 'active':
      config['active'] = { 'monitoring-endpoint': self.monitoring_endpoint }
    else:
      config['passive'] = { 'frequency': self.frequency }

    return config

