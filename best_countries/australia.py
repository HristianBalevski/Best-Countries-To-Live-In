from best_countries.country import Country


class Australia(Country):
    def __init__(self):
        super().__init__()
        self.name = 'Australia'
        self.agility = 83.6
        self.entrepreneurship = 63.7
        self.open_for_business = 77
        self.social_purpose = 84
        self.quality_of_life = 85.7

    def description(self):
        return f'{self.name}:'"""
        There are countless reasons why Australia is considered one of the best nations in the world to live in
        for expats. The most populous nation in Oceania, although slightly further afield, a number of the best
        quality-of-life factors make it the perfect home away from home.
        
        For a start, the country has a stable and strong economy and maintains political neutrality.
        
        Additionally, Australia ranks highly in standard of living concerning healthcare and has a wide range of
        educational opportunities.
        
        Australia ranks seventh on the OCED Better Live Index, based on living conditions overall quality of life
        factors in several aspects such as the environment, work-life balance, community, and safety. The country
        also ranks in the top ten countries for average life expectancy based on the UN Population Division.
        
        The climate and scenery in Australia are also very pleasant, with a lot of variation due to being one of
        the largest countries in the world with vast areas of land. All major cities run along its coastline.
        Australian cities like Sidney enjoy a more temperature climate throughout the year, making it one of the
        best warm countries to live in the world, whereas isolated cities like Perth have hotter summers and 
        colder winters.
        """

    def healthcare(self):
        return """
        Healthcare:
        The Australian high-quality healthcare system provides services at a substantially reduced cost through its
        Medicare program.
        
        Australian residents have free access to essential healthcare in public hospitals. Most Australians take out
        insurance to access private healthcare should they need it. The average monthly premium is very cheap at 245
        AUD per month on average.
        
        A comparison by Compare the Market found that 73.4 percent of Australians felt satisfied with the quality
        of healthcare in Australia, as opposed to 54.2 percent of Americans with the quality of healthcare in the US.
        """

    def education(self):
        return """
        Education:
        The nation's world-class public education system runs stringently to ensure quality schooling at all levels.
        Public education until university is free for Australian permanent residents, and the government heavily
        subsidizes tuition fees through taxes.
        
        Many Australian universities, such as the University of Melbourne, have high overall rankings in higher 
        education comparison studies and are very strong in various fields of study, such as biological sciences and
        engineering.
        """