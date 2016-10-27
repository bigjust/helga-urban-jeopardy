import requests
import urlparse

from twisted.internet import reactor

from helga.db import db
from helga.plugins import command

from helga_jeopardy import jeopardy, ANSWER_DELAY, reveal_answer


UD_API_URL = 'https://mashape-community-urban-dictionary.p.mashape.com/define'

def retrieve_word(client, channel):
    """
    Retrieve a word via the random url.

    The first definition is the question text, and the answer is the word.

    """

    resp = requests.get('http://www.urbandictionary.com/random.php')

    random_word = urlparse.parse_qs(resp.url).items()[0][1][0]

    resp = requests.get(
        UD_API_URL,
        headers={
            'x-mashape-key': 'CNpEo84pRZmshewSL2ssKWoHyFGyp1eu9uIjsnVfHBr9zaPAkJ',
            'accept': 'text/plain',
        },
        params={
            'term': random_word,
        },
    )

    resp_json = resp.json()
    definition = resp_json['list'][0]['definition']

    db.urban_jeopardy.insert({
        'question': definition,
        'answer': random_word,
        'active': True,
        'channel': channel,
    })

    reactor.callLater(ANSWER_DELAY, reveal_answer, client, channel, definition, random_word, mongo_db=db.urban_jeopardy)

    return '"{}"'.format(definition)


@command('u', help='HALP')
def urban_jeopardy(client, channel, nick, message, cmd, args):
    return jeopardy(client, channel, nick, message, cmd, args, quest_func=retrieve_word)
