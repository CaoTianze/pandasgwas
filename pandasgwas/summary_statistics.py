import os
import re
import sys
import warnings
import webbrowser
import random
import requests
from requests.adapters import HTTPAdapter

s = requests.Session()
s.mount('https://', HTTPAdapter(max_retries=5))
from pandas import DataFrame, read_csv, Series, read_table
from pandasgwas.client import ask_yes_no_question


def _applyDF(line):
    matchobj = re.match('\.(.*/)((.*)-(.*)-(.*).h.tsv.gz)', line)
    if matchobj is not None:
        return Series(
            data=['/pub/databases/gwas/summary_statistics' + matchobj.group(1), matchobj.group(2), matchobj.group(3),
                  matchobj.group(4), matchobj.group(5)])
    matchobj = re.match('\.(.*/)((GCST[0-9]*).h.tsv.gz)', line)
    return Series(
        data=['/pub/databases/gwas/summary_statistics' + matchobj.group(1), matchobj.group(2), None, matchobj.group(3),
              None])


project_dir = os.path.split(os.path.realpath(__file__))[0]
home_path = os.path.expanduser('~') + os.sep + 'pandasgwas_home'
host = 'ftp.ebi.ac.uk'
harmonised_df = read_csv(project_dir + os.sep + 'harmonised_list.txt', names=['raw'])
harmonised_df[['dir', 'file_name', 'PubMed_id', 'study_accession_id', 'EFO_trait_id']] = harmonised_df['raw'].apply(
    _applyDF)


def search(PubMed_id: str = None, study_accession_id: str = None, EFO_trait_id: str = None) -> DataFrame:
    if PubMed_id is None and study_accession_id is None and EFO_trait_id is None:
        warnings.warn('Since there are no input conditions, all index values will be returned.')
    filter_df = harmonised_df.copy()
    if PubMed_id is not None:
        filter_df = filter_df[filter_df['PubMed_id'] == PubMed_id]
    if study_accession_id is not None:
        filter_df = filter_df[filter_df['study_accession_id'] == study_accession_id]
    if EFO_trait_id is not None:
        filter_df = filter_df[filter_df['EFO_trait_id'] == EFO_trait_id]
    return filter_df


def browser(searched_DF: DataFrame):
    if len(searched_DF) > 5:
        answer = ask_yes_no_question(
            "You will have more than %s pages opened."
            "\r\nDo you still want to proceed? (Yes or No)" % len(searched_DF))
        if answer == "NO":
            return
    searched_DF['dir'].apply(lambda x: webbrowser.open_new_tab('https://' + host + x))


def download(search_DF: DataFrame):
    list(map(lambda x, y: _download_FTP(x, y), search_DF['dir'], search_DF['file_name']))


def _download_FTP(ftp_dir: str, file_name: str):
    os.makedirs(home_path, exist_ok=True)
    with s.get('https://' + host + ftp_dir + file_name, stream=True) as r:
        r.raise_for_status()
        with open(home_path + os.sep + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                i = random.randint(1, 5)
                sys.stdout.write(file_name + ' downloading' + '.' * i + '\r')
                f.write(chunk)
    sys.stdout.write('%s downloaded in %s\n' % (file_name, home_path))


def parse(searched_DF: DataFrame) -> DataFrame:
    pass
