from best_countries.country import Country


class Finland(Country):
    def __init__(self):
        super().__init__()
        self.name = 'Finland'
        self.agility = 64.8
        self.entrepreneurship = 63.7
        self.open_for_business = 85.9
        self.social_purpose = 95.4
        self.quality_of_life = 90

    def description(self):
        return f'{self.name}:'"""
        Rated as the world's happiest country for five years in a row proves that Finnish citizens must be happy
        with the standard of living in Finland.
        
        There are many reasons why Finns live such happy lives. And a big reason goes back to Finnish culture.
        
        Finnish philosopher Frank Martela describes Finns as generally happy people because Finnish culture is
        more accepting of negative emotions and tough times. "Nobody goes through life without tragedies, so
        being able to accept the situation is helpful", he says.
        
        But this is not the only reason why Finns are happy. Although this relatively isolated country in
        northern Europe can be a bit pricey to live in due to high-income taxes, the trickle down benefits of this are
        enormous.
        
        Crime rates are criminally low - non pun intended - and it's one of the safest countries in the world.
        According to Numbeo, it has the lowest pollution and the best air quality in the world. Tap water purity is 
        also amongst the highest in any nations.
        
        The high taxation has also created the most comprehensive welfare system available. Welfare support matches
        the cost of living for things like maternity, job lost, and child care.
        """

    def healthcare(self):
        return """
        Healthcare:
        Healthcare in Finland is publicly funded through taxes and social security. However, while the initiatives
        focus on health promotions and social welfare policies at the federal level, the healthcare system is
        mainly decentralized, with local authorities organizing healthcare delivery to residents.
        
        Nonetheless, global perceptions see Finland as having the best healthcare system due to its focus on general
        health and well-being and disease prevention rather than treatment.
        """

    def education(self):
        return """
        Education:
        Besides coming in first place for the best welfare system, the well-developed public education system in
        Finland is also unparalleled. It's an excellent place for expats to rise a family as there's not only great
        importance placed on access education but the quality of it too.
        
        Huge accountability is placed on teachers, and rightly so. They are on the frontline of education, delivering
        curricula to children. But many countries have low standards for teachers and don't adequately prepare them to
        carry out heir jobs effectively.
        
        The Finnish education system places the bar so high for its educators that there is almost no requirement for
        a rigorous grading system to assess the quality of their work.
        
        Educators in Finland are required to have master's degrees, in addition to completing studies in pedagogy,
        before the can seek employment.
        
        Conditions for teaching in Finland also create a much better environment for teachers and students, such as
        tight oversight over schools and adequate professional support for teachers.     
        """

