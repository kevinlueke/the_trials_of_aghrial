# Python3 Game
import rooms


class Map(object):

    room_names = {
            'intro': rooms.Introduction(),
            'cabin_main_room': rooms.CabinMainRoom(),
            'cabin_bathroom': rooms.CabinBathroom(),
            'cabin_bedroom': rooms.CabinBedroom(),
            'outside_cabin': rooms.OutsideCabin(),
            'river': rooms.River(),
            'woods': rooms.Woods(),
            'village': rooms.Village(),
            'village_homes': rooms.VillageHomes(),
            'higalra_residence_porch': rooms.ResidencePorch('Higalra', 'higalra_residence'),
            'higalra_residence': rooms.HigalraResidence(),
            'higalra_basement': rooms.HigalraBasement(),
            'higalra_kitchen': rooms.HigalraKitchen(),
            'higalra_bathroom': rooms.HigalraBathroom(),
            'higalra_bedroom': rooms.HigalraBedroom(),
            'dempster_residence_porch': rooms.ResidencePorch('Dempster', 'dempster_residence'),
            'dempster_residence': rooms.DempsterResidence(),
            'jail': rooms.Jail(),
            'secret_path': rooms.SecretPath(),
            'south_wiggols_village': rooms.SouthWiggolsVillage(),
            'north_wiggols_village': rooms.NorthWiggolsVillage(),
            'wiggols_job_board': rooms.WiggolsJobBoard(),
            'abandoned_house': rooms.AbandonedHouse(),
            'waterfall': rooms.Waterfall(),
            'secret_room': rooms.SecretRoom(),
            'road_map': rooms.RoadMap()
            }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.room_names.get(room_name)
        return val
    
    def opening_room(self):
        return self.next_room(self.start_room)
