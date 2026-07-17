import tomllib

def read_toml():
    file=open("config.toml","rb")
    return tomllib.load(file)

print(read_toml())