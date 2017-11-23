# frozen_string_literal: true
# This is a Chef attributes file. It can be used to specify default and override
# attributes to be applied to nodes that run this cookbook.

# Set a default name
default['maven']['m3_download_url'] = 'http://www.gtlib.gatech.edu/pub/apache/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz'
default['maven']['m3_checksum'] = '948110de4aab290033c23bf4894f7d9a'

# For further information, see the Chef documentation (https://docs.chef.io/essentials_cookbook_attribute_files.html).
