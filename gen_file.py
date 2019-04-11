def gen_file(server_type):

    import jinja2
    from cfg_loader import load_yaml

    server_type = server_type + '.j2'
    templateFilePath = jinja2.FileSystemLoader('./')
    jinjaEnv = jinja2.Environment(loader=templateFilePath)
    jtemplserver = jinjaEnv.get_template(server_type)
    conf = load_yaml('config.yml')

    outputsrv = jtemplserver.render(conf)
    return outputsrv

