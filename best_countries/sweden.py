from best_countries.country import Country


class Sweden(Country):
    def __init__(self):
        super().__init__()
        self.name = 'Sweden'
        self.agility = 81.9
        self.entrepreneurship = 73.2
        self.open_for_business = 81.9
        self.social_purpose = 100
        self.quality_of_life = 100

    def description(self):
        return f'{self.name}:'"""
        The most populous nation on the Scandinavian 
        peninsula, Sweden is often hailed as one of the best 
        countries in the world to live in year after year, and 
        it's no wonder why. It consistently ranks high on lists
        of the happiest nations in the world and on the 
        Human Development Index.
        
        The standard of living is fantastic. Swedes enjoy a 
        high level of freedom, low crime, high average
        income and income equality, and a beautiful country
        with loads to see and do.
        
        Although it can be expensive place to live, it's still considered one of the best countries to live in 2023 
        as it's one of the safest countries in the world, with a strong economy, and there are plenty of opportunities
        for expats to find well-paid jobs.
        """

    def healthcare(self):
        return """
        Healthcare:
        Unlike most Scandinavian nations, the Swedish healthcare system is decentralized and mainly government-funded,
        but local authorities decide how it's run and how much the total healthcare budget will be through local taxes.
        
        The level of care you receive in one municipality could be slightly better or worse than in another, although
        the country generally provides a high quality healthcare system.
        
        Private global health insurance is available for those who want access to more healthcare options and faster
        treatment, costing as little as 4,000 kr per annum.     
        """

    def education(self):
        return """
        Education:
        Sweden has a tax-funded well-developed public education system which is also decentralized. The government
        grants local authorities autonomy in designing course carricula as long as national standardized goals are met.
        
        There is a growing number in independent educational institutions in the country, also funded trough taxes.
        Children can choose whether to attend a public municipal school or  an independent one.
        
        Sweden is one of the best nations in the world to live with family and rise children. From the age of three,
        there is already a heavy incorporation of STEM (science, technology, engineering, and mathematics) curriculum
        in schools. 
        """