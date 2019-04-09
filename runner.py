from cfg_loader import load_yaml

conf = load_yaml('config.yml')

print(conf['cpu_limit_slave'])


