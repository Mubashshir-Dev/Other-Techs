import tomllib

from pprint import pprint #pretty print

#binary data is represented by < class 'bytes'> in python


# -> mtlb func return krega dict (error nhi ayega agar nhi ki)
def load_toml() -> dict:

    """Load Toml data from file"""
    
    #it is plain text format document still tomllib() expect raw binary format file thats why we open it in binary mode 
    
    with open("config.toml","rb") as f:

        #its like int x = 9; -> x: int = 9;
        toml_data: dict = tomllib.load(f)
        return toml_data

pprint(load_toml(),sort_dicts=False)#format data into pretty ways and no sorting of key value pairs 