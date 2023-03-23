# summary_statistics

Functions for easy retrieval of summary statistics data based on FTP data.

## *function* search(PubMed_id: Optional[str] = None, study_accession_id: Optional[str] = None, EFO_trait_id: Optional[str] = None, online_index: bool = False) -> DataFrame
Search for where data is stored based on indexing and query criteria.
### param PubMed_id
ID of PubMed.
### param study_accession_id
ID of study accession.
### param EFO_trait_id
ID of EFO trait.
### param online_index
Whether to use an online index.

## *function* download(search_DF: DataFrame)
Download FTP data to directory $HOME/pandas_home.
### param search_DF
A DataFrame that stores the FTP storage location. Obtained from calling the search function.

## *function* browser(search_DF: DataFrame, interactive: bool = True)
See where the data is stored in the browser.
### param search_DF
A DataFrame that stores the FTP storage location. Obtained from calling the search function.
### param interactive
Whether to make interactive prompts.

## *function* parse(search_DF: DataFrame, interactive: bool = True) -> DataFrame
Resolves the specified data from the directory $HOME/pandas_home to a DataFrame.
### param search_DF
A DataFrame that stores the FTP storage location. Obtained from calling the search function.
### param interactive
Whether to make interactive prompts.