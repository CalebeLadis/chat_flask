class Mensagem:
    def __init__(self, id=None, id_remetente=None, id_destinatario=None, datetime=None, texto =None):
        self.__id = id
        self.__id_remetente = id_remetente
        self.__id_destinatario = id_destinatario
        self.__datetime = datetime
        self.__texto = texto

    @property
    def id(self):
        return self.__id

    @property
    def id_remetente(self):
        return self.__id_remetente

    @property
    def id_destinatario(self):
        return self.__id_destinatario

    @property
    def texto(self):
        return self.__texto

    @property
    def datetime(self):
        return self.__datetime
