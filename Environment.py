import os

class EDS1_SIM:


    
    def __str__(self):
        return f"SIM\n\tNAME: {self.name} \n\tDIR: {self.sim_directory}"


    def set_sim_directory(self, sim_directory):
        self.sim_directory = sim_directory

    def set_name(self, name):
        self.name = name

class EDS1_PNR:

    def __str__(self):
        return f"PNR\n\tPNR-NAME: {self.name} \n\tPNR-DIR: {self.pnr_directory} \n\tSIM-NAME: {self.SIM.name} \n\tSIM-DIR: {self.SIM.sim_directory}"

    def set_pnr_directory(self, pnr_directory):
        self.pnr_directory = pnr_directory

    def set_name(self, name):
        self.name = name

    def set_sim(self, sim):
        self.SIM = sim




class EDS1_ENV:
    def add_sim(self, sim):
        self.sim = sim

    def get_sim(self):
        return self.sim
    
    def add_pnr(self, pnr):
        self.pnr = pnr

    def get_pnr(self):
        return self.pnr
    
        




