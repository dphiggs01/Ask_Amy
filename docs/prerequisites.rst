Getting Started
===============

|prereq| Before diving in there are a few prerequisites that must be satisfied:

* We will need an `Amazon Developer account <https://developer.amazon.com/>`_ to design and deploy our skills *voice user interface*
* An `AWS (Amazon Web Services) Account <https://aws.amazon.com/>`_ to deploy our skills *execution code* (we will be deploying on `AWS Lambda <https://aws.amazon.com/lambda/>`_)

.. note::

    Additional beneficial reading on getting started with Alexa Skill development can be found here with the `Amazon provided documentation <https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/requirements-to-build-a-skill>`_


Once we have our accounts setup the next step is to :ref:`install-ask-amy-label` for those with a Python 3.+
environment already installed this should be a very simple process of just calling `pip install ask_amy`.

.. code-block:: bash

   $ pip install ask_amy


The final prerequisite is setting up integration with AWS Lambda, CloudWatch & DynamoDB this is accomplish in two easy steps
first we must install the AWS CLI (Command Line Interface) and second we must create an IAM (Identity and Access Management) Role
to allow our executing code access to these services.

.. code-block:: bash

    $ pip install --upgrade --user awscli


.. note::

  Additional Amazon CLI documentation can be found here:

  * `CLI installation <http://docs.aws.amazon.com/cli/latest/userguide/installing.html>`_

  * `CLI configure <http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html>`_


.. warning::

   When configuring AWS CLI provide credentials that have the appropriate level of authority
   to deploy lambda functions.


* An IAM (Identity and Access Management) Role is required to enable CloudWatch Logging and Dynamo DB access

.. |prereq| image:: _static/icon-prereq.png
            :width: 40px
            :height: 30px
            :align: middle

