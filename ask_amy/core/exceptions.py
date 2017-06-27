"""
Global exception and warning classes.
"""


class ASKAmyError(Exception):
    """ Common base class for all ASK Amy exceptions."""


class ApplicationIdError(ASKAmyError):
    """The application id provided does not match application id for this skill"""


class IntentControlError(ASKAmyError):
    """The Intent Name does not map to an Intent in the IntentControl section for this skill"""


class DialogIntentError(ASKAmyError):
    """The Intent Name does not map to an Intent in the IntentControl section for this skill"""

class SessionError(ASKAmyError):
    """Error in session """
