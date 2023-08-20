from abc import ABC, abstractmethod


class Country(ABC):
    def __init__(self):
        self.name = ''
        self.agility = 0
        self.entrepreneurship = 0
        self.open_for_business = 0
        self.social_purpose = 0
        self.quality_of_life = 0

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
