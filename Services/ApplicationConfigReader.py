from Services.GenericConfigReader import GenericConfigReader


class ApplicationConfigReader(GenericConfigReader):



    def readFromConfigFile(self, option: str):

        try:
            file = [i.split(':') for i in open(self.configFilePath)]
        except:
            return FileNotFoundError

        result = list(filter(lambda x: x[0] == option, file))[0][1].strip()
        return result


