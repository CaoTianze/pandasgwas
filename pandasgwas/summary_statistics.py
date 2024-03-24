"""
Functions for easy retrieval of summary statistics data based on FTP data.
```Python
from pandasgwas import summary_statistics
#Search the index based on PubMed_id, study_accession_id, and EFO_trait_id. The indexed results will be returned as a DataFrame.
search_DF = summary_statistics.search(PubMed_id='27918534', study_accession_id='GCST003966')
#Based on the index results, view the data directory on the browser.
summary_statistics.browser(search_DF)
#Based on index results, download summary statistics data in $Home/pandasgwas_home.
summary_statistics.download(search_DF)
#Based on the index results, load the data from $Home/pandasgwas_home and convert it into a DataFrame.
df = summary_statistics.parse(search_DF)
```
"""
import os
import re
import sys
import warnings
import webbrowser

import requests
from pandas import DataFrame, read_csv, Series, read_table, concat
from requests.adapters import HTTPAdapter

from pandasgwas.client import ask_yes_no_question

s = requests.Session()
s.mount('https://', HTTPAdapter(max_retries=5))


def _applyDF(line):
    matchobj = re.match('\\.(.*/)((.*)-(.*)-(.*).h.tsv.gz)', line)
    if matchobj is not None:
        return Series(
            data=['/pub/databases/gwas/summary_statistics' + matchobj.group(1), matchobj.group(2), matchobj.group(3),
                  matchobj.group(4), matchobj.group(5)])
    matchobj = re.match('\\.(.*/)((GCST.*).h.tsv.gz)', line)
    return Series(
        data=['/pub/databases/gwas/summary_statistics' + matchobj.group(1), matchobj.group(2), None, matchobj.group(3),
              None])


project_dir = os.path.split(os.path.realpath(__file__))[0]
home_path = os.path.expanduser('~') + os.sep + 'pandasgwas_home'
host = 'ftp.ebi.ac.uk'
harmonised_df = read_csv(project_dir + os.sep + 'harmonised_list.txt', names=['raw'])
harmonised_df[['dir', 'file_name', 'PubMed_id', 'study_accession_id', 'EFO_trait_id']] = harmonised_df['raw'].apply(
    _applyDF)


def search(PubMed_id: str = None, study_accession_id: str = None, EFO_trait_id: str = None,
           online_index: bool = False) -> DataFrame:
    """
    Search for where data is stored based on indexing and query criteria.

    Args:
        PubMed_id: ID of PubMed.
        study_accession_id: ID of study accession.
        EFO_trait_id: ID of EFO trait.
        online_index: Whether to use an online index.

    Returns:
        A DataFrame that records where the data is stored.

    """
    if PubMed_id is None and study_accession_id is None and EFO_trait_id is None:
        warnings.warn('Since there are no input conditions, all index values will be returned.')
    if online_index:
        _download_FTP('/pub/databases/gwas/summary_statistics/', 'harmonised_list.txt')
        filter_df = read_csv(home_path + os.sep + 'harmonised_list.txt', names=['raw'])
        filter_df[['dir', 'file_name', 'PubMed_id', 'study_accession_id', 'EFO_trait_id']] = filter_df['raw'].apply(
            _applyDF)
    else:
        filter_df = harmonised_df.copy()
    if PubMed_id is not None:
        filter_df = filter_df[filter_df['PubMed_id'] == PubMed_id]
    if study_accession_id is not None:
        filter_df = filter_df[filter_df['study_accession_id'] == study_accession_id]
    if EFO_trait_id is not None:
        filter_df = filter_df[filter_df['EFO_trait_id'] == EFO_trait_id]
    return filter_df.reset_index(drop=True)


def browser(search_DF: DataFrame, interactive: bool = True) -> None:
    """
    See where the data is stored in the browser.

    Args:
        search_DF: A DataFrame that stores the FTP storage location. Obtained from calling the search function.
        interactive: Whether to make interactive prompts.

    Returns:

    """
    if len(search_DF) > 5 and interactive:
        answer = ask_yes_no_question(
            "You will have more than %s pages opened."
            "\r\nDo you still want to proceed? (Yes or No)" % len(search_DF))
        if answer == "NO":
            return
    search_DF['dir'].apply(lambda x: webbrowser.open_new_tab('https://' + host + x))


def download(search_DF: DataFrame) -> None:
    """
    Download FTP data to directory $HOME/pandasgwas_home.

    Args:
        search_DF: A DataFrame that stores the FTP storage location. Obtained from calling the search function.

    Returns:

    """
    
    os.makedirs(home_path, exist_ok=True)
    list(map(lambda x, y: _download_FTP(x, y), search_DF['dir'], search_DF['file_name']))


def _download_FTP(ftp_dir: str, file_name: str):
    # import urllib3
    # s.keep_alive = False
    # s.verify = False
    # urllib3.disable_warnings()
    # proxies = {
    #    'http': 'http://127.0.0.1:7890/',
    #    'https': 'http://127.0.0.1:7890/'
    # }
    # with s.get('https://' + host + ftp_dir + file_name, proxies=proxies, stream=True) as r:
    with s.get('https://' + host + ftp_dir + file_name, timeout=60, stream=True) as r:
        online_size = r.headers.get('content-length', 0)
        local_size = 0
        if os.path.exists(home_path + os.sep + file_name):
            local_size = os.path.getsize(home_path + os.sep + file_name)
        if local_size > 0 and (int(online_size) == local_size):
            sys.stdout.write('[SKIP]: %s has been downloaded in %s\n' % (file_name, home_path))
            return
        r.raise_for_status()
        with open(home_path + os.sep + file_name, 'wb') as f:
            i = 0
            for chunk in r.iter_content(chunk_size=1024):
                i += 1024
                sys.stdout.write('%s downloading: %.2f MB\r' % (file_name, i / 1024 / 1024))
                f.write(chunk)
        sys.stdout.write('%s(%.2f MB) has been downloaded in %s\n' % (file_name, i / 1024 / 1024, home_path))


def parse(search_DF: DataFrame, interactive: bool = True) -> DataFrame:
    """
    Resolves the specified data from the directory $HOME/pandas_home to a DataFrame.

    Args:
        search_DF: A DataFrame that stores the FTP storage location. Obtained from calling the search function.
        interactive: Whether to make interactive prompts.

    Returns:
        A DataFrame that records summary statistics.

    """
    def map_func(file_name, PubMed_id, study_accession_id, EFO_trait_id):
        one_DF = read_table(home_path + os.sep + file_name,
                            usecols=['variant_id', 'p_value', 'chromosome', 'base_pair_location',
                                     'odds_ratio', 'ci_lower', 'ci_upper', 'beta', 'standard_error',
                                     'effect_allele', 'other_allele', 'effect_allele_frequency',
                                     'hm_variant_id', 'hm_odds_ratio', 'hm_ci_lower', 'hm_ci_upper',
                                     'hm_beta', 'hm_effect_allele', 'hm_other_allele',
                                     'hm_effect_allele_frequency', 'hm_code'], compression='gzip')
        one_DF['PubMed_id'] = PubMed_id
        one_DF['study_accession_id'] = study_accession_id
        one_DF['EFO_trait_id'] = EFO_trait_id
        return one_DF

    total = sum(map(lambda x: os.path.getsize(home_path + os.sep + x), search_DF['file_name'])) / 1024 / 1024 / 1024
    if total > 1 and interactive:
        answer = ask_yes_no_question(
            "You will load more than %.2f GB data."
            "\r\nDo you still want to proceed? (Yes or No)" % total)
        if answer == "NO":
            return

    return concat(map(map_func, search_DF['file_name'], search_DF['PubMed_id'], search_DF['study_accession_id'],
                      search_DF['EFO_trait_id']), ignore_index=True)
