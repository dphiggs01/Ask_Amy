import logging
from ask_amy.core.exceptions import IntentControlError, DialogIntentError
from ask_amy.core.dialog import Dialog
from ask_amy.core.reply import Reply

logger = logging.getLogger()


class DefaultDialog(Dialog):
    def __init__(self, dialog_dict=None):
        super().__init__(dialog_dict)

    def new_session_started(self):
        logger.debug("**************** entering DefaultDialog.new_session_started")
        pass

    def launch_request(self):
        logger.debug("**************** entering DefaultDialog.launch_request")
        try:
            self._method_name = self._sc_intent_control['AMAZON.HelpIntent']
        except KeyError as error:
            raise IntentControlError("No Key found for IntentControl: AMAZON.HelpIntent") from error

        return self.execute_method(self.method_name)

    def session_ended_request(self):
        logger.debug("**************** entering DefaultDialog.session_ended_request")
        logger.debug("request.request_type {}".format(self.request.request_type))
        logger.debug("request.reason {}".format(self.request.reason))
        logger.debug("request.locale {}".format(self.request.locale))
        logger.debug("request.timestamp {}".format(self.request.timestamp))
        logger.debug("request.request_id {}".format(self.request.request_id))
        return {}

    def intent_request(self):
        """
        Executes the method related to the intent sent from Alexa.
        The methods are mapped in the skill_configuration.json file under the attribute name 'intentControl'

        Returns: Response object

        """
        logger.debug("**************** entering DefaultDialog.intent_request")
        try:
            self._method_name = self._sc_intent_control[self.request.intent_name]
        except KeyError as error:
            raise IntentControlError("No Key found for IntentControl: {}".format(self.request.intent_name)) from error
        return self.execute_method(self.method_name)

    def default_stop_intent(self):
        logger.debug("**************** entering DefaultDialog.default_stop_intent")
        return self.handle_default_intent(use_default_message=True)

    def default_cancel_intent(self):
        logger.debug("**************** entering DefaultDialog.default_cancel_intent")
        return self.handle_default_intent(use_default_message=True)

    def handle_default_intent(self, use_default_message=None):
        logger.debug('**************** entering DefaultDialog.handle_default_intent.{}'.format(self.method_name))
        try:
            reply_dialog = self.reply_dialog[self.method_name]
        except KeyError as error:
            if use_default_message is not None:
                reply_dialog = {
                    "speech_out_text": "Good Bye.",
                    "should_end_session": True}
            else:
                raise DialogIntentError("No key found for Intent in Dialog: {}".format(self.method_name)) from error

        reply = Reply.build(reply_dialog, self.session)
        return reply
