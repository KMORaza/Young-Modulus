import numpy as np
from material import Material
class Experiment:
    def __init__(self, material, force_data, extension_data, time_data=None, temperature_data=None, pressure_data=None):
        self.material = material
        self.force_data = force_data 
        self.extension_data = extension_data
        self.time_data = time_data if time_data else None 
        self.temperature_data = temperature_data if temperature_data else None  
        self.pressure_data = pressure_data if pressure_data else None  
    def stress(self, forces):
        stresses = []
        for force in forces:
            stress = force / self.material.cross_sectional_area()
            stresses.append(stress)
        return stresses
    def strain(self, extensions):
        return [extension / self.material.length for extension in extensions]
    def youngs_modulus(self):
        num_experiments = len(self.force_data)
        moduli = []
        for i in range(num_experiments):
            forces = self.force_data[i]
            extensions = self.extension_data[i]
            stresses = self.stress(forces)
            strains = self.strain(extensions)
            avg_stress = np.mean(stresses)
            avg_strain = np.mean(strains)

            modulus = avg_stress / avg_strain
            moduli.append(modulus)
        return moduli
    def run_experiment(self):
        print("Running experiment...")
        print("Material:", self.material)
        for i in range(len(self.force_data)):
            print(f"Experiment {i+1}:")
            print("Force Data:", self.force_data[i])
            print("Extension Data:", self.extension_data[i])
            if self.time_data is not None:
                print("Time Data:", self.time_data[i])
            if self.temperature_data is not None:
                print("Temperature Data:", self.temperature_data[i])
            if self.pressure_data is not None:
                print("Pressure Data:", self.pressure_data[i])
            print("Calculating Young's Modulus...")
            moduli = self.youngs_modulus()
            print(f"Young's Modulus for Experiment {i+1}: {moduli[i]}")
            print()
