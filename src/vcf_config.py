import os
import vcf


class VcfMisconfigured(Exception):
    pass


class VCFConfiguration:

    def __init__(self, vcf_dir, vcf_filename=None):
        """
        Configures a way of reading multiple vcfs efficiently. Instead of going through all the code,
        just specify a directory and an optional vcf_file
        :param vcf_dir: The directory to read vcfs from.
        :param vcf_filename: The name of a specific vcf file you want to analyze.
        """
        self.vcf_dir = vcf_dir  # Please provide absolute path to directory of vcf files.
        self.vcf_filename = vcf_filename  # The name of the vcf file you would like to analyze.
        if not vcf_filename.endswith('.vcf'):  # Trigger errors if vcf_filename does not point to a proper vcf_file
            self.vcf_filename = None

    def all_vcfs(self):
        """
        Returns a list of paths to all vcfs in the directory vcf_dir.
        :return: type list(str): A list of paths to all VCFs in vcf_dir.
        """
        vcf_file_list = next(os.walk(self.vcf_dir))[2]
        return [os.path.join(self.vcf_dir, vcf_file) for vcf_file in vcf_file_list if
                vcf_file != '.DS_Store' and vcf_file.endswith('.vcf')]

    def open_all_vcfs(self):
        """
        Creates a list of file objects for all vcfs in vcf_dir
        :return: type list(file). A list of opened VCF file objects in vcf_dir.
        """
        return [open(vcf, 'r') for vcf in self.all_vcfs()]

    def read_all_vcfs(self):
        """
        Creates a list of all readers in this
        :return: type list(vcf._Reader): A list of readers for all VCF's in this directory.
        """
        return [vcf.Reader[vcf_file] for vcf_file in self.open_all_vcfs()]

    def vcf_path(self):
        """
        Returns an intelligently joined path given a specified vcf filename.
        :return: type str. A path to the configured VCF.
        """
        if not self.vcf_filename:
            raise VcfMisconfigured("VCF not configured.")
        return os.path.join(self.vcf_dir, self.vcf_filename)

    def open_vcf(self):
        """
        Opens a vcf file. Can throw IOError if misconfigured.
        :return: type file. An opened vcf file.
        """
        if not self.vcf_filename:
            raise VcfMisconfigured('VCF not configured.')
        return open(self.vcf_path(), 'r')

    def read_vcf(self):
        """
        Opens a vcf reader for the specified file. Can throw IOError if misconfigured.
        :return: type vcf._Reader. An opened reader to iterate over a filereader.
        """
        if not self.vcf_filename:
            raise VcfMisconfigured('VCF not configured.')
        return vcf.Reader(self.open_vcf())

# Create your own configs down here.
andrew_config = VCFConfiguration('/Users/atsun/Documents/CSE182/vcf', 'CMS_nonCMS_chrX.annotated.phased.vcf')