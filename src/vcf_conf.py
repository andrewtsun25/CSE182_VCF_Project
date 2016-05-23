import os
import vcf


class NO_VCF(Exception):
    pass


class VCF_Configuration:

    def __init__(self, vcf_dir, vcf_filename):
        self.vcf_dir = vcf_dir  # Please provide absolute path if possible.
        self.vcf_filename = vcf_filename
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

    def vcf_path(self):
        """
        Returns an intelligently joined path given a specified vcf filename.
        :return: type str. A path to the configured VCF.
        """
        if not self.vcf_filename:
            raise NO_VCF("VCF not configured.")
        return os.path.join(self.vcf_dir, self.vcf_filename + '.vcf')

    def open_vcf(self):
        """
        Opens a vcf file. Can throw IOError if misconfigured.
        :return: type file. An opened vcf file.
        """
        if not self.vcf_filename:
            raise NO_VCF('VCF not configured.')
        return open(self.vcf_path())

    def read_vcf(self):
        """
        Opens a vcf reader for the specified file. Can throw IOError if misconfigured.
        :return: type vcf._Reader. An opened reader to iterate over a filereader.
        """
        if not self.vcf_filename:
            raise NO_VCF('VCF not configured.')
        return vcf.Reader(self.open_vcf())

defaultConfig = VCF_Configuration('/Users/atsun/Documents/vcf', 'CMS_nonCMS_chrX.annotated.phased.vcf')