from ask_amy.core.default_dialog import DefaultDialog
from ask_amy.core.reply import Reply

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
