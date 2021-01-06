
def substitue(message, abreviation):

    message_complet = ""

    for mot in message.split():
        if mot in abreviation:
            message_complet = message.replace(mot, abreviation[mot])
            message = message_complet

    return message




print(substitue('C. N. cpt 2 to inf', {'C.' : 'Chuck',
                                 'N.' : 'Norris',
                                 'cpt' : 'counted',
                                 '2' : 'two times',
                                 'inf' : 'infinity'}))