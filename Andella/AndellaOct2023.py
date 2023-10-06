import configparser
config_object = configparser.ConfigParser()
file =open("Confi.ini","r")
config_object.read_file(file)
output_dict=dict()
sections=config_object.sections()
for section in sections:
    output_dict[section]={}
    items=config_object.items(section)
    for key,val in items:
        #print("key {}= val {}".format(key,val))
        try:
            output_dict[section][key] = config_object.getint(section, key)
        except ValueError:
            try:
                output_dict[section][key] = config_object.getfloat(section, key)
            except ValueError:
                #output_dict[section][key] = config_object.get(section, key)
                try:
                    output_dict[section][key] = config_object.getboolean(section, key)
                except ValueError:
                    output_dict[section][key] = config_object.get(section, key)

    #output_dict[section]=dict(items)
print("The output dictionary is:")
print(output_dict)