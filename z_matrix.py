"""
Basic Z-matrix encoding template in Python
"""

class ZMatrix:
    def __init__(self):
        self.atoms = []  # List of tuples: (atom, connections)

    def add_atom(self, atom, connections):
        """
        Add an atom to the Z-matrix.
        atom: str, e.g. 'C', 'H', 'O'
        connections: tuple, e.g. (atom_index, bond_length, angle_index, angle, dihedral_index, dihedral)
        """
        self.atoms.append((atom, connections))

    def encode(self):
        """
        Returns a string representing the Z-matrix.
        """
        lines = []
        for i, (atom, conn) in enumerate(self.atoms):
            line = atom
            if i == 0:
                pass  # First atom, no connections
            elif i == 1:
                line += f" {conn[0]+1} {conn[1]}"
            elif i == 2:
                line += f" {conn[0]+1} {conn[1]} {conn[2]+1} {conn[3]}"
            else:
                line += f" {conn[0]+1} {conn[1]} {conn[2]+1} {conn[3]} {conn[4]+1} {conn[5]}"
            lines.append(line)
        return "\n".join(lines)

if __name__ == "__main__":
    # Example usage
    zm = ZMatrix()
    zm.add_atom('O', ())
    zm.add_atom('H', (0, 0.96))
    zm.add_atom('H', (0, 0.96, 1, 104.5))
    print(zm.encode())
