# Centreon configuration difference

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Centreon Configuration Difference script for Centreon operator.

**Goals**:

- Configuration change management via git.
- Ensure the consistency of the Centreon configuration.
- Simplifies the configuration of a new Centreon stack.
- Standalone and lightweight.

## Installation

```sh
python -m pip install centreoncdiff
```

## Usage

### 1. Create yaml centreon configuration

Example :

- Create the file my_acl_menu.yml with the following content :

```yml
- object: aclmenu
  name: ACL menu number 1
  alias: An ACL menu
  activate: True
  comment: My first ACL Menu
  grantrw:
    - Home
```

### 2.1 Simple generation file

```sh
python centreoncdiff -c my_acl_menu.yml
# or into a file
python centreoncdiff -c my_acl_menu.yml > centreon_config.txt
```

### 2.2 Simple generation and centreon import process

```sh
python centreoncdiff -c my_acl_menu.yml > centreon_config.txt && centreon -u admin -p mypassword -i centreon_config.txt
```

## Roadmap

Much work remains to be done.

But here are the next steps:

- Implement difference in main program
- Developping Centreon ACL resources configuration (and these unit tests).
- Developping Centreon ACL groups configuration (and these unit tests).

Here are the other topics that will be covered (this list may be expanded).

- Developping Centreon commands configuration (and these unit tests).
- Developping Centreon contact groups configuration (and these unit tests).
- Developping Centreon contact templates configuration (and these unit tests).
- Developping Centreon host categories configuration (and these unit tests).
- Developping Centreon host groups configuration (and these unit tests).
- Developping Centreon host templates configuration (and these unit tests).
- Developping Centreon service categories configuration (and these unit tests).
- Developping Centreon service groups configuration (and these unit tests).
- Developping Centreon service templates configuration (and these unit tests).
- Developping Centreon time periods configuration (and these unit tests).
