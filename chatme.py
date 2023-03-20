import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!', ['hello', 'hi', 'hii','hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])
    
    
    response('We belong to GWECA of Ajmer',['boss','owner','senior'], single_response=True)
    response('We are available 24 hrs for your help.How are you feeling?\n 1.Hungry\n 2.Wanna Study\n 3.Wanna Listen music\n 4.Entertainment',['available','timings','free'],single_response=True)
    response('You may Order your favourites from Swiggy or Zomato.\nSwiggy:https://www.swiggy.com/\nZomato:https://www.zomato.com/',['1'],single_response=True)
    response('You may use geeksforgeeks or javatpoint to learn new.\ngeeksforgeeks: https://www.geeksforgeeks.org/\njavatpoint:https://www.javatpoint.com/',['2'],single_response=True)
    response('You may Listen your favourites from ganna or spotify.\nganna: https://gaana.com/\n spotify: https://open.spotify.com/',['3'],single_response=True)
    response('Visit Swiggy or Zomato on our website.',['order','eat','eating','hungry','hunger','hot','cold'],single_response=True)
    
    
    
    
    response('(a) News\n(b)Movies\n(c)Sports',['4'],single_response=True)
    
    
    response('You may contact to different news channels like ndtv or economic times.\n NDTV : https://www.ndtv.com/\n THE ECONOMIC TIMES : https://economictimes.indiatimes.com/',['a'],single_response=True)
    response('You may connect with Netflix Amazon prime.\nNetflix : https://www.netflix.com/in/\n Amazon Prime : https://www.primevideo.com/',['b'],single_response=True)
    response('You may use sports18 or sky sports.\nSports18 : https://www.sports18.com/\nSky Sports : https://www.skysports.com/',['c'],single_response=True)
    
    
    # Longer responses
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))
