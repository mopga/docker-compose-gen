import jinja2
import ruamel.yaml as yaml


def gen_file(server_type):

    server_type = server_type + '.j2'
    templateFilePath = jinja2.FileSystemLoader('./')
    jinjaEnv = jinja2.Environment(loader=templateFilePath)
    jtemplserver = jinjaEnv.get_template(server_type)
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


print(gen_file('master'))
print(gen_file('slave'))


