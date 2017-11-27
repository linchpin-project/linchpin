from __future__ import print_function
import os,sys,json,pprint
excludedLibrariesList = ["tzdata","libstdc++6"]
dockerFileName = "Dockerfile"


#Generate the list of all the python packages installed
def generatePythonPackagelist():
    pythonPackages = os.popen("pip freeze").readlines()
    return pythonPackages


#Returns default value if val is not in the list l
def safe_list_get (l, val, default):
  try:
    return l.index(val)
  except ValueError:
    return default


#As per the discussion we decided not to install the system libraries that break the apt-get command so excluding these libraries
def isLibraryRequired(name):
    for libraryName in excludedLibrariesList:
        if name in libraryName:
            return False
    return True


#Returns the list of packages needed to be installed from pip
def getPythonPackages(packageList):
    # print ("packageList",packageList)
    packages = generatePythonPackagelist()
    # print ("freeze",packages)
    packageNames = []
    #Create a list of names only instead of name==version
    for package in packages:
        # print("package",package.strip())
        packageNames.append(package.strip().split("==")[0])

    pipPackages = []
    for packagePath in packageList:
        if "/usr/local/lib/python2.7/dist-packages/" in packagePath:
            pack = packagePath.split("/")
            if len(pack) == 7:
                idx = safe_list_get(packageNames,pack[6],-1)
                if idx != -1:
                    pipPackages.append(packages[idx])
    return pipPackages



def genrateDockerFile():
    configJSON = json.load(open(sys.argv[1]))
    linchpinConfigPath = "/".join(sys.argv[1].split("/")[:-1])
    #print((configJSON["packages"]))
    osNameAndVersion = ":".join(configJSON['runs'][0]['distribution'])
    with open(linchpinConfigPath + "/" + dockerFileName,"w") as outfile:
        outfile.write("FROM "+ osNameAndVersion + "\n\n")
        outfile.write("RUN apt-get update" + "\n")
        for package in configJSON["packages"]:
            name = package['name']
            if isLibraryRequired(name):
                # name = package['name']
                version = package['version']
                outfile.write("RUN apt-get install -y " + name + "=" + version + "\n")
        outfile.write("RUN apt-get install -y python-pip" + "\n\n")
        pipCommands = getPythonPackages(configJSON["other_files"])
        #print (pipCommands)
        for pipCommand in pipCommands:
            outfile.write("RUN pip install " + pipCommand)
        outfile.write("\n")
        argvFromJson = configJSON['runs'][0]['argv']
        #print(argvFromJson)
        splitfolderName = argvFromJson[1].split('/')
        folderName = splitfolderName[1]
        #print (folderName)
        outfile.write("COPY " + folderName + " /" + folderName + "\n\n")
        outfile.write("ENTRYPOINT " + argvFromJson[0] + " " + "/".join(splitfolderName[1:]))


if __name__ == "__main__":
    genrateDockerFile()
