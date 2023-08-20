from abc import ABC, abstractmethod


class Country(ABC):
    def __init__(self, name='', agility=0, entrepreneurship=0, open_for_business=0, social_purpose=0,
                 quality_of_life=0):
        self.name = name
        self.agility = agility
        self.entrepreneurship = entrepreneurship
        self.open_for_business = open_for_business
        self.social_purpose = social_purpose
        self.quality_of_life = quality_of_life

    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def healthcare(self):
        pass

    @abstractmethod
    def education(self):
        pass

    def __repr__(self):
        total_score = ((self.agility + self.entrepreneurship + self.open_for_business + self.social_purpose +
                        self.quality_of_life) / 5)

        return f'{self.name}: Top five quality-of-life attributes\n' + \
            f'Agility: {self.agility}\n' + \
            f'Entrepreneurship: {self.entrepreneurship}\n' + \
            f'Open for business: {self.open_for_business}\n' + \
            f'Social purpose: {self.social_purpose}\n' + \
            f'Quality of life: {self.quality_of_life}\n' + \
            f'\n' + \
            f'Total score: {total_score:.2f}'
