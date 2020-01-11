"""
This is a Python template for Alexa to get you building skills (Tourist) quickly.
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------
def get_test_response():
    """ An example of a custom intent. Same structure as welcome message. Structur for place-1 """
    session_attributes = {}
    card_title = "Test"
    speech_output = "The Kanaka Durga Temple is definitely one of the most holy temples of Andhra Pradesh, and it is one of Vijayawada's prides. It is a destination of much importance for Hindus, Kanaka Durga Temple is located in the state of Andhra Pradesh, in Vijayawada. Gracing the Indrakeeladri Hill, this temple is on the banks of Krishna River, and minds mention in Indian Vedic literature. The small and beautiful metropolis of Vijayawada is a nice place to explore here in the state of Andhra Pradesh, with a good cultural presence. Among all its many delights, the temple of Kanaka Durga is probably the best place of interest. Standing here seeking in reverence in front of the divine Goddess, the image of Shakti, is perhaps a blessing in itself. This is where you can seek divinity, and ask Kanaka Durga your heart's desires."
    reprompt_text = "You never responded to the Kanka temple message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_test1_response():
    """ An example of a custom intent. Same structure as welcome message. Structur for place-2 """
    session_attributes = {}
    card_title = "Test1"
    speech_output = "Bhavani Island is a picturesque spot blessed by the placid waters and is one of the most favored travel attractions of Vijayawada visited by the locals as well as tourists with equal zest. Surrounded by mangroves and manicured gardens, Bhavani Island is the perfect destination for enjoying evening walks amidst the serenity, fresh air and lush green surroundings of this place. One can enjoy a boat ride and swim here with the amazing facilities offered by the Andhra Pradesh Tourist Development Corporation. One can also indulge in adventure activities and water sports on this attractive island."
    reprompt_text = "You never responded to the Bhavani temple message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_test2_response():
    """ An example of a custom intent. Same structure as welcome message. Structur for place-3 """
    session_attributes = {}
    card_title = "Test2"
    speech_output = "Kondaveedu Fort is a historically significant ancient hill fortress located in Kondaveedu, a village in the Chilakaluripet of Guntur district, Andhra Pradesh, India. The site is located 16 miles west of the city of Guntur. In recent years, tourists from across the state continue thronging the place and enjoying the scenic beauty of the area."
    reprompt_text = "You never responded to the Kondaveedu Fort message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_test3_response():
    """ An example of a custom intent. Same structure as welcome message. Structur for place-4 """
    session_attributes = {}
    card_title = "Test3"
    speech_output = "The Undavalli Cave is a monolithic example of Indian rock-cut architecture and one of the finest testimonials to ancient Viswakarma chapatis. It is located in Undavalli of Guntur district in the Indian state of Andhra Pradesh."
    reprompt_text = "You never responded to the Undavalli Caves message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_test4_response():
    """ An example of a custom intent. Same structure as welcome message. Structur for place-5 """
    session_attributes = {}
    card_title = "Test4"
    speech_output = "The Amaravati Stupa is a famous specimen of the Buddhist art and architecture of ancient India. It is located at Amravati in Andhra Pradesh, which is around 65 km from the city of Vijayawada. Being visited by hundreds of tourists and pilgrims makes it one of the popular tourist attractions in Andhra Pradesh"
    reprompt_text = "You never responded to the Amaravti Stupa message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
        
def get_test5_response():
    """ An example of a custom intent. Same structure as welcome message. Structur for place-5 """
    session_attributes = {}
    card_title = "Test5"
    speech_output = "Prakasam Barrage stretches 1223.5 m across the Krishna River connecting Krishna and Guntur districts in the state of Andhra Pradesh. The barrage also serves as a road bridge and spans over a lake. There are three canals associated with the barrage that run through the city of Vijayawada, crossing it and giving it a Venetian appearance."
    reprompt_text = "You never responded to the Prakasam Barrage message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could add those here """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to Tourist alexa application!"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I don't know if you heard me, welcome to your custom alexa application!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass



def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    # Dispatch to your skill's launch message
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "test":
        return get_test_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    elif intent_name == "test_one":
        return get_test1_response()
    elif intent_name == "test_two":
        return get_test2_response()
    elif intent_name == "test_three":
        return get_test3_response()
    elif intent_name == "test_four":
        return get_test4_response()
    elif intent_name == "test_five":
        return get_test5_response()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])