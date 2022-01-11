[![tests](https://github.com/boutetnico/ansible-role-sensu-go-backend/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-sensu-go-backend/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.sensu_go_backend-blue.svg)](https://galaxy.ansible.com/boutetnico/sensu_go_backend)

ansible-role-sensu-go-backend
=============================

This role installs [Sensu Go backend](https://docs.sensu.io/sensu-go/latest/reference/backend/) through Docker.

It is part of a family of Ansible roles allowing to setup and configure Sensu Go components:

- [ansible-role-sensu-go-agent](https://github.com/boutetnico/ansible-role-sensu-go-agent)
- [ansible-role-sensu-go-cli](https://github.com/boutetnico/ansible-role-sensu-go-cli)
- [ansible-role-sensu-go-backend](https://github.com/boutetnico/ansible-role-sensu-go-backend)

Requirements
------------

Ansible 2.7 or newer.

Supported Platforms
-------------------

- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                        | Required | Default            | Choices   | Comments                                           |
|---------------------------------|----------|--------------------|-----------|----------------------------------------------------|
| sensu_backend_docker_image      | true     | `sensu/sensu`      | string    |                                                    |
| sensu_backend_docker_tag        | true     | `latest`           | string    | https://hub.docker.com/r/sensu/sensu/tags          |
| sensu_backend_docker_pull       | true     | `false`            | boolean   | Set `true` to force pulling a newer Docker image.  |
| sensu_backend_docker_env        | true     |                    | dict      | See `defaults/main.yml`.                           |
| sensu_backend_host_data_path    | true     | `/var/lib/sensu`   | string    | Path to files on host for persistence.             |
| sensu_backend_log_level         | true     | `warn`             | string    | Values: panic, fatal, error, warn, info, debug.    |
| sensu_backend_network_mode      | true     | `bridge`           | string    | `bridge`, `host`, `none` or `container:<name|id>`. |
| sensu_backend_ports             | true     |                    | list      | See `defaults/main.yml`.                           |
| sensu_backend_container_state   | true     | `started`          | string    | `absent`, `present`, `stopped` or `started`.       |
| sensu_backend_restart_policy    | true     | `unless-stopped`   | string    | `no`, `on-failure`, `always`, `unless-stopped`.    |

Dependencies
------------

Docker

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-sensu-go-backend

Testing
-------

## Debian

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-11

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-2004

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
