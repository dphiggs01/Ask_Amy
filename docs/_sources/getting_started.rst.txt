.. _getting-started-label:

Getting Started
===============

The typical first application a programmer writes when working with a new language or framework is the *Hello World*
application in which we get a minimal thread of execute to demonstrate base functionality. For our first skill we will
be deploying an simple Fact telling skill, this is essentially the *Hello World* of Alexa skills but since the facts can
be easily changed and updated this is actually a useful and fun initial skill to deploy and later modify.

.. note::

    Our fact skill is based upon the `Space Geek Skill
    <https://github.com/amzn/alexa-skills-kit-java/tree/master/samples/src/main/java/spacegeek>`_
    a demo skill written by the Amazon developer team for the Java programming language.



Deploying our first skill
-------------------------

.. sidebar:: *Expected Time Under 10 Minutes*

   Once you have a functioning **ASK Amy** environment the time to create and deploy a pre build skill is *under 10 minutes*
   and with a little bit of experience it can be *under 5 minutes*.

There are two primary tasks in building and deploying a skill the **first** is constructing the *User Interaction Model*
and the **second** is *coding* of the behavior of the interactions.

The Alexa interaction with our skill would be similar to the below:

    | **User**: "Alexa, ask Obama fact to give me a fact."
    | **Alexa**: "Did you know : ..."


To deploy our example skill:

* Clone the **ASK Amy** examples.

    .. code-block:: bash

        $ git clone https://github.com/dphiggs01/ask_amy_example_skills.git

* Edit the `alexa_obama_fact_skill/cli_config.json` and update aws_role with your :ref:`aws-lambda-role-label`.

    .. code-block:: python

        {
            "skill_name": "alexa_obama_fact_skill",
            "skill_home_dir": ".",
            "aws_region": "us-east-1",
            "aws_profile": "default",
            "aws_role": "arn:aws:iam::***********:role/alexa_skill_role",

            "lambda_runtime": "python3.6",
            "lambda_handler": "ask_amy.lambda_function.lambda_handler",
            "lambda_timeout": "5",
            "lambda_memory": "128",
            "lambda_zip": "alexa_skill.zip",

            "ask_amy_dev": false,
            "ask_amy_home_dir": ""
        }


* Create the AWS Lambda Function by executing the `ask-amy-cli create_lambda ...` command below.

    .. code-block:: bash

        $ ask-amy-cli create_lambda --deploy-json-file cli_config.json
        {
            "add_trigger": {
                "Statement": "{\"Sid\":\"al....
            },
            "create_function": {
                "Role": "arn:aws:iam::095547219887:role/alexa_skill_role",
                "MemorySize": 128,
                "CodeSize": 69157,
                "Description": "alexa_obama_fact_skill",
                "Runtime": "python3.6",
                "FunctionName": "alexa_obama_fact_skill",
                "TracingConfig": {
                    "Mode": "PassThrough"
                },
                "Version": "$LATEST",
                "FunctionArn": "arn:aws:lambda:us-east-1:095547219887:function:alexa_obama_fact_skill",
                "CodeSha256": "JZ/7XolvjCmxaYHUELY7ezuPGJWQs1os6Udhwv1rG9Y=",
                "LastModified": "2017-07-23T17:17:05.962+0000",
                "Handler": "ask_amy.lambda_function.lambda_handler",
                "Timeout": 5
            }
        }

    .. note::

        subsequent calls would use *deploy_lambda* inplace of *create_lambda* i.e
        `ask-amy-cli deploy_lambda --deploy-json-file cli_config.json`


* Logon to `Alex Development Portal <https://developer.amazon.com/alexa>`_. Select `Add New Skill`

    .. image:: _static/tut_1_01_add_new_skill.png
            :width: 600px
            :height: 203px

* In **Skill Information** set *Name* to `Obama Fact` and set *Invocation Name* to `Obama Fact`, click `Save`
  and `Next`

    .. image:: _static/tut_1_02_skill_information.png
            :width: 600px
            :height: 478px

* In **Intercation Model** copy the contents of the `alexa_obama_fact_skill/speech_assests/intent_schema.json` to
  **Intent Schema** and `alexa_obama_fact_skill/speech_assests/utterance.txt` to **Sample Utterances**, click `Save`
  and `Next`

    .. image:: _static/tut_1_03_a_interaction_model.png
            :width: 600px
            :height: 339px

    .. image:: _static/tut_1_03_b_interaction_model.png
            :width: 600px
            :height: 244px


* In **Configuration** click `AWS Lambda ARN`, `North America` and paste the *FunctionArn* from step three above
  into the Service Endpoint Field, click `Save` and `Next`

    .. image:: _static/tut_1_04_configuration.png
            :width: 600px
            :height: 617px

* In **Test** *Enter Utterance* `Give me a fact` and click `Ask Obama Fact` note the *Lambda Response*

    .. image:: _static/tut_1_05_test.png
            :width: 600px
            :height: 611px

* Congratulations, You have deployed your first ASK Amy based skill!

