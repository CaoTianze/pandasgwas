from pandasgwas.summary_statistics import search, browser, download


def test_search():
    search_DF = search(PubMed_id='27918534', study_accession_id='GCST003966')
    assert len(search_DF) == 1


def test_browser():
    search_DF = search(PubMed_id='27918534', study_accession_id='GCST003966')
    browser(search_DF)
    assert True


def test_download():
    search_DF = search(PubMed_id='27918534', study_accession_id='GCST003966')
    search_DF = search(EFO_trait_id='EFO_0009934')
    download(search_DF)
    assert True
