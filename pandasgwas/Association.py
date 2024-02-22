from pandas import DataFrame, Series, json_normalize, set_option
import numpy
import warnings

set_option('display.max_columns', None)
set_option('display.width', 1000)
set_option('display.colheader_justify', 'center')
set_option('display.precision', 3)


class Association:
    """
    Python class to represent a set of GWAS Catalog Association. For more information, see "[GWAS CATALOG API Guide](https://www.ebi.ac.uk/gwas/rest/docs/api)"

    ```Python
    # get Association by study_id
    from pandasgwas.get_associations import get_associations

    associations = get_associations(study_id='GCST000854')
    ```

    Attributes:
        associations: pandas.DataFrame. A DataFrame to represent all queried Associations from GWAS Catalog REST API
        loci: pandas.DataFrame. A DataFrame to represent column loci from associations
        strongest_risk_alleles: pandas.DataFrame. A DataFrame to represent column strongest_risk_alleles from loci
        author_reported_genes: pandas.DataFrame. A DataFrame to represent column author_reported_genes from loci
        entrez_gene_ids: pandas.DataFrame. A DataFrame to represent column entrez_gene_ids from author_reported_genes
        ensembl_gene_ids: pandas.DataFrame. A DataFrame to represent column entrez_gene_ids from author_reported_genes

    """
    def __init__(self, data: list = None):
        if data is None:
            data = []
        self.parse(data)

    def __str__(self) -> str:
        class_str = (
            'Association has 6 DataFrames with hierarchical dependencies.\nassociations\n|\n -loci\n|\n '
            '-strongext_risk_alleles\n|\n -author_reported_genes\n    |\n     -ensembl_gene_ids\n    |\n     '
            '-entrez_gene_ids')
        return class_str

    def __repr__(self) -> str:
        return self.__str__()
    

    def parse(self, data: list = None):
        if data is None:
            warnings.warn("Data is None, DataFrame will be empty")
        self.raw_data = data
        if data is None or len(data) == 0:
            self.associations = DataFrame(
                columns=['riskFrequency', 'pvalueDescription', 'pvalueMantissa', 'pvalueExponent', 'multiSnpHaplotype',
                         'snpInteraction', 'snpType', 'standardError', 'range', 'description', 'orPerCopyNum',
                         'betaNum', 'betaUnit', 'betaDirection', 'loci', 'lastMappingDate', 'lastUpdateDate', 'pvalue',
                         'associationId'])
            self.loci = DataFrame(
                columns=['haplotypeSnpCount', 'description', 'strongestRiskAlleles', 'authorReportedGenes',
                         'associationId', 'lociId'])
            self.strongest_risk_alleles = DataFrame(
                columns=['associationId', 'lociId', 'riskAlleleName', 'riskFrequency', 'genomeWide', 'limitedList'])
            self.author_reported_genes = DataFrame(
                columns=['associationId', 'lociId', 'geneName', 'entrezGeneIds', 'ensemblGeneIds',
                         'authorReportedGeneId'])
            self.entrez_gene_ids = DataFrame(
                columns=['associationId', 'lociId', 'authorReportedGeneId', 'entrezGeneId'])
            self.ensembl_gene_ids = DataFrame(
                columns=['associationId', 'lociId', 'authorReportedGeneId', 'ensemblGeneId'])
            return
        self.associations: DataFrame = json_normalize(data, max_level=2)

        loci = json_normalize(data, record_path=['loci'], meta=['associationId'])
        loci['lociId'] = Series(data=range(0, len(loci)))
        self.loci: DataFrame = loci
        strongest_risk_alleles = loci[['strongestRiskAlleles', 'associationId', 'lociId']].copy()
        strongest_risk_alleles['strongestRiskAlleles'] = strongest_risk_alleles['strongestRiskAlleles'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        strongest_risk_alleles = strongest_risk_alleles.dropna()
        strongest_risk_alleles = strongest_risk_alleles.explode('strongestRiskAlleles')
        strongest_risk_alleles[['riskAlleleName', 'riskFrequency', 'genomeWide', 'limitedList']] = \
            strongest_risk_alleles[
                'strongestRiskAlleles'].apply(
                lambda x: Series(data=[x['riskAlleleName'], x['riskFrequency'], x['genomeWide'], x['limitedList']]))
        strongest_risk_alleles = strongest_risk_alleles.drop(columns=['strongestRiskAlleles'])
        self.strongest_risk_alleles: DataFrame = strongest_risk_alleles.reset_index(drop=True)

        author_reported_genes = loci[['authorReportedGenes', 'associationId', 'lociId']].copy()
        author_reported_genes['authorReportedGenes'] = author_reported_genes['authorReportedGenes'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        author_reported_genes = author_reported_genes.dropna()
        author_reported_genes = author_reported_genes.explode('authorReportedGenes')
        author_reported_genes[['geneName', 'entrezGeneIds', 'ensemblGeneIds']] = author_reported_genes[
            'authorReportedGenes'].apply(
            lambda x: Series(data=[x['geneName'], x['entrezGeneIds'], x['ensemblGeneIds']]))
        author_reported_genes = author_reported_genes.drop(columns=['authorReportedGenes'])
        author_reported_genes['authorReportedGeneId'] = Series(data=range(0, len(author_reported_genes)))
        self.author_reported_genes: DataFrame = author_reported_genes.reset_index(drop=True)

        entrez_gene_ids = author_reported_genes[
            ['entrezGeneIds', 'associationId', 'lociId', 'authorReportedGeneId']].copy()
        entrez_gene_ids['entrezGeneIds'] = entrez_gene_ids['entrezGeneIds'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        entrez_gene_ids = entrez_gene_ids.dropna()
        entrez_gene_ids = entrez_gene_ids.explode('entrezGeneIds')
        entrez_gene_ids['entrezGeneId'] = entrez_gene_ids[
            'entrezGeneIds'].apply(
            lambda x: x['entrezGeneId'])
        entrez_gene_ids = entrez_gene_ids.drop(columns=['entrezGeneIds'])
        self.entrez_gene_ids: DataFrame = entrez_gene_ids.reset_index(drop=True)

        ensembl_gene_ids = author_reported_genes[
            ['ensemblGeneIds', 'associationId', 'lociId', 'authorReportedGeneId']].copy()
        ensembl_gene_ids['ensemblGeneIds'] = ensembl_gene_ids['ensemblGeneIds'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        ensembl_gene_ids = ensembl_gene_ids.dropna()
        ensembl_gene_ids = ensembl_gene_ids.explode('ensemblGeneIds')
        ensembl_gene_ids['ensemblGeneId'] = ensembl_gene_ids[
            'ensemblGeneIds'].apply(
            lambda x: x['ensemblGeneId'])
        ensembl_gene_ids = ensembl_gene_ids.drop(columns=['ensemblGeneIds'])
        self.ensembl_gene_ids: DataFrame = ensembl_gene_ids.reset_index(drop=True)

    def __len__(self):
        return len(self.associations)

    def __getitem__(self, item):
        if isinstance(item, str) or isinstance(item, int):
            arr = [item]
        elif isinstance(item, list) or isinstance(item, tuple) or isinstance(item, range):
            arr = item
        elif isinstance(item, slice):
            start, stop, step = item.indices(len(self))
            arr = list(range(start, stop, step))
        else:
            raise TypeError('Invalid argument type: {}'.format(type(item)))
        raw_data = self.raw_data
        raw_data_dict = {}
        for j in raw_data:
            raw_data_dict[j['associationId']]=j
        sub_set = []
        for i in arr:
            if isinstance(i, str) :
                sub_set.append(raw_data_dict[i])
            elif isinstance(i, int):
                sub_set.append(raw_data[i])
            else:
                raise TypeError('Invalid item type: {}'.format(type(i)))
        return Association(sub_set)

    def __add__(self, other):
        return Association(self.raw_data + other.raw_data)

    def __sub__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['associationId'])
            self_dict[i['associationId']] = i
        for j in other.raw_data:
            other_key_set.add(j['associationId'])
        sub_key = self_key_set - other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return Association(data)

    def __and__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['associationId'])
            self_dict[i['associationId']] = i
        for j in other.raw_data:
            other_key_set.add(j['associationId'])
        sub_key = self_key_set & other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return Association(data)

    def __or__(self, other):
        and_dict = {}
        for i in self.raw_data:
            and_dict[i['associationId']] = i
        for j in other.raw_data:
            and_dict[j['associationId']] = j
        data = list(and_dict.values())
        return Association(data)

    def __xor__(self, other):
        self_key_set = set()
        and_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['associationId'])
            and_dict[i['associationId']] = i
        for j in other.raw_data:
            other_key_set.add(j['associationId'])
            and_dict[j['associationId']] = j
        sub_key = self_key_set ^ other_key_set
        data = []
        for k in sub_key:
            data.append(and_dict[k])
        return Association(data)

    def __eq__(self, other):
        if self is None or other is None:
            return self is None and other is None
        return self.raw_data == other.raw_data
