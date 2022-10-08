# dubilier
A Discord bot providing a modular command structure with the primary focus 
of managing users within a ham radio club's server.

## Contributing
The development workflow is very close to a trunk based development flow, with 
a minor addition that the primary development branch is `develop` with any and 
all code that is merged into the `main` branch considered as "production ready".

### Preparing Development Environment
Currently the suggested development environment is focused on Linux using the 
Ubuntu distribution, however, the following steps could be applied to your 
distro of choice.

**Install system level packages**
```bash
sudo apt-get update
sudo apt-get install -y python3.9 python3-pip python3-venv
```

**Create Python environment**

> **NOTE**: This should be done at the root level of the repository in order to 
avoid any potential conflicts.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Install development dependencies**

> **NOTE**: This assumes that the venv for the project has been activated.

```bash
python3 -m pip install -Ue .[dev]
```

**Test development environment**

> **NOTE**: This should be ran prior to making any changes to ensure that a 
passing result is experienced.

> **NOTE**: This should be ran at the root level of the repository and assumes 
that the venv for the project has been activated.

```bash
tox
```

In the event that `tox` exits successfully, the development environment setup 
is complete.