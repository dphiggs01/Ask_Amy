import logging

from ask_amy.core.event import Event
from ask_amy.core.exceptions import ApplicationIdError
from ask_amy.core.object_dictionary import ObjectDictionary

logger = logging.getLogger()


class Dialog(ObjectDictionary):
    def __init__(self, dialog_dict=None):
        super().__init__(dialog_dict)
        self._event = None
        self._intent_name = None

        self._sc_application_id = self.get_value_from_dict(['applicationId'])

        self._sc_request_control = {
            "LaunchRequest": "launch_request",
            "IntentRequest": "intent_request",
            "SessionEndedRequest": "session_ended_request"
        }
        self._sc_intent_control = self.get_value_from_dict(['intentControl'])

    def _get_event(self):
        return self._event
    event = property(_get_event)

    def _get_session(self):
        return self._event.session
    session = property(_get_session)

    def _get_request(self):
        return self._event.request
    request = property(_get_request)

    def _get_version(self):
        return self._event.version
    version = property(_get_version)

    def _get_application_id(self):
        return self._sc_application_id
    application_id = property(_get_application_id)

    def _get_intent_name(self):
        return self._intent_name
    intent_name = property(_get_intent_name)

    def _get_reply_dialog(self):
        return self._obj_dict
    reply_dialog = property(_get_reply_dialog)

    # todo deprecate replace with property 'reply_dialog'
    def get_intent_details(self, intent_name):
        return self.get_value_from_dict([intent_name])

    def get_expected_intent_for_data(self, data_name):
        return self.get_value_from_dict(['slots', data_name, 'expected_intent'])

    def get_re_prompt_for_slot_data(self, data_name):
        slot_data_details = self.get_value_from_dict(['slots', data_name])
        if 're_prompt_text' in slot_data_details:
            slot_data_details['speech_out_text'] = slot_data_details['re_prompt_text']
            del slot_data_details['re_prompt_text']
        if 're_prompt_ssml' in slot_data_details:
            slot_data_details['speech_out_text'] = slot_data_details['re_prompt_ssml']
            del slot_data_details['re_prompt_ssml']
        slot_data_details['should_end_session'] = False
        return slot_data_details

    def get_slot_data_details(self, data_name):
        slot_data_details = self.get_value_from_dict(['slots', data_name])
        slot_data_details['should_end_session'] = False
        return slot_data_details

    def begin(self, event_dict):
        logger.debug("**************** entering Dialog.begin")
        self._event = Event(event_dict)
        logger.debug("####### event={}".format(self._event))

        # If we have and application id in our configuration see if it matches the
        # application id in the event
        if self._sc_application_id:
            if self.session.application_id != self._sc_application_id:
                raise ApplicationIdError("Invalid Application ID")

        # If we are starting a new session then call new_session_started.
        # This methods may be overridden on the skills derived class
        if self.session.is_new_session:
            self.new_session_started()


        # Get the request type from the event and execute the mapped method
        # This methods may be overridden on the skills derived class
        # Current request may be  "LaunchRequest", "IntentRequest", "SessionEndedRequest"
        request_type = self.request.request_type
        method_name = self._sc_request_control[request_type]
        return self.execute_method(method_name)

    def execute_method(self, method_name):
        method = getattr(self, method_name)
        return method()
