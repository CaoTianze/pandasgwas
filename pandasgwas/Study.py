from pandas import DataFrame, Series, json_normalize, set_option
import numpy
import warnings

set_option('display.max_columns', None)
set_option('display.width', 1000)
set_option('display.colheader_justify', 'center')
set_option('display.precision', 3)


class Study:
    def __init__(self, data: list = None):
        if data is None:
            data = []
        self.parse(data)

    def __str__(self) -> str:
        class_str = (
            'Study has 7 DataFrames with hierarchical dependencies.\nstudies\n|\n -platforms\n|\n -ancestries\n    '
            '|\n     -ancestral_groups\n    |\n     -countries_of_origin\n    |\n     -countries_recruitment\n|\n '
            '-geontyping_tcchnologies')
        return class_str
    
    def __repr__(self) -> str:
        return self.__str__()

    def parse(self, data: list = None):
        if data is None:
            warnings.warn("Data is None, DataFrame will be empty")
        self.raw_data = data
        if data is None or len(data) == 0:
            self.studies = DataFrame(
                columns=['initialSampleSize', 'gxe', 'gxg', 'snpCount', 'qualifier', 'imputed', 'pooled',
                         'studyDesignComment', 'accessionId', 'fullPvalueSet', 'userRequested', 'platforms',
                         'ancestries', 'genotypingTechnologies', 'replicationSampleSize', 'diseaseTrait.trait',
                         'publicationInfo.pubmedId', 'publicationInfo.publicationDate', 'publicationInfo.publication',
                         'publicationInfo.title', 'publicationInfo.author.fullname', 'publicationInfo.author.orcid'])
            self.genotyping_technologies = DataFrame(columns=['genotypingTechnology', 'accessionId'])
            self.platforms = DataFrame(columns=['manufacturer', 'accessionId'])
            self.ancestries = DataFrame(
                columns=['type', 'numberOfIndividuals', 'ancestralGroups', 'countryOfOrigin', 'countryOfRecruitment',
                         'accessionId', 'ancestryId'])
            self.ancestral_groups = DataFrame(columns=['accessionId', 'ancestryId', 'ancestralGroup'])
            self.country_of_origin = DataFrame(
                columns=['accessionId', 'ancestryId', 'majorArea', 'region', 'countryName'])
            self.country_of_recruitment = DataFrame(
                columns=['accessionId', 'ancestryId', 'majorArea', 'region', 'countryName'])
            return
        self.studies: DataFrame = json_normalize(data, max_level=2)
        self.genotyping_technologies: DataFrame = json_normalize(data, record_path=['genotypingTechnologies'],
                                                                 meta=['accessionId'])
        self.platforms: DataFrame = json_normalize(data, record_path=['platforms'], meta=['accessionId'])
        ancestries = json_normalize(data, record_path=['ancestries'], meta=['accessionId'])
        ancestries['ancestryId'] = Series(data=range(0, len(ancestries)))
        self.ancestries: DataFrame = ancestries
        ancestral_groups = ancestries[['ancestralGroups', 'accessionId', 'ancestryId']].copy()
        ancestral_groups['ancestralGroups'] = ancestral_groups['ancestralGroups'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        ancestral_groups = ancestral_groups.dropna()
        ancestral_groups = ancestral_groups.explode('ancestralGroups')
        ancestral_groups['ancestralGroup'] = ancestral_groups['ancestralGroups'].apply(
            lambda x: x['ancestralGroup'])
        ancestral_groups = ancestral_groups.drop(columns=['ancestralGroups'])
        self.ancestral_groups: DataFrame = ancestral_groups.reset_index(drop=True)
        country_of_origin = ancestries[['countryOfOrigin', 'accessionId', 'ancestryId']].copy()
        country_of_origin['countryOfOrigin'] = country_of_origin['countryOfOrigin'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        country_of_origin = country_of_origin.dropna()
        country_of_origin = country_of_origin.explode('countryOfOrigin')
        if len(country_of_origin)>0:
            country_of_origin[['majorArea', 'region', 'countryName']] = country_of_origin['countryOfOrigin'].apply(
                lambda x: Series(data=[x['majorArea'], x['region'], x['countryName']]))
        else:
            country_of_origin.assign(majorArea=[],region=[],countryName=[])
        country_of_origin = country_of_origin.drop(columns=['countryOfOrigin'])
        self.country_of_origin: DataFrame = country_of_origin.reset_index(drop=True)
        country_of_recruitment = ancestries[['countryOfRecruitment', 'accessionId', 'ancestryId']].copy()
        country_of_recruitment['countryOfRecruitment'] = country_of_recruitment['countryOfRecruitment'].apply(
            lambda x: x if len(x) > 0 else numpy.nan)
        country_of_recruitment = country_of_recruitment.dropna()
        country_of_recruitment = country_of_recruitment.explode('countryOfRecruitment')
        if len(country_of_recruitment)>0:
            country_of_recruitment[['majorArea', 'region', 'countryName']] = country_of_recruitment[
                'countryOfRecruitment'].apply(lambda x: Series([x['majorArea'], x['region'], x['countryName']]))
        else:
            country_of_recruitment.assign(majorArea=[],region=[],countryName=[])
        country_of_recruitment = country_of_recruitment.drop(columns=['countryOfRecruitment'])
        self.country_of_recruitment: DataFrame = country_of_recruitment.reset_index(drop=True)

    def __len__(self):
        return len(self.studies)

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
            raw_data_dict[j['accessionId']]=j
        sub_set = []
        for i in arr:
            if isinstance(i, str) :
                sub_set.append(raw_data_dict[i])
            elif isinstance(i, int):
                sub_set.append(raw_data[i])
            else:
                raise TypeError('Invalid item type: {}'.format(type(i)))
        return Study(sub_set)

    def __add__(self, other):
        return Study(self.raw_data + other.raw_data)

    def __sub__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['accessionId'])
            self_dict[i['accessionId']] = i
        for j in other.raw_data:
            other_key_set.add(j['accessionId'])
        sub_key = self_key_set - other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return Study(data)

    def __and__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['accessionId'])
            self_dict[i['accessionId']] = i
        for j in other.raw_data:
            other_key_set.add(j['accessionId'])
        sub_key = self_key_set & other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return Study(data)

    def __or__(self, other):
        and_dict = {}
        for i in self.raw_data:
            and_dict[i['accessionId']] = i
        for j in other.raw_data:
            and_dict[j['accessionId']] = j
        data = list(and_dict.values())
        return Study(data)

    def __xor__(self, other):
        self_key_set = set()
        and_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['accessionId'])
            and_dict[i['accessionId']] = i
        for j in other.raw_data:
            other_key_set.add(j['accessionId'])
            and_dict[j['accessionId']] = j
        sub_key = self_key_set ^ other_key_set
        data = []
        for k in sub_key:
            data.append(and_dict[k])
        return Study(data)

    def __eq__(self, other):
        if self is None or other is None:
            return self is None and other is None
        return self.raw_data == other.raw_data