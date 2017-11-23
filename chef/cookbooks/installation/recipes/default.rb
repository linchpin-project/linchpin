#
# Cookbook:: installation
# Recipe:: default
# Creates Docker Image from tar file and run the experiment. 
# Tar file should have Docker file and all project files.


git_tar_dir = "https://github.com/linchpin-project/linchpin/raw/master/examples/"

# Tar file to be deployed using Chef
git_tar_file = 'docker.tar'

#Check if OS is from Debian family e.g Ubuntu
unless %w(debian rhel).include?(node[:platform_family])
	return
end

# create directory where experiment is reproduced
home_dir = node['systemd_paths']['user']

tar_file_path = home_dir + "/linchpin-run/"

directory tar_file_path do
	action :create
end

#Download tar file from Git
remote_file tar_file_path + git_tar_file do
	source git_tar_dir + git_tar_file
end

# Create Docker Image
docker_image_name = git_tar_file.split(".tar").first
docker_image docker_image_name do
	source tar_file_path + git_tar_file
	action :build
end

# Create Docker container
docker_container docker_image_name do
	repo docker_image_name
	action :run
end
