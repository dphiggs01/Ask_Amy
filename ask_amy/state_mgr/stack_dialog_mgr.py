from ask_amy.core.default_dialog import DefaultDialog
from ask_amy.core.request import IntentRequest
from ask_amy.core.reply import Reply
from ask_amy.utilities.iso_8601_type import ISO8601_Validator
from ask_amy.utilities.custom_type import Custom_Validator
from ask_amy.core.exceptions import CustomTypeLoadError
from functools import wraps
import logging

logger = logging.getLogger()

class StackDialogManager(DefaultDialog):

    def requested_value_intent(self):
        logger.debug('**************** entering StackDialogManager.requested_value_intent')

        established_dialog = self.peek_established_dialog()
        if established_dialog != self.intent_name:
            return self.handle_session_end_confused()
        else:
            self.pop_established_dialog()
            established_dialog = self.peek_established_dialog()
            self._intent_name = established_dialog
            return self.execute_method(established_dialog)

    def redirect_to_initialize_dialog(self,intent_name):
        self._intent_name = intent_name
        return self.execute_method(intent_name)

    def is_good_state(self):
        logger.debug('**************** entering StackDialogManager.is_good_state')
        state_good = True
        established_dialog = self.peek_established_dialog()
        if established_dialog is not None:
            if established_dialog != self.intent_name:
                state_good = False
        else:
            self.push_established_dialog(self.intent_name)
        return state_good

    def required_fields_process(self, required_fields):
        reply_dict = None
        for key in required_fields:
            if not self.session.attribute_exists(key):
                expected_intent = self.get_expected_intent_for_data(key)
                self.push_established_dialog(expected_intent)
                self.session.attributes['slot_name'] = key
                reply_slot_dict = self.get_slot_data_details(key)
                return Reply.build(reply_slot_dict, self.session)

        return reply_dict

    def get_expected_intent_for_data(self, data_name):
        return self.get_value_from_dict(['slots', data_name, 'expected_intent'])

    def handle_session_end_confused(self):
        logger.debug('**************** entering StackDialogManager.handle_session_end_confused')
        # can we re_prompt?
        if not self.session.attribute_exists('retry_attempted'):
            prompt_dict = {"speech_out_text": "Could you please repeat or say help.",
                           "should_end_session": False}

            if self.session.attribute_exists('slot_name'):
                requested_value_nm = self.session.attributes['slot_name']
                prompt_dict = self.get_re_prompt_for_slot_data(requested_value_nm)

            self.session.attributes['retry_attempted'] = True
            return Reply.build(prompt_dict, self.session)
        else:
            # we are done
            self._intent_name = 'handle_session_end_confused'
            return self.handle_default_intent()


    def peek_established_dialog(self):
        logger.debug("**************** entering StackDialogManager.peek_established_dialog")
        ret_val = None
        if self.session.attribute_exists('established_conversation'):
            dialog_stack = self.session.attributes['established_conversation']
            ret_val = dialog_stack[len(dialog_stack) - 1]
        return ret_val

    def push_established_dialog(self, intent_name):
        logger.debug("**************** entering Dialog.push_established_dialog")
        if self.session.attribute_exists('established_conversation'):
            dialog_stack = self.session.attributes['established_conversation']
        else:
            dialog_stack = []
        dialog_stack.append(intent_name)
        self.session.attributes['established_conversation'] = dialog_stack
        return dialog_stack

    def pop_established_dialog(self):
        logger.debug("**************** entering StackDialogManager.pop_established_dialog")
        ret_val = None
        if self.session.attribute_exists('established_conversation'):
            dialog_stack = self.session.attributes['established_conversation']
            ret_val = dialog_stack.pop()
        return ret_val

    def reset_established_dialog(self):
        logger.debug("**************** entering StackDialogManager.reset_established_dialog")
        ret_val = None
        if self.session.attribute_exists('established_conversation'):
            dialog_stack = self.session.attributes['established_conversation']
            del dialog_stack[:]
        return ret_val

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

    def slot_data_to_session_attributes(self):
        logger.debug("**************** entering StackDialogManager.slot_data_to_session_attributes")
        # If we have an Intent Request map the slot values to the session
        if isinstance(self.event.request, IntentRequest):
            slots_dict = self.event.request.slots
            for name in slots_dict.keys():
                # get the value for this name if available
                value = self.request.value_for_slot_name(name)
                if value is not None:
                    # If this is a 'requested_value' do we have a field to map to?
                    if name == 'requested_value':
                        if self.session.attribute_exists('slot_name'):
                            name = self.session.attributes['slot_name']

                    if self.validate_slot_data_type(name, value):
                            self.session.attributes[name] = value



    def validate_slot_data_type(self, name, value):
        logger.debug("**************** entering StackDialogManager.validate_slot_data_type")
        slot_type = self.get_value_from_dict(['slots', name, 'type'])
        valid = True
        if slot_type is None:
            return valid # If type is not defined skip validation test
        else:
            if slot_type.startswith('AMAZON.'):
                valid = ISO8601_Validator.is_valid_value(value, slot_type)
            else:
                try:
                    validator = Custom_Validator.class_from_str(slot_type)
                    valid = validator.is_valid_value(value)
                except CustomTypeLoadError:
                    logger.debug("Unable to load {}".format(slot_type))
                    valid = True

        return valid



def required_fields(fields):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            obj = args[0]
            if isinstance(obj,StackDialogManager):
                obj.slot_data_to_session_attributes()
                need_additional_data = obj.required_fields_process(fields)
                if need_additional_data is not None:
                    return need_additional_data

                # print(fields)
                # print(args)
                # print(kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator
