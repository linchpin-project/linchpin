# Linchpin

## Purpose
Linchpin is a framework to reproduce large scale scientic experiments.

**Note:** As of now, the framework only works for projects developed in Python.

## Software Requirements

### Required
* Python
* Reprozip - https://www.reprozip.org/
Note: Reprozip internally requires Python

### Optional
* Chef

## How to Reproduce an Experiment?

### Step 1: Run your experiment with Linchpin

Create a directory within the "run" directory, and store all your experiment source code within that directory.

	$ ./linchpin <command to execute your experiment>
	
For Example, if you created the directory "python-test", and have your python code within that directory.

	test@pc1:~/linchpin/run$ ls
	python-test
	test@pc1:~/linchpin/run$ cd python-test/
	test@pc1:~/linchpin/run/python-test$ ls
	demo.py

In this example, you can use the following command:

	$ ./linchpin python run/python-test/demo.py
	
Internally, Linchpin will invoke "Reprozip" to capture experimental environment including system details, libraries used, packages used, etc.

Reprozip stores all this information in a "yml" file.
Linchpin will create a directory "linchpin-config" under your experimental directory, and will store the yml file under this directory.

For example, in our case:
	
	test@pc1:~/linchpin/run/python-test$ ls
	linchpin-config	demo.py
	
### Step 2: Parsing Phase

* Phase A: Input to this phase is the "yml" file created by Reprozip. Linchpin will invoke a parser program to convert yml to JSON. This will remove unwanted entries created by Reprozip in the yml file. Also, it will format the configuration required further to generate the Docker configuration file (Dockerfile).

* Phase B: Input to this phase is the "JSON" file created in Phase A. After this, Linchpin will invoke another parser program to generate Dockerfile from JSON file generated in Phase A.

**Parameter Sweeping:** In Phase B, you can edit the dependencies/version in the JSON file.

Note: Both the JSON and Dockerfile will be stored under the "linchpin-config" directory.

### Step 3: Bundling Docker and Experiment files

Linchpin will create a "tar" file bundling Dockerfile and experiment files (source code) together.

### Step 4: Deployment (Optional)

In our case, we are uploading a tar file generated in Step 3 to git under "examples" directory.

We are using "Chef" (https://www.chef.io/) for deployment. The Chef cookbook can be found in "chef/cookbooks/installation/" directory.

Chef-client will download the "tar" file from git. (**Note:** Please edit the URLs of git project and tar file located by variable names "git_tar_dir", and "git_tar_file" in the Chef recipe ("chef/cookbooks/installation/recipes/default.rb").
Chef-client will create a "linchpin-run" directory in your home directory, and will download the "tar" file in that directory.
After that, Chef-client will create a docker image and container from the "Dockerfile" bundled in the "tar" file. It will also copy the source code to the docker image.

Upon the creation of container, Chef-client will automatically run the container once.

You can check the docker container created by Chef using:

	$ sudo docker ps -a
	
You will see a container created with the name of your experiment (This name is taken from the project directory you created under the "run" directory).

You can reproduce your experiment by executing the following command:

	$ sudo docker run -it <tar file name>
	
For example, in our case, the command would be:

	$ sudo docker run -it python-test
	

## Contributors

* [Rafael Ferreira da Silva][rs]
* [Vishal Oswal][vo]
* [Akshay Joshi][aj]

[rs]: http://rafaelsilva.com/
[vo]: https://www.linkedin.com/in/vishal13may/
[aj]: https://www.linkedin.com/in/akshay-joshi-8a961192/

