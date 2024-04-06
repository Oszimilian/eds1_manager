import os
from Environment import EDS1_ENV


class INIT_ENV:

    def print_sim_dirs(self, dirs):
        print("SIM DIR")
        
        for dir in dirs:
            print(f"-> {dir}")

    def print_pnr_dirs(self, dirs):
        print("PNR DIR")

        for dir in dirs:
            print(f"-> {dir[0]} - {dir[1]}")

    def get_eds1_pnr_dir(self, eds1_directories):
        pnr_dirs = []

        for sim_dir in eds1_directories:
            if "/sim/" in sim_dir:
                for pnr_dir in eds1_directories:
                    name = "/pnr/" + os.path.basename(sim_dir)
                    if name in pnr_dir:
                        pnr_dirs.append((pnr_dir, sim_dir))

        return pnr_dirs
    
    def get_eds1_sim_dir(self, eds1_directories):
        sim_dirs = []

        for directory in eds1_directories:
            if "/sim/" in directory:
                for dir in eds1_directories:
                    name = "/pnr/" + os.path.basename(directory)
                    if name in dir:
                        break
                sim_dirs.append(directory)

        for pnr_dir in self.get_eds1_pnr_dir(eds1_directories):
            sim_dirs.remove(pnr_dir[1])

        return sim_dirs
        

    def get_eds1_directories(self, directory_path):
        eds1_directories = []

        for root, directories, files in os.walk(directory_path):  
            for directory in directories:
                eds1_directories.append(os.path.join(root, directory))

        return eds1_directories

    def get_sim_objects(self, directory_path):
        sim_objs = []

        eds1_dirs = self.get_eds1_directories(directory_path)
        sim_dirs = self.get_eds1_sim_dir(eds1_dirs)

        for sim_dir in sim_dirs:
            sim = EDS1_SIM()
            sim.set_name(os.path.basename(sim_dir))
            sim.set_sim_directory(sim_dir)

            sim_objs.append(sim)

        return sim_objs
    
    def get_pnr_objects(self, directory_path):
        pnr_objs = []

        eds1_dirs = self.get_eds1_directories(directory_path)
        pnr_dirs = self.get_eds1_pnr_dir(eds1_dirs)

        for pnr_dir in pnr_dirs:
            sim = EDS1_SIM()
            sim.set_name(os.path.basename(pnr_dir[1]))
            sim.set_sim_directory(pnr_dir[1])

            pnr = EDS1_PNR()
            pnr.set_name(os.path.basename(pnr_dir[0]))
            pnr.set_pnr_directory(pnr_dir[0])
            pnr.set_sim(sim)

            pnr_objs.append(pnr)

        return pnr_objs

    def get_env(self, directory_path):
        env = EDS1_ENV()
        env.add_sim(self.get_sim_objects(directory_path))
        env.add_pnr(self.get_pnr_objects(directory_path))
        return env
    

env_input = INIT_ENV()

env = env_input.get_env("/home/maximilian/Git/eds1")
