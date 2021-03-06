from ._entity import Entity



#===================================================================================================
# Broadcast
#===================================================================================================
class Broadcast(Entity):
    '''
    :ivar str message:
        Broadcast message.
    '''

    __slots__ = [
        'message',
    ]
