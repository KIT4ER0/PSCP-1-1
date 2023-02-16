"""Phasmophobia"""
def main():
    """main"""
    ghost = {
        "EMF Level 5" : ["Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"],
        "Ghost Writing" : ["Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"],
        "Fingerprints" : ["Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"],
        "Spirit Box" : ["Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"],
        "Freezing Temperatures" : ["Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"],
        "Ghost Orb" : ["Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"],
        "No evidence" : ["Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", "Poltergeist", \
        "Revenant", "Shade", "Spirit", "Wraith", "Yurei"]
    }
    val = sorted(set(ghost[input()]) & set(ghost[input()]) & set(ghost[input()]))
    if len(val) == 0:
        print("Not yet discovered")
    else:
        print(*val, sep="\n")
main()
