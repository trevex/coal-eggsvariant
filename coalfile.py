from coal import CoalFile
from util import git_clone, download, unzip, default_cmake_build, cp
from os import path

class EggsvariantFile(CoalFile):
    url = "https://github.com/eggs-cpp/variant"
    exports = ["include"]
    def prepare(self):
        git_clone(self.url, 'master')
    def info(self, generator):
        generator.add_include_dir('include/')
