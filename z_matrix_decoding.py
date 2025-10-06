"""
Basic Z-matrix decoding template in Python
"""

class ZMatrixDecoder:
    def __init__(self, z_matrix_str):
        self.z_matrix_str = z_matrix_str
        self.atoms = []
        self.parse()

    def parse(self):
        lines = self.z_matrix_str.strip().split('\n')
        for i, line in enumerate(lines):
            parts = line.split()
            atom = parts[0]
            if i == 0:
                self.atoms.append({'atom': atom})
            elif i == 1:
                self.atoms.append({'atom': atom, 'bond_to': int(parts[1])-1, 'bond_length': float(parts[2])})
            elif i == 2:
                self.atoms.append({'atom': atom, 'bond_to': int(parts[1])-1, 'bond_length': float(parts[2]), 'angle_to': int(parts[3])-1, 'angle': float(parts[4])})
            else:
                self.atoms.append({'atom': atom, 'bond_to': int(parts[1])-1, 'bond_length': float(parts[2]), 'angle_to': int(parts[3])-1, 'angle': float(parts[4]), 'dihedral_to': int(parts[5])-1, 'dihedral': float(parts[6])})

    def get_atoms(self):
        """
        Returns a list of atom dictionaries decoded from the Z-matrix.
        """
        return self.atoms

if __name__ == "__main__":
    # Example usage
    z_str = """\
O
H 1 0.96
H 1 0.96 2 104.5
"""
    decoder = ZMatrixDecoder(z_str)
    print(decoder.get_atoms())
