from best_countries.country import Country


class Switzerland(Country):
    def __init__(self):
        super().__init__()
        self.name = 'Switzerland'
        self.agility = 70.8
        self.entrepreneurship = 81.3
        self.open_for_business = 100
        self.social_purpose = 86.6
        self.quality_of_life = 96.7

    def description(self):
        return f'{self.name}:'"""
        A historically wealthy nation, Switzerland ranks and has long been ranked as haven for the wealthy, and it's
        also a haven for expats seeking a high standard of living with a new lif abroad.
        
        Home of the World Economic Forum and as one of the world's wealthiest countries per capita, it has the world
        most stable political system, with long-standing neutrality concerning politics.
        
        Its stability makes it one of the best countries to live in the future, and it's one attractive destination
        for expats who want to avoid with volatile politics.
        """

    def healthcare(self):
        return """
        Healthcare:
        Switzerland has a universal compulsory private health insurance system that Swiss Federal Law on Health
        Insurance regulate. It ensures that Swiss residents have access to affordable medical insurance policies,
        ranging from CHF 300 to a maximum of CHF 2,500 per annum.
        
        Each canton in Switzerland sets its administrative policies, but regardless of where you live in Switzerland, 
        you can expect to receive world-class healthcare.
        """

    def education(self):
        return """
        Education:
        Switzerland ranks as having one of the best education systems in the world, with free public secondary
        education, placing in ninth position out of 65 nations and economies in a recent OECD survey of educational
        standards among 15 years-old. Switzerland's modern and well-developed public education system focuses
        heavily on real-world training as part of its curriculum.
        
        By the end of high school, VET programs (Vocational and Professional Education System) are introduced, 
        combining vocational education with onsite training at a company.
        
        Additionally, children and young adolescents with special educational needs have a right to free schooling and
        support from specialists from birth to their 20th birthday.
        """
