.. ask amy documentation master file, created by
   sphinx-quickstart on Sun Jun 25 14:33:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome
=======
.. sidebar:: *What users say*

   "ASK Amy is an easy to use framework with plenty of **goodies** to help accelerate development!"

ASK Amy is a fun and easy to use framework for developing Alexa Skills. We hope you will like the design approaches
we have taken to help simplify many of the complexities of developing Alexa Skills. The framework helps new skills
developers with many sample applications that can be deployed in minutes and then modified to meet specific use cases.
Advanced developers will find that although the framework provides many best practice patterns and guardrails the full
Alex Request JSON is always available for interrogation for niche cases.



|features| Key Features:
------------------------
* The **Template Skill Code Generator** creates a deploy-able skill template from an Alexa Intent Schema json file.
* A **AWS CLI Wrapper** simplifies Lambda function creation, deployment, and CloudWatch log file dumps.
* The **No Code Persistence** provides automatic saving and restoration of session state attributes across skill invocations.
* **Multiple Data Scopes** supports encapsulation of attributes at the Request, Intent, Session, and Application scopes which enhances data visibility and minimizes use of session scope attributes when it is not required or desired.
* The **JSON to Object Marshalling** feature, automatically converts Alex json Events into Python Objects and Converts Python Reply Objects into Alex json format for return to the Alexa Service.
* The **State Manager** provides a simple yet powerful finite state machine that manages *expected intents* and *required field processing*.
* Numerous **Sample Applications** are provided, demonstrating Amazon's blueprint samples from their Java and Node.JS github repos.
* Comprehensive **Logging and log level throttling** is provided to support development, debug, & production monitoring.


|benefits| Key Benefits:
------------------------
* **Enhanced Developer Productivity** The ASK Amy framework encapsulates much of the boiler plate code required for skill deployment enabling developers to focus writing core skill functionality.
* **Enhanced User Experience Design Productivity** With ASK AMY the user experience (UX) is provided in a separate json file which can be developed an tweaked independent of the skill code.
* **Improved Agility** The ASK Amy framework is designed with change in mind and can easily accommodate iterative and incremental development and deployment.
* **Simplified Deploy and Debug Cycles** Ask Amy reduces developer frustration with AWS logs and browser based deployments with directed tools supporting the specific needs of Alexa Skill development.


|design| Design Principles:
----------------------------
* **Separation of Concern** abstracting the text / speech of intent responses into a JSON document and providing a clear demarcation of intent processing user experience (UX) code from application code
* **Paradigm Consistency** using similar terminology and design patterns found in the *Alexa Service* development allows for a more seamless flow between *intent schema* and *ASK Amy Skill* development
* **Extensible Framework** supports plug-able components to support *state machines* or additional *databases*
* **Microservices** approach to skill development and application integration enhances reusability of code


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   prerequisites.rst
   getting_started.rst
   example_skills.rst
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


