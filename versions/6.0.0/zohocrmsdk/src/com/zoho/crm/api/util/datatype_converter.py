try:
    from dateutil.tz import tz
    import dateutil.parser
    from zohocrmsdk.src.com.zoho.crm.api.util.constants import Constants
    from datetime import date, datetime,time
except Exception:
    from dateutil.tz import tz
    import dateutil.parser
    from .constants import Constants
    from datetime import date, datetime,time


class DataTypeConverter(object):

    """
    This class converts JSON value to the expected object type and vice versa.
    """

    pre_converter_map = {}

    post_converter_map = {}

    @staticmethod
    def init():

        """
        The method to initialize the PreConverter and PostConverter lambda functions.
        """

        if len(DataTypeConverter.pre_converter_map) != 0 and len(DataTypeConverter.post_converter_map) != 0:
            return

        DataTypeConverter.add_to_map("String", lambda obj: str(obj), lambda obj: str(obj))
        DataTypeConverter.add_to_map("Integer", lambda obj: int(obj), lambda obj: int(obj))
        DataTypeConverter.add_to_map("Long", lambda obj: int(obj) if str(obj) != Constants.NULL_VALUE else None, lambda obj: int(obj))
        DataTypeConverter.add_to_map("Boolean", lambda obj: bool(obj), lambda obj: bool(obj))
        DataTypeConverter.add_to_map("Float", lambda obj: float(obj), lambda obj: float(obj))
        DataTypeConverter.add_to_map("Double", lambda obj: float(obj), lambda obj: float(obj))
        DataTypeConverter.add_to_map("Date", lambda obj: dateutil.parser.isoparse(obj).date(), lambda obj: obj.isoformat())
        DataTypeConverter.add_to_map("DateTime", lambda obj: dateutil.parser.isoparse(obj).astimezone(tz.tzlocal()), lambda obj: obj.replace(microsecond=0).astimezone(tz.tzlocal()).isoformat())
        DataTypeConverter.add_to_map("Object", lambda obj: DataTypeConverter.pre_convert_object_data(obj), lambda obj: DataTypeConverter.post_convert_object_data(obj))
        DataTypeConverter.add_to_map("TimeZone", lambda obj: str(obj), lambda obj: str(obj))
        DataTypeConverter.add_to_map("LocalTime", lambda obj: DataTypeConverter.string_to_local_time(obj), lambda obj: DataTypeConverter.local_time_to_sting(obj))

    @ staticmethod
    def local_time_to_sting(obj):
        return str(obj.hour) + ':' + str(obj.minute)

    @staticmethod
    def string_to_local_time(obj):
        value = str(obj).split(':')
        return time(int(value[0]), int(value[1]))

    @staticmethod
    def pre_convert_object_data(obj):
        return obj

    @staticmethod
    def post_convert_object_data(obj):

        if obj is None:
            return None
        if isinstance(obj, list):
            list_value = []
            for data in obj:
                list_value.append(DataTypeConverter.post_convert_object_data(data))

            return list_value

        elif isinstance(obj, dict):
            dict_value = {}
            for key, value in obj.items():
                dict_value[key] = DataTypeConverter.post_convert_object_data(value)

            return dict_value

        elif isinstance(obj, date):
            return DataTypeConverter.post_convert(obj, Constants.DATE_NAMESPACE)

        elif isinstance(obj, datetime):
            return DataTypeConverter.post_convert(obj, Constants.DATETIME_NAMESPACE)

        else:
            return obj

    @staticmethod
    def add_to_map(name, pre_converter, post_converter):

        """
        This method to add PreConverter and PostConverter instance.
        :param name: A str containing the data type class name.
        :param pre_converter: A pre_converter instance.
        :param post_converter: A post_converter instance.
        """

        DataTypeConverter.pre_converter_map[name] = pre_converter
        DataTypeConverter.post_converter_map[name] = post_converter

    @staticmethod
    def pre_convert(obj, data_type):

        """
        The method to convert JSON value to expected data value.
        :param obj: An object containing the JSON value.
        :param data_type: A str containing the expected method return type.
        :return: An object containing the expected data value.
        """

        DataTypeConverter.init()
        if data_type in DataTypeConverter.pre_converter_map:
            return DataTypeConverter.pre_converter_map[data_type](obj)

    @staticmethod
    def post_convert(obj, data_type):

        """
        The method to convert python data to JSON data value.
        :param obj: A object containing the python data value.
        :param data_type: A str containing the expected method return type.
        :return: An object containing the expected data value.
        """

        DataTypeConverter.init()
        if data_type in DataTypeConverter.post_converter_map:
            return DataTypeConverter.post_converter_map[data_type](obj)
