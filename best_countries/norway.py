from best_countries.country import Country


class Norway(Country):

    def __init__(self):
        super().__init__()
        self.name = 'Norway'
        self.agility = 69.6
        self.entrepreneurship = 63.7
        self.open_for_business = 84.2
        self.social_purpose = 99.7
        self.quality_of_life = 96.3

    def description(self):
        return f'{self.name}:'"""
        Although most Northern European countries enjoy
        many quality-of-life benefits, Norway, the largest
        country on the Scandinavian Peninsula, ranks as one of
        the highest in the Human Development Index. Simple
        factors such as good governance, income equality, civil
        rights, low unemployment, and a high net worth per
        capita allow Norwegians to enjoy a high standard of
        living. 
        
        The average salary in Norway is €50000. Although Norway imposes high-income taxes, the money 
        generated is used well. It's also a great country for expats who love the outdoors, with
        Jotunheimen National Park rated as one of the best national parks in Europe.
        """

    def healthcare(self):
        return """
        Healthcare:
        Like most Nordic countries, the Norwegian universal healthcare system has been praised for its efficiency and
        simplicity. There is no requirement for private medical insurance as all residents have access to free health
        care paid by government taxes.
        
        Prescriptions are subsidized by the government and have a low universal cost, making them very affordable
        regardless of what kind of treatment you require.
        
        As an expat in Norway, you'll have access to high-quality care in addition to low wait times for appointments
        and health services.
        """

    def education(self):
        return """
        Education:
        Not only is the well-developed public education system in Norway free, but EU and EEA are also 
        eligible to receive a free bursary to support their education that does not need to paid back. 
        """