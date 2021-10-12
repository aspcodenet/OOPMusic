
class Song:
    def __init__(self,title : str, lengthInSeconds : int):
        self._title = title
        self._lengthInSeconds = lengthInSeconds

    def getTitle(self) -> str:
        return self._title


    def doesStartOnLetter(self, s:str) -> bool:
        return self._title.upper().startswith(s.upper())
        # if self._title.upper().startswith(s.upper()): 
        #     return True          
        # return False


    def getLengthInSeconds(self) -> int:
        return self._lengthInSeconds


