import os
from pandas import DataFrame, read_csv

project_dir = os.path.split(os.path.realpath(__file__))[0]
base_url = 'ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/'
harmonised_df = read_csv(project_dir + os.sep + 'harmonised_list.txt', usecols=[1])

def search(pmid: str, study_accession: str, EFO_trait: str) -> DataFrame:
    pass


def browser():
    pass


def download():
    pass


def parse():
    pass
