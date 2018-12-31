#! /usr/bin/env python3

import requests
import os
import datetime

from influxdb import InfluxDBClient

BASE_URL = os.environ['SONAR_URL']
USER = os.environ['SONAR_USER']
PASSWORD = os.environ['SONAR_PASSWORD']
INFLUX_URL = os.environ['INFLUX_URL']
INFLUX_USER = os.environ['INFLUX_USER']
INFLUX_PASSWORD = os.environ['INFLUX_PASSWORD']
INFLUX_DB = os.environ['INFLUX_DB']
INFLUX_PORT = os.environ['INFLUX_PORT']

class SonarApiClient:

    def __init__(self, user, passwd):
        self.user = user
        self.passwd = passwd

    def _make_request(self, endpoint):
        r = requests.get(BASE_URL + endpoint, auth=(self.user, self.passwd))
        return r.json()
    
    def get_all_ids(self, endpoint):
        data = self._make_request(endpoint)
        ids = []
        for component in data['components']:
            dict = {
                'id': component['id'],
                'key': component['key']
            }
            ids.append(dict)
        return ids
    
    def get_all_available_metrics(self, endpoint):
        data = self._make_request(endpoint)
        metrics = []
        for metric in data['metrics']:
            metrics.append(metric['key'])
        return metrics
    
    def get_measures_by_component_id(self, endpoint):
        data = self._make_request(endpoint)
        return data['component']['measures']


class Project:

    def __init__(self, identifier, key):
        self.id = identifier
        self.key = key
        self.metrics = None
        self.timestamp = datetime.datetime.utcnow().isoformat()

    def set_metrics(self, metrics):
        self.metrics = metrics

    def export_metrics(self):
        influx_client = InfluxDBClient(
            host=INFLUX_URL,
            port=INFLUX_PORT,
            username=INFLUX_USER,
            password=INFLUX_PASSWORD,
            database=INFLUX_DB
        )
        influx_client.write_points(self._prepare_metrics())

    def _prepare_metrics(self):
        json_to_export = []
        for metric in self.metrics:
            try:
                metric['value'] = float(metric['value'] if ('value' in metric) else 0)
            except ValueError:
                metric['value'] = 0
            one_metric = {
                "measurement": metric['metric'],
                "tags": {
                    "id": self.id,
                    "key": self.key
                },
                "time": self.timestamp,
                "fields": {
                    "value": metric['value'] if ('value' in metric) else 0
                }
            }
            json_to_export.append(one_metric)
        return json_to_export


# Fetch all projects IDs
client = SonarApiClient(USER, PASSWORD)
ids = client.get_all_ids('/api/components/search?qualifiers=TRK')

# Fetch all available metrics
metrics = client.get_all_available_metrics('/api/metrics/search')
comma_separated_metrics = ''
for metric in metrics:
    comma_separated_metrics += metric + ','

# Collect metrics per project
uri = '/api/measures/component'
for item in ids:
    project_id = item['id']
    project_key = item['key']
    print(project_key, project_id)
    project = Project(identifier=project_id, key=project_key)
    component_id_query_param = 'componentId=' + project_id
    metric_key_query_param = 'metricKeys=' + comma_separated_metrics
    measures = client.get_measures_by_component_id(uri + '?' + component_id_query_param + '&' + metric_key_query_param)
    project.set_metrics(measures)
    project.export_metrics()

