from best_countries.country import Country


class The_Netherlands(Country):
    def __init__(self):
        super().__init__()
        self.name = 'The Netherlands'
        self.agility = 76.5
        self.entrepreneurship = 70
        self.open_for_business = 76.1
        self.social_purpose = 90.9
        self.quality_of_life = 88.9

    def description(self):
        return f'{self.name}:'""" 
        The Netherlands is a liberal paradise with numerous quality-of-life benefits to match. Dutch people are known
        for being welcoming and highly tolerant of people of different cultures and beliefs. 
        
        Cycling is engaged within Dutch culture and is the main form of transport for many people who live there.
        Despite having the highest population density of all the large economies in the European Union, a profound
        cycling culture consistently places the Netherlands in high position on low air pollution indexes. It maintains
        clean air quality even in compact cities.
        
        The cost of living in the Netherlands is relatively affordable, especially compared to the largest countries in
        western Europe. And although the Dutch language can be challenging to learn, English is widely spoken throughout
        the nation, 95 percent of the population speaking English.
        """

    def healthcare(self):
        return """
        Healthcare:
        The think tank, Health Consumer Powerhouse, ranked the Netherlands at number two in a pool of the 35 best
        healthcare systems in the world due to its heavy focus on patient-centered health services and the satisfaction
        of Dutch residents with the quality of their healthcare service.
        
        The excellent healthcare system is divided between well-developed public health services and private
        healthcare. The government automatically insure Dutch residents, but basic medical insurance is compulsory.
        
        Health insurance prices are very affordable in the Netherlands, with premiums starting at around €125 per month.
        Furthermore, the good news for young families is that children are automatically covered under their parent's
        medical insurance policies.
        """

    def education(self):
        return """
        Education:
        The Netherlands employs a progressive and well-developed public education system. By the time a child
        reaches the high school age of twelve, they enter one of three different streams of education based on the
        student's academic level and interests.
        
        The three streams are:
        
        VMBO (preparatory secondary vocational education): Similar to high school in other developed nations. VMBO
        provides education based on vocationally-oriented education over four years.
        
        HAVO (senior general secondary education): A five-year educational plan that prepares children to study at
        universities of applied sciences.
        
        VWO (university preparatory education): An education stream over six years focused on theoretical knowledge
        that prepares students to follow bachelor's degrees at research universities.
        
        Although different streams prepare children for carious fields of study, any of them can be accessed regardless
        of which stream is entered. Some just allow public education phases to be completed in a much shorter time-span.
        """

