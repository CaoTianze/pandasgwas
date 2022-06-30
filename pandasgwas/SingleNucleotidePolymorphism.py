from pandas import DataFrame, Series, json_normalize, set_option
import numpy
import warnings

set_option('display.max_rows', None)
set_option('display.max_columns', None)
set_option('display.width', 1000)
set_option('display.colheader_justify', 'center')
set_option('display.precision', 3)


class SingleNucleotidePolymorphism:
    def __init__(self, data: list = None):
        if data is None:
            data = []
        self.parse(data)

    def parse(self, data: list = None):
        if data is None:
            warnings.warn("Data is None, DataFrame will be empty")
        self.raw_data = data
        if data is None or len(data) == 0:
            self.single_nucleotide_polymorphisms = DataFrame(
                columns=['rsId', 'merged', 'functionalClass', 'lastUpdateDate', 'locations', 'genomicContexts'])
            self.locations = DataFrame(columns=['chromosomeName', 'chromosomePosition', 'region.name', 'rsId'])
            self.genomic_contexts = DataFrame(
                columns=['isIntergenic', 'isUpstream', 'isDownstream', 'distance', 'source', 'mappingMethod',
                         'isClosestGene', 'gene.geneName', 'gene.entrezGeneIds', 'gene.ensemblGeneIds',
                         'location.chromosomeName', 'location.chromosomePosition', 'location.region.name', 'rsId',
                         'genomicContextId'])
            self.ensembl_gene_ids = DataFrame(columns=['rsId', 'genomicContextId', 'ensemblGeneId'])
            self.entrez_gene_ids = DataFrame(columns=['rsId', 'genomicContextId', 'entrezGeneId'])
            return
        self.single_nucleotide_polymorphisms: DataFrame = json_normalize(data, max_level=2)
        self.locations: DataFrame = json_normalize(data, record_path=['locations'], meta=['rsId'])
        genomic_contexts = json_normalize(data, record_path=['genomicContexts'], meta=['rsId'])
        genomic_contexts['genomicContextId'] = Series(data=range(0, len(genomic_contexts)))
        self.genomic_contexts: DataFrame = genomic_contexts
        ensembl_gene_ids = genomic_contexts[['gene.ensemblGeneIds', 'rsId', 'genomicContextId']].copy()
        ensembl_gene_ids['gene.ensemblGeneIds'] = ensembl_gene_ids['gene.ensemblGeneIds'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        ensembl_gene_ids = ensembl_gene_ids.dropna()
        ensembl_gene_ids = ensembl_gene_ids.explode('gene.ensemblGeneIds')
        ensembl_gene_ids['ensemblGeneId'] = ensembl_gene_ids['gene.ensemblGeneIds'].apply(
            lambda x: x['ensemblGeneId'])
        ensembl_gene_ids = ensembl_gene_ids.drop(columns=['gene.ensemblGeneIds'])
        self.ensembl_gene_ids: DataFrame = ensembl_gene_ids.reset_index(drop=True)
        entrez_gene_ids = genomic_contexts[['gene.entrezGeneIds', 'rsId', 'genomicContextId']].copy()
        entrez_gene_ids['gene.entrezGeneIds'] = entrez_gene_ids['gene.entrezGeneIds'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        entrez_gene_ids = entrez_gene_ids.dropna()
        entrez_gene_ids = entrez_gene_ids.explode('gene.entrezGeneIds')
        entrez_gene_ids['entrezGeneId'] = entrez_gene_ids['gene.entrezGeneIds'].apply(
            lambda x: x['entrezGeneId'])
        entrez_gene_ids = entrez_gene_ids.drop(columns=['gene.entrezGeneIds'])
        self.entrez_gene_ids: DataFrame = entrez_gene_ids.reset_index(drop=True)

    def __len__(self):
        return len(self.single_nucleotide_polymorphisms)

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
            raw_data_dict[j['rsId']]=j
        sub_set = []
        for i in arr:
            if isinstance(i, str) :
                sub_set.append(raw_data_dict[i])
            elif isinstance(i, int):
                sub_set.append(raw_data[i])
            else:
                raise TypeError('Invalid item type: {}'.format(type(i)))
        return SingleNucleotidePolymorphism(sub_set)

    def __add__(self, other):
        return SingleNucleotidePolymorphism(self.raw_data + other.raw_data)

    def __sub__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['rsId'])
            self_dict[i['rsId']] = i
        for j in other.raw_data:
            other_key_set.add(j['rsId'])
        sub_key = self_key_set - other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return SingleNucleotidePolymorphism(data)

    def __and__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['rsId'])
            self_dict[i['rsId']] = i
        for j in other.raw_data:
            other_key_set.add(j['rsId'])
        sub_key = self_key_set & other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return SingleNucleotidePolymorphism(data)

    def __or__(self, other):
        and_dict = {}
        for i in self.raw_data:
            and_dict[i['rsId']] = i
        for j in other.raw_data:
            and_dict[j['rsId']] = j
        data = list(and_dict.values())
        return SingleNucleotidePolymorphism(data)

    def __xor__(self, other):
        self_key_set = set()
        and_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['rsId'])
            and_dict[i['rsId']] = i
        for j in other.raw_data:
            other_key_set.add(j['rsId'])
            and_dict[j['rsId']] = j
        sub_key = self_key_set ^ other_key_set
        data = []
        for k in sub_key:
            data.append(and_dict[k])
        return SingleNucleotidePolymorphism(data)

    def __eq__(self, other):
        if self is None or other is None:
            return self is None and other is None
        return self.raw_data == other.raw_data