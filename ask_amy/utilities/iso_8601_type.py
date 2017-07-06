import logging

logger = logging.getLogger()


class ISO8601_Validator(object):
    @staticmethod
    def is_valid_value(value, iso_type):
        valid = False
        if iso_type == 'AMAZON.NUMBER':
            try:
                int(value)
                valid = True
            except ValueError:
                logger.debug("Value in slot not a valid AMAZON.NUMBER")

        if iso_type == 'AMAZON.TIME':
            if ':' in value:
                hours_str, minutes_str = value.split(':')
                try:
                    hours = int(hours_str)
                    minutes = int(minutes_str)
                    if 0 <= hours <= 23 and 0 <= minutes <= 59:
                        valid = True
                except ValueError:
                    logger.debug("Value in slot not a valid AMAZON.TIME")

            elif value in ['NI', 'MO', 'AF', 'EV']:
                valid = True
        return valid
