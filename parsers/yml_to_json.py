from __future__ import print_function
import sys,json,yaml,os


#Convert the yml file to json and remove the unnecessary data
def parse():
    inFileName = sys.argv[1]
    outFileName = inFileName.replace("yml","json")
    with open(outFileName, "w") as output_file, open(inFileName) as input_file:
        yml_to_dictionary = yaml.safe_load(input_file)
        if "version" in yml_to_dictionary.keys():
            del yml_to_dictionary['version']
        if 'additional_patterns' in  yml_to_dictionary.keys():
            del yml_to_dictionary['additional_patterns']
        if 'pack_id' in yml_to_dictionary.keys():
            del yml_to_dictionary["pack_id"]
        if "packages" in yml_to_dictionary.keys():
            for package in yml_to_dictionary["packages"]:
                del package["files"]
                del package["size"]
                del package["packfiles"]
        if "runs" in yml_to_dictionary.keys():
            for run in yml_to_dictionary["runs"]:
                del run["environ"]
        json.dump(yml_to_dictionary, output_file)


if __name__ == "__main__":
    parse()
