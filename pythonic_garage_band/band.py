class Musician:
    """Base class of all different musicians in a band."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        """returns instrument type"""
        raise NotImplementedError

    def play_solo(self):
        """playing a solo"""
        raise NotImplementedError


class Guitarist(Musician):
    """Guitarist in band"""

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"


class Bassist(Musician):
    """Bassist in band."""

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"


class Drummer(Musician):
    """Drummer in band."""

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Band:
    """Various musicians in band."""
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        """Band members play a solo."""
        return [member.play_solo() for member in self.members]

    def __str__(self):
        return f"The band {self.name}"

    def __repr__(self):
        return f"Band instance. Name = {self.name}"

    @classmethod
    def to_list(cls):
        """Returns a list of all previously created Band instances."""
        return cls.instances
