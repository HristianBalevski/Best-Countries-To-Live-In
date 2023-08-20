from best_countries.country import Country


class Germany(Country):
    def __init__(self):
        super().__init__()
        self.name = 'Germany'
        self.agility = 92.1
        self.entrepreneurship = 100
        self.open_for_business = 62
        self.social_purpose = 70.3
        self.quality_of_life = 90

    def description(self):
        return f'{self.name}:'"""
        Germany receives frequent praise for its high standard of living from expats living with family
        and young adults. It's the nation that is home to the most expats in Europe, and justifiable so.
        
        Expats frequently cite Germany's efficient infrastructure, the abundance of available activities,
        public services, income equality, and work opportunities in a wide range of industries as some of the main
        reasons why it's such a great place to live.
        
        The country boasts a rich cultural heritage and is home to some of the world;s most famous tourist destinations,
        like its capital city, Munich, as well as Berlin and Hamburg.
        
        Germans also have the second highest-ranking passport in the world on the Global Passport index, which
        measures the strength of a nation's passport. Furthermore, Germany is one of the biggest contributors to the
        United Nations, which demonstrates its dedication to peace.
        """

    def healthcare(self):
        return """
        Healthcare:
        The German healthcare system is a statutory health insurance system (SHI) financed with equal payments
        divided between an employee and an employer.
        
        SHI enacts comprehensive insurance that covers major surgeries, prescriptions, and sick-pay, without excess
        payments or additional fees.
        
        The German healthcare system is one of the most technologically-advanced in the world. Residents seldom
        need to venture abroad should they require any specialist treatment.
        
        Hygiene is also a crucial of the German healthcare system, and access to the most up-to-date technologies and
        innovative treatments is also widely available.
        """

    def education(self):
        return """
        Education:
        Germany has a free public school system and a wide range of high-quality fee-based private and international
        schools. The general quality of education is high, whether public or private. In each world report for 
        education, German students consistently rank high in cornerstone subjects such as maths and science.
        
        How special needs children are integrated into the mainstream school system is also exemplary, offering
        adequate additional support and specialist help.
        
        German universities are ideal for international students interested in fields in which Germany is a global
        leader, such as the automotive industry.
        
        Mercedes-Benz offers a world-class dual-study program at the Baden-Württemberg Cooperative State
        University in Stuttgart. It provides theoretical studies in conjunction with dynamic, practical training at
        its state-of-the-art research and development, and manufacturing facilities.
        """
