import logging

from ask_amy.core.session import Session
from ask_amy.core.request import Request, IntentRequest


logger = logging.getLogger()


class Event(object):
    def __init__(self, event_dict):
        self._request = Request.factory(event_dict['request'])
        self._session = Session(event_dict['session'])
        self._version = event_dict['version']

    def _get_session(self):
        return self._session
    session = property(_get_session)

    def _get_request(self):
        return self._request
    request = property(_get_request)

    def _get_version(self):
        return self._version
    version = property(_get_version)

    def slot_data_to_session_attributes(self):
        logger.debug("**************** entering Event.slot_data_to_session_attributes")
        # If we have an Intent Request map the slot values to the session
        if isinstance(self._request, IntentRequest):
            slots_dict = self._request.slots
            for name in slots_dict.keys():
                # get the value for this name if available
                value = self.request.value_for_slot_name(name)
                if value is not None:
                    # If this is a 'requested_value' do we have a field to map to?
                    if name == 'requested_value':
                        if self.session.attribute_exists('slot_name'):
                            requested_value_nm = self.session.attributes['slot_name']
                            self.session.attributes[requested_value_nm] = value
                        else:
                            self.session.attributes[name] = value
                    else:
                        self.session.attributes[name] = value

    def __str__(self):
        output = 'Event[\n\tsession = {}\n\trequest = {}\n]'.format(
            self._session,
            self._request)
        return output
