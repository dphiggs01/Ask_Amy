import abc
import logging
import importlib
from ask_amy.core.exceptions import CustomTypeLoadError

logger = logging.getLogger()


class Custom_Validator(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def is_valid_value(value):
        raise NotImplementedError('users must define is_valid_value to use this base class')


    @staticmethod
    def class_from_str(dotted_path):
        logger.debug("**************** entering Custom_Validator.__import_class_from_str")
        try:
            module_path, class_name = dotted_path.rsplit('.', 1)
            module = importlib.import_module(module_path)
        except ValueError as error:
            logger.critical("Error Custom_Validator.class_from_str")
            raise CustomTypeLoadError('Unable to load Custum Type: Value error for {}'.format(dotted_path)) from error

        try:
            return getattr(module, class_name)
        except AttributeError as error:
            logger.critical("Error in Custom_Validator.class_from_str path {} err={}".format(dotted_path, error))
            raise CustomTypeLoadError('Unable to load Custom Type: Attribute error for {}'.format(module, class_name)) \
                from error
