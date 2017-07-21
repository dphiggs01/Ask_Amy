.. ask amy documentation master file, created by
   sphinx-quickstart on Sun Jun 25 14:33:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome
=======
.. sidebar:: *What users say*

   "ASK Amy is an easy to use framework with plenty of **goodies** to help accelerate development!"

ASK Amy adheres to a number of simple design principles that helps new developer create skills quickly and advanced
developer leverage the Alexa Skills Kit API to its full extent.



|design| Design Principles:
----------------------------
* **Separation of Concern** abstracting the text / speech of intent responses into a JSON document and providing a clear demarcation of intent processing user experience (UX) code from application code
* **Paradigm Consistency** using similar terminology and design patterns as found in the *Alexa Service* allows for a more seamless development flow between *intent schema* and *ASK Amy Skill* development
* **Extensible Framework** supports plug-able components to support *state machines* or additional *databases*
* **Microservices** approach to skill development and application integration enhances reusability of code


|features| Features:
--------------------
* **Template Skill Code Generation** creates a deploy-able skill template from a JSON intent schema
* **AWS CLI Wrapper** simplifies Lambda function creation, deployment, and CloudWatch log file dumps
* **No Code Persistence of attributes** provides automatic saving and restoration of session state across skill invocations
* **Multiple Data Scopes** supporting Request, Intent, Session, and Application scopes enhances data visibility
* **JSON to Object Marshalling** automatically converts JSON Events into Objects and Converts Reply Objects into JSON
* **State Manager** provides a simple yet powerful finite state machine that manages expected intents and required field processing
* **Sample Applications** Full functioning applications implement Amazons blueprint samples that from there Java and Node.JS github
* **Logging and log level throttling** comprehensive logging and log level setting to support development, debug, & production monitoring


|benefits| Key Benefits:
------------------------
* **Enhanced Developer Productivity** the ASK Amy framework encapsulates much of the boiler plate enabling developers to focus on the core skill functionality
* **Enhanced User Experience Design Productivity** as the UX can be developed an tweaked independent of the code
* **Improved Agility**
* **Simplified Deploy and Debug Cycles**


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   prerequisites.rst
   models.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


.. |design| image:: _static/icon-design.png
            :width: 40px
            :height: 30px
            :align: middle


.. |benefits| image:: _static/icon-benefits.png
            :width: 50px
            :height: 30px
            :align: middle


.. |features| image:: _static/icon-features.png
            :width: 50px
            :height: 40px
            :align: middle


