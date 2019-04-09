def gen_file():

    import jinja2
    from cfg_loader import load_yaml

    templateFilePath = jinja2.FileSystemLoader('./')
    jinjaEnv = jinja2.Environment(loader=templateFilePath)
    jtemplMaster = jinjaEnv.get_template("master.j2")
    jtemplSlave = jinjaEnv.get_template("slave.j2")

    with load_yaml('config.yml') as conf:
        outputMaster = jtemplMaster.render(conf)
        outputSlave = jtemplSlave.render(conf)
        print("\nConfMaster:\n", outputMaster)
        print("\nConfSlaver:\n", outputSlave)
