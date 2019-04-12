from jinja2 import Environment
import ruamel.yaml as yaml

master_template = """\
version: '2.2'

services:
  pdi-srv:
    build: .
    container_name: {{ container_name }}-{{ i }}
    command: 'master'
    network_mode: host
    volumes:
      - ./log/tmp:/tmp:rw
      - ./log/pdi:/home/pdi/data-integration/logs:rw
    environment:
      PENTAHO_DI_JAVA_OPTIONS: {{ java_opts_master }}
      PDI_MAX_LOG_LINES: {{ max_log_line }}
      PDI_MAX_LOG_TIMEOUT: {{ max_log_timeout }}
      PDI_MAX_OBJ_TIMEOUT: {{ max_obj_timeot }}
      SERVER_NAME: {{ master_name }}
      SERVER_HOST: {{ server_host }}
      SERVER_PORT: {{ final_port }}
      SERVER_USER: {{ server_user }}
      SERVER_PASSWD: {{ server_passwd }}
    cpus: {{ cpu_limit_master }}
"""

slave_template = """\
version: '2.2'

services:
  pdi-srv:
    build: .
    container_name: {{ container_name }}-{{ i }}
    command: 'slave'
    network_mode: host
    volumes:
      - ./log/tmp:/tmp:rw
      - ./log/pdi:/home/pdi/data-integration/logs:rw
    environment:
      PENTAHO_DI_JAVA_OPTIONS: {{ java_opts_slave }}
      PDI_MAX_LOG_LINES: {{ max_log_line }}
      PDI_MAX_LOG_TIMEOUT: {{ max_log_timeout }}
      PDI_MAX_OBJ_TIMEOUT: {{ max_obj_timeot }}
      SERVER_NAME: {{ server_name }}
      SERVER_HOST: {{ server_host }}
      SERVER_PORT: {{ final_port }}
      SERVER_USER: {{ server_user }}
      SERVER_PASSWD: {{ server_passwd }}
    cpus: {{ cpu_limit_slave }}
"""


def gen_file(template):

    jtemplserver = Environment().from_string(template)
    conf = load_yaml('config.yml')
    outputsrv = jtemplserver.render(conf)
    return outputsrv


def load_yaml(filename, safe=True):

    try:
        f = open(filename, 'r')
        if safe:
            yml = yaml.YAML(typ='safe')
            conf = yml.load(f)
        else:
            yml = yaml.YAML(typ='rt')
            conf = yml.load(f)
        return conf or {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError("YAML parsing error: {0}".format(e.__traceback__))
    except Exception:
        raise


print(gen_file(master_template))
print(gen_file(slave_template))


