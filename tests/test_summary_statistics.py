from pandasgwas.summary_statistics import search, browser, download, parse


def test_search():
    search_DF = search(PubMed_id='27918534', study_accession_id='GCST003966')
    assert len(search_DF) == 1


def test_browser():
    search_DF = search(PubMed_id='27918534', study_accession_id='GCST003966')
    browser(search_DF)
    assert True


def test_download():
    df=search(study_accession_id='GCST001198')
    download(df)
    search_DF = search(PubMed_id='20081858')
    download(search_DF)
    assert True


def test_parse():
    search_DF = search(PubMed_id='20081858')
    download(search_DF)
    df = parse(search_DF)
    assert len(df) == 9845349