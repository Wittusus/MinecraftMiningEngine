from Services.MiningEngineService import MiningEngineService
from Services.Logger import Logger
from Services.ApplicationConfigReader import ApplicationConfigReader


class Program:

    # Dependency injection

    def __init__(self):

        # Configuration of services

        self.config = ApplicationConfigReader("Config/app_config.txt")
        self.miningEngine = MiningEngineService()
        self.logger = Logger(self.config.readFromConfigFile("application_log_path"))

    # running program
    def run(self):

        self.logger.log_message("Application stared")
        try:
            mining_engine = self.config.readFromConfigFile("mining_engine")

            if mining_engine == "basic":
                print("Starting basic mining engine \n")
                self.miningEngine.start_mining()
                self.logger.log_message("Initialized MiningEngineService")


            else:
                config_file = self.config.configFilePath
                print(f"[ERROR] mining_engine not selected in config file {config_file}")
                return Exception
        except:

            print('Failed to initialize services')
            self.logger.log_message('Failed to initialize services', "error")

