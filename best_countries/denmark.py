from best_countries.country import Country


class Denmark(Country):

    def __init__(self):
        super().__init__()
        self.name = 'Denmark'
        self.agility = 78.8
        self.entrepreneurship = 71
        self.open_for_business = 82
        self.social_purpose = 98.9
        self.quality_of_life = 99.9

    def description(self):
        return f'{self.name}:'"""
        Denmark should be at the top of the list for expats
        searching for the best standard of living available.
        This small Nordic country consistently ranks highly 
        in international surveys on factors like happiness,
        income equality, safety, and access to education. It's
        also a global leader in social welfare.
        """

    def healthcare(self):
        return """
        Healthcare:
        The Danes are known to have one of the best quality healthcare systems, which is evident from its citizens' high
        life expectancy and low mortality rate. The universal healthcare system runs under a well-developed public
        health insurance scheme that requires registration with the Danish Civil Registration System. Once enrolled, all
        Danish nationals are entitled to free universal health coverage.
        """

    def education(self):
        return """
        Education:
        Denmark upholds the principle of free education at all levels. Regardless of what you choose to study or which
        public university you attend, there are no charges incurred or student loan to pay back.
        """


