import functools

import requests
import json
import progressbar
from typing import List, Dict
import re

from cachetools import TTLCache
from requests.adapters import HTTPAdapter

cache = TTLCache(maxsize=1024*1024, ttl=60 * 60 * 24)


def cache_get(url, s):
    if url in cache:
        return cache[url]
    res = s.get(url)
    if res.status_code == 200:
        cache[url] = res
    return res


def get_studies(url: str, interactive: bool = True) -> List[Dict]:
    with requests.Session() as s:
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = cache_get(url, s)
        if r.status_code == 200:
            parsed_data = json.loads(r.text, object_hook=remove_links)
            if parsed_data.get('_embedded') is not None:
                study_list = parsed_data.get('_embedded').get("studies")
                if parsed_data.get('page') is not None and parsed_data.get('page').get('totalPages') > 1:
                    if parsed_data.get('page').get('totalPages') > 100 and interactive:
                        answer = ask_yes_no_question(
                            "You are about to download to many data from the GWAS Catalog.\r\nThis might take several "
                            "minutes.\r\nDo you still want to proceed? (Yes or No)")
                        if answer == "NO":
                            return []
                    bar = progressbar.ProgressBar(max_value=parsed_data.get('page').get('totalPages')-1).start()
                    for i in range(1, parsed_data.get('page').get('totalPages')):
                        format_url = '%s?page=%d&size=20' % (url, i)
                        if '?' in url:
                            format_url = '%s&page=%d&size=20' % (url, i)
                        # print('http req:'+format_url)

                        bar.update(i)
                        r = cache_get(format_url, s)
                        if r.status_code == 200:
                            study_list.extend(
                                json.loads(r.text, object_hook=remove_links).get('_embedded').get("studies"))
                        else:
                            raise Exception('The request for %s failed: response code was %d' % (format_url, r.status_code))
                    bar.finish()
                return study_list
            else:
                return [parsed_data]
        elif r.status_code == 404:
            return []
        else:
            print('The request for %s failed: response code was %d' % (url, r.status_code))


def get_SNPs(url: str, interactive: bool = True) -> List[Dict]:
    with requests.Session() as s:
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = cache_get(url, s)
        if r.status_code == 200:
            parsed_data = json.loads(r.text, object_hook=remove_links)
            if parsed_data.get('_embedded') is not None:
                variant_list = parsed_data.get('_embedded').get("singleNucleotidePolymorphisms")
                if parsed_data.get('page') is not None and parsed_data.get('page').get('totalPages') > 1:
                    if parsed_data.get('page').get('totalPages') > 100 and interactive:
                        answer = ask_yes_no_question(
                            "You are about to download to many data from the GWAS Catalog.\r\nThis might take several "
                            "minutes.\r\nDo you still want to proceed? (Yes or No)")
                        if answer == "NO":
                            return []
                    bar = progressbar.ProgressBar(max_value=parsed_data.get('page').get('totalPages')-1).start()
                    for i in range(1, parsed_data.get('page').get('totalPages')):
                        format_url = '%s?page=%d&size=20' % (url, i)
                        if '?' in url:
                            format_url = '%s&page=%d&size=20' % (url, i)
                        # print('http req:'+format_url)
                        bar.update(i)
                        r = cache_get(format_url, s)
                        if r.status_code == 200:
                            variant_list.extend(
                                json.loads(r.text, object_hook=remove_links).get('_embedded').get(
                                    "singleNucleotidePolymorphisms"))
                        else:
                            raise Exception('The request for %s failed: response code was %d' % (format_url, r.status_code))
                    bar.finish()
                return variant_list
            else:
                return [parsed_data]
        elif r.status_code == 404:
            return []
        else:
            print('The request for %s failed: response code was %d' % (url, r.status_code))


def get_traits(url: str, interactive: bool = True) -> List[Dict]:
    with requests.Session() as s:
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = cache_get(url, s)
        if r.status_code == 200:
            parsed_data = json.loads(r.text, object_hook=remove_links)
            if parsed_data.get('_embedded') is not None:
                trait_list = parsed_data.get('_embedded').get("efoTraits")
                if parsed_data.get('page') is not None and parsed_data.get('page').get('totalPages') > 1:
                    if parsed_data.get('page').get('totalPages') > 100 and interactive:
                        answer = ask_yes_no_question(
                            "You are about to download to many data from the GWAS Catalog.\r\nThis might take several "
                            "minutes.\r\nDo you still want to proceed? (Yes or No)")
                        if answer == "NO":
                            return []
                    bar = progressbar.ProgressBar(max_value=parsed_data.get('page').get('totalPages')-1).start()
                    for i in range(1, parsed_data.get('page').get('totalPages')):
                        format_url = '%s?page=%d&size=20' % (url, i)
                        if '?' in url:
                            format_url = '%s&page=%d&size=20' % (url, i)
                        # print('http req:'+format_url)
                        bar.update(i)
                        r = cache_get(format_url, s)
                        if r.status_code == 200:
                            trait_list.extend(
                                json.loads(r.text, object_hook=remove_links).get('_embedded').get("efoTraits"))
                        else:
                            raise Exception('The request for %s failed: response code was %d' % (format_url, r.status_code))
                    bar.finish()
                return trait_list
            else:
                return [parsed_data]
        elif r.status_code == 404:
            return []
        else:
            print('The request for %s failed: response code was %d' % (url, r.status_code))


def get_associations(url: str, interactive: bool = True) -> List[Dict]:
    with requests.Session() as s:
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = cache_get(url, s)
        if r.status_code == 200:
            parsed_data = json.loads(r.text, object_hook=remove_links_get_id)
            if parsed_data.get('_embedded') is not None:
                association_list = parsed_data.get('_embedded').get("associations")
                if parsed_data.get('page') is not None and parsed_data.get('page').get('totalPages') > 1:
                    if parsed_data.get('page').get('totalPages') > 100 and interactive:
                        answer = ask_yes_no_question(
                            "You are about to download to many data from the GWAS Catalog.\r\nThis might take several "
                            "minutes.\r\nDo you still want to proceed? (Yes or No)")
                        if answer == "NO":
                            return []
                    bar = progressbar.ProgressBar(max_value=parsed_data.get('page').get('totalPages')-1).start()
                    for i in range(1, parsed_data.get('page').get('totalPages')):
                        format_url = '%s?page=%d&size=20' % (url, i)
                        if '?' in url:
                            format_url = '%s&page=%d&size=20' % (url, i)
                        # print('http req:'+format_url)
                        bar.update(i)
                        r = cache_get(format_url, s)
                        if r.status_code == 200:
                            association_list.extend(
                                json.loads(r.text, object_hook=remove_links_get_id).get('_embedded').get(
                                    "associations"))
                        else:
                            raise Exception('The request for %s failed: response code was %d' % (format_url, r.status_code))
                    bar.finish()
                return association_list
            else:
                return [parsed_data]
        elif r.status_code == 404:
            return []
        else:
            print('The request for %s failed: response code was %d' % (url, r.status_code))


def ask_yes_no_question(question: str) -> str:
    yes_no_answer = ""
    while yes_no_answer != "YES" and yes_no_answer != "NO":
        yes_no_answer = input(question).upper()
    return yes_no_answer


def remove_links(d: dict):
    temp = {}
    for a in d.keys():
        if a != '_links':
            temp[a] = d[a]
    return temp


def remove_links_get_id(d: dict):
    temp = {}
    for a in d.keys():
        if a != '_links':
            temp[a] = d[a]
        elif 'self' in d['_links'] and not (re.match('.*associations/(.*)', d['_links']['self']['href']) is None):
            temp['associationId'] = re.match('.*associations/(.*)', d['_links']['self']['href']).group(1)
    return temp


def get_child_efo(url: str, interactive: bool = True) -> List[Dict]:
    with requests.Session() as s:
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = cache_get(url, s)
        if r.status_code == 200:
            parsed_data = json.loads(r.text, object_hook=remove_links)
            if parsed_data.get('_embedded') is not None:
                terms = parsed_data.get('_embedded').get("terms")
                if parsed_data.get('page') is not None and parsed_data.get('page').get('totalPages') > 1:
                    if parsed_data.get('page').get('totalPages') > 100 and interactive:
                        answer = ask_yes_no_question(
                            "You are about to download to many data from the GWAS Catalog.\r\nThis might take several "
                            "minutes.\r\nDo you still want to proceed? (Yes or No)")
                        if answer == "NO":
                            return []
                    bar = progressbar.ProgressBar(max_value=parsed_data.get('page').get('totalPages') - 1).start()
                    for i in range(1, parsed_data.get('page').get('totalPages')):
                        format_url = '%s?page=%d&size=20' % (url, i)
                        if '?' in url:
                            format_url = '%s&page=%d&size=20' % (url, i)
                        # print('http req:'+format_url)

                        bar.update(i)
                        r = cache_get(format_url, s)
                        if r.status_code == 200:
                            terms.extend(
                                json.loads(r.text, object_hook=remove_links).get('_embedded').get("terms"))
                        else:
                            raise Exception('The request for %s failed: response code was %d' % (format_url, r.status_code))
                    bar.finish()
                return terms
            else:
                return []
        elif r.status_code == 404:
            return []
        else:
            print('The request for %s failed: response code was %d' % (url, r.status_code))