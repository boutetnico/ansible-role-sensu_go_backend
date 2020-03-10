ansible-role-sensu-go-backend
=============================

This role installs Sensu Go backend through Docker.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)

Role Variables
--------------

| Variable                        | Required | Default                         | Choices   | Comments                                         |
|---------------------------------|----------|---------------------------------|-----------|--------------------------------------------------|
| sensu_backend_docker_image      | true     | `sensu/sensu`                   | string    |                                                  |
| sensu_backend_docker_tag        | true     | `latest`                        | string    | https://hub.docker.com/r/sensu/sensu/tags        |
| sensu_backend_docker_env        | true     |                                 | dict      | See `defaults/main.yml`.                         |
| sensu_backend_host_data_path    | true     | `/var/lib/sensu`                | string    | Path to files on host for persistence.           |
| sensu_backend_log_level         | true     | `warn`                          | string    | Values: panic, fatal, error, warn, info, debug.  |
| sensu_backend_webui_port        | true     | `3000`                          | int       | Sensu web UI.                                    |
| sensu_backend_api_port          | true     | `8080`                          | int       | Sensu API used by sensuctl, plugins.             |
| sensu_backend_websocket_port    | true     | `8081`                          | int       | WebSocket API used by Sensu agents.              |
| sensu_backend_restart_policy    | true     | `unless-stopped`                | string    |                                                  |

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

    molecule --base-config molecule/shared/base.yml test --scenario-name debian-9
    molecule --base-config molecule/shared/base.yml test --scenario-name debian-10

## Ubuntu

    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1604
    molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu-1804

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
