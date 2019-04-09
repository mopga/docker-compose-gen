def load_yaml(filename, safe=True):

    import ruamel.yaml as yaml
    from log import Log

    try:
        f = open(filename, 'r')
        Log.debug("Parsing YAML...")
        if safe:
            yml = yaml.YAML(typ='safe')
            conf = yml.load(f)
        else:
            yml = yaml.YAML(typ='rt')
            conf = yml.load(f)
        return conf or {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError("YAML parsing error: {0}".format(e.problem))
    except Exception:
        raise
