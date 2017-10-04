:orphan:

ASK Amy Example Skills
======================

To help accelerate your development and deployment with ASK Amy we have rewritten many of the popular tutorial skills
using ASK Amy. Once you have your ASK Amy environment setup deploying and running any of these skills can be done in
less than 10 minutes. Each skill highlights different features of ASK Amy.


|source_code| Available Skills:
-------------------------------

+---------------------------------+------------------------------------------------------------------------------------------+
| Skill                           | Description                                                                              |
+=================================+==========================================================================================+
| **1:** Alexa Obama Fact Skill   | Have Alexa read interesting random facts on any subject of your choosing                 |
|                                 | this skill just happens to be about presidential facts. Here is an interesting fact      |
|                                 | using ASK Amy this skill is written in less than 25 lines of code!                       |
+---------------------------------+------------------------------------------------------------------------------------------+
| **2:** Alexa High Low Skill     | Simple number guessing game that saves the history of number of games played.            |
|                                 | This skill introduces how easy persistence and session management is with ASK Amy.       |
+---------------------------------+------------------------------------------------------------------------------------------+
| **3:** Alexa Scorekeeper Skill  | A Scorekeeper for multiple player games. Demonstrates a slightly more complex            |
|                                 | persistence model than the *Alexa High Low Skill* and introduces custom validators for   |
|                                 | slots. ASK Amy uses custom validators to automatically re-prompt if the data is not      |
|                                 | what is expected.                                                                        |
+---------------------------------+------------------------------------------------------------------------------------------+
| **4:** Alexa Tide Skill         | The Tide Pooler example demonstrates connecting to a web API to retrieve tide            |
|                                 | information. The example also outputs SSML with audio (the sound of a crashing wave).    |
|                                 | It also uses ASK Amy state management for required slots, re-prompting the user when     |
|                                 | necessary without requiring any additional code to accomplish this.                      |
+---------------------------------+------------------------------------------------------------------------------------------+
| **5:** Alexa History Buff Skill | Have Alexa tell interesting facts about what happened on this day in history. Another    |
|                                 | web API interface but with more data and paging of the content ("tell me more").         |
+---------------------------------+------------------------------------------------------------------------------------------+
| **6:** Alexa Wise Guy Skill     | Knock Knock Joke Skill. Demonstrates multiple user interactions.                         |
+---------------------------------+------------------------------------------------------------------------------------------+
| **7:** Alexa Account Link Skill | An example of how to accomplish Account Linking with ASK Amy.                            |
+---------------------------------+------------------------------------------------------------------------------------------+
| **8:** Alexa Podcast Skill      | A Podcast player. Demonstrating integrating with Alexa's Audio / Music management.       |
+---------------------------------+------------------------------------------------------------------------------------------+
| **9:** Alexa Session Skill      | Simple example showing how to manage a users interactions in a session with ASK Amy.     |
+---------------------------------+------------------------------------------------------------------------------------------+
| **10:** Alexa Hello Skill       | A template for getting started. This is not needed in most cases as ASK Amy has a        |
|                                 | **Template Skill Code Generator** that will create an executable stub skill from an      |
|                                 | intent schema file.                                                                      |
+---------------------------------+------------------------------------------------------------------------------------------+


|github| Get the Example code:
------------------------------

* Clone the **ASK Amy** examples.

    .. code-block:: bash

        $ git clone https://github.com/dphiggs01/ask_amy_example_skills.git




.. |source_code| image:: _static/icon-source_code.png
            :width: 40px
            :height: 30px
            :align: middle

.. |github| image:: _static/icon-github.png
            :width: 40px
            :height: 30px
            :align: middle
