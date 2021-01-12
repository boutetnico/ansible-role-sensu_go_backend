import pytest

import os

import requests

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('sensu-backend'),
])
def test_container(host, name):
    container = host.docker(name)
    assert container.name == name
    assert container.is_running


@pytest.mark.parametrize('endpoint', [
  ('http://127.0.0.1:8080/health'),
])
def test_sensu_backend_is_reachable(endpoint):
    response = requests.get(endpoint)
    data = response.json()
    assert data['ClusterHealth'][0]['Healthy']
