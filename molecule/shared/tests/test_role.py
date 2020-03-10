import pytest

import os

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
