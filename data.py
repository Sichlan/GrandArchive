import random

class RollResult:
    Id: int
    Name: str
    
    def __init__(self, id: int, name: str):
        self.Id = id
        self.Name = name
    
    def __str__(self):
        return f'{self.Id} - {self.Name}'
    

class SystemFeature(RollResult):
    
    def __init__(self, 
                 id: int, 
                 name: str, 
                 description: str = None, 
                 apply_effect_quantity: str = None, 
                 enforce_effect: bool = None, 
                 effects: list[str] = None):
        
        # if not apply_effect_quantity is None and apply_effect_quantity.lower() in ('one', 'any', 'all'):
        #     raise ValueError(f'apply_effect_quantity must be one of "one", "any", "all"! given value: {apply_effect_quantity}')
        
        RollResult.__init__(self, id, name)
        self.Description = description
        self.ApplyEffectQuantity = apply_effect_quantity
        self.EnforceEffect = enforce_effect
        self.Effects = effects

SF_BOUNTIFUL = SystemFeature(1, 'Bountiful', 'A System with this System Feature has been blessed with an abundance of rare and unusual materials. The formation of the nearby stars might have bled off an unusual amount of exotic materials, or the System could have become saturated with such resources as passing meteors and comets became trapped in their gravity wells. However it came about, the area is now a veritable storehouse of mineral treasures, waiting to be tapped in the name of profit. Habitable worlds within such an area are highly prized as possible colony sites, although well-equipped Rogue Traders have been known to set up their mining operations on worlds that would not normally allow human settlement')

# todo: move all of those to dedicated globals
SYSTEM_FEATURES = [
    SF_BOUNTIFUL,
    SystemFeature(2, 'Gravity Tides'),
    SystemFeature(3, 'Haven'),
    SystemFeature(4, 'Ill-Omened'),
    SystemFeature(5, 'Pirate Den'),
    SystemFeature(6, 'Ruined Empire'),
    SystemFeature(7, 'Starfarers'),
    SystemFeature(8, 'Stellar Anomaly'),
    SystemFeature(9, 'Warp Stasis'),
    SystemFeature(10, 'Warp Turbulence')
]