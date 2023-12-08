from pandas import DataFrame, json_normalize, set_option
import warnings

set_option('display.max_columns', None)
set_option('display.width', 1000)
set_option('display.colheader_justify', 'center')
set_option('display.precision', 3)


class Trait:
    def __init__(self, data: list = None):
        if data is None:
            data = []
        self.parse(data)

    def __str__(self) -> str:
        class_str='''Trait has 1 DataFremes with hierarchical dependencies.\nefo_traits'''
        return class_str
    def __repr__(self) -> str:
        return self.__str__()
    

    def __len__(self):
        return len(self.efo_traits)

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
            raw_data_dict[j['shortForm']]=j
        sub_set = []
        for i in arr:
            if isinstance(i, str) :
                sub_set.append(raw_data_dict[i])
            elif isinstance(i, int):
                sub_set.append(raw_data[i])
            else:
                raise TypeError('Invalid item type: {}'.format(type(i)))
        return Trait(sub_set)

    def parse(self, data: list = None):
        if data is None:
            warnings.warn("Data is None, DataFrame will be empty")
        self.raw_data = data
        if data is None or len(data) == 0:
            self.efo_traits = DataFrame(columns=['trait', 'uri', 'shortForm'])
            return
        self.efo_traits: DataFrame = json_normalize(data, max_level=2)

    def __add__(self, other):
        return Trait(self.raw_data + other.raw_data)

    def __sub__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['shortForm'])
            self_dict[i['shortForm']] = i
        for j in other.raw_data:
            other_key_set.add(j['shortForm'])
        sub_key = self_key_set - other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return Trait(data)

    def __and__(self, other):
        self_key_set = set()
        self_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['shortForm'])
            self_dict[i['shortForm']] = i
        for j in other.raw_data:
            other_key_set.add(j['shortForm'])
        sub_key = self_key_set & other_key_set
        data = []
        for k in sub_key:
            data.append(self_dict[k])
        return Trait(data)

    def __or__(self, other):
        and_dict = {}
        for i in self.raw_data:
            and_dict[i['shortForm']] = i
        for j in other.raw_data:
            and_dict[j['shortForm']] = j
        data = list(and_dict.values())
        return Trait(data)

    def __xor__(self, other):
        self_key_set = set()
        and_dict = {}
        other_key_set = set()
        for i in self.raw_data:
            self_key_set.add(i['shortForm'])
            and_dict[i['shortForm']] = i
        for j in other.raw_data:
            other_key_set.add(j['shortForm'])
            and_dict[j['shortForm']] = j
        sub_key = self_key_set ^ other_key_set
        data = []
        for k in sub_key:
            data.append(and_dict[k])
        return Trait(data)


    def __eq__(self, other):
        if self is None or other is None:
            return self is None and other is None
        return self.raw_data == other.raw_data
