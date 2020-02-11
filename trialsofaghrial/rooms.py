# Rooms
from random import randint
from textwrap import dedent
import player_stats

# Dictionary of tasks to be completed for morality points

# Other classes will inherit this class it helps keep code DRY
class InitialRoom(object):

    def dir(self, valid_actions):
        while True:
            action = input('~> ')
            
            # Allows help to be available whenever a player needs to know controls
            if action == 'help':
                print(dedent("""
                    ---------------------------------------
                    The directions to move are as follows:
                    w will move forward
                    a will move left
                    s will move back
                    d will move right
                    ---------------------------------------
                    When presented with a choice to do something:
                    yes or y will agree to something
                    no or n will disagree to something
                    ---------------------------------------
                    mp will dislpay current score
                    map will show the map if you have it
                    """))
            elif action == 'map':
                if 'map' in (player_stats.player.stats['items']):
                    print(dedent("""
                        32171423 1029 291714 321029142725102121 29342514 24251423 281428102224
                        """))
                else:
                    print('no map')
            elif action == 'mp':
                print(f"Your current mp is {player_stats.player.stats['morality_points']}")

            elif action in valid_actions:
                return action

            else:
                print("Not a valid action right now. 'help' will list all possible actions")

# Beginning of game that a player will start at
class Introduction(InitialRoom):

    def enter(self):
        print(dedent("""
            Welcome to The Trials of Aghrial
            Years ago, Aghrial stopped a murder from happening
            Only days after the man that he saved killed hundreds
            After that tragic day Aghrial disappeared, leaving no trace of himself behind
            
            This game will allow you to choose between good and bad
            Sometimes chosing the wrong thing will lead to
            greater morality points (mp) and vice versa
            You may choose to achieve a score of 100 mp or -100 mp
            If you only choose choices of one side then the game will be imposiible to win
            ---------------------------------------
            The directions to move are as follows:
            w will move forward
            a will move left
            s will move back
            d will move right
            ---------------------------------------
            When presented with a choice to do something:
            yes or y will agree to something
            no or n will disagree to something
            ---------------------------------------
            Typing mp will give you your current score
            
            If at any point you are unsure of all available actions just type help

            
            There's a magical door right in front of you
            """))
        action = self.dir(('w',))

        if action == 'w':
            print("\nThe door you came out of slammed shut behind you and disappeared")
            return 'cabin_main_room'


class CabinMainRoom(InitialRoom):

    def enter(self):
        print(dedent("""
            You are standing in the entrance of a cabin
            To your right there is a bathroom
            Behind you is a bedroom
            In front of you is a door to leave the cabin
            """))
        action = self.dir(('w', 'd', 's'))

        if action == 'w':
            return 'outside_cabin'
        elif action == 'd':
            return 'cabin_bathroom'
        elif action == 's':
            return 'cabin_bedroom'


class CabinBathroom(InitialRoom):
    
    def enter(self):
        if player_stats.player.stats['drugs'] == False:
            print(dedent("""
                There is a bottle of Xeron Elixir in the bathroom
                The label is scraped off, you don't know what it'll do
                Do you steal it for -5 mp?
                """))
            action = self.dir(('yes', 'y', 'no', 'n'))

            if action == 'yes' or action == 'y':
                player_stats.player.stats['drugs'] = True
                player_stats.player.stats['morality_points'] -= 5
                print(dedent(f"""
                    After taking the elixir your whole body feels amazing
                    """))

            elif action == 'no' or action == 'n':
                print(dedent(f"""
                    You refrained from stealing drugs
                    """))
    
        print(dedent("""
            There is nothing else in the bathroom to use
            All you can do is head back
            """))
        action = self.dir(('s',))

        if action == 's':
            return 'cabin_main_room'


class CabinBedroom(InitialRoom):

    def enter(self):
        if player_stats.player.stats['cleaned_room'] == False:
            print(dedent("""
                The bedroom is messy
                Do you clean it for +5 mp?
                """))
            action = self.dir(('yes', 'y', 'no', 'n'))

            if action == 'yes' or action == 'y':
                player_stats.player.stats['cleaned_room'] = True
                player_stats.player.stats['morality_points'] += 3

                print(dedent(f"""
                    While cleaning the room you came upon a lockpick
                    Do you steal it for -5 mp?
                    """))
                action = self.dir(('yes', 'y', 'no'))
                if action == 'yes' or action == 'y':
                    player_stats.player.stats['morality_points'] -= 5
                    print("\nYou slide the lockpick into your pocket")
                    player_stats.player.stats['items'] = ['lockpick']

                elif action == 'no' or action == 'n':
                    print("\nThe lockpick is left where it is")

            elif action == 'no' or action == 'n':
                player_stats.player.stats['morality_points'] -= 1
                print(dedent(f"""
                    Ha!
                    You left the room messy
                    For doing such an evil thing you lost a morality point
                    """))

        print("There is nothing else to do in the bedroom")
        action = self.dir(('s',))

        if action == 's':
            return 'cabin_main_room'


class OutsideCabin(InitialRoom):

    def enter(self):
        print(dedent("""
            It's a beautiful sunny day outside
            To your left is a river
            To your right is the woods
            Straight ahead is a village
             """))
        action = self.dir(('a', 's', 'w', 'd'))

        if action == 'a':
            return 'river'
        elif action == 's':
            return 'cabin_main_room'
        elif action == 'w':
            return 'village'
        elif action == 'd':
            return 'woods'


class Woods(InitialRoom):

    def enter(self):
        if player_stats.player.stats['cannibals'] == False:
            print(dedent("""
                You came upon a tribe of cannibals
                Luckily for you they have just eaten
                Rather than eat you they want to see if you'll eat human meat
                Do you eat it for -5 mp?
                """))
            action = self.dir(('yes', 'y', 'no', 'n'))

            if action == 'yes' or action == 'y':
                player_stats.player.stats['cannibals'] = True
                player_stats.player.stats['morality_points'] -= 5
                print(dedent(f"""
                    You ate the meat and feel full
                    They thank you for eating with them and show you a secret path to the right
                    """))
                action = self.dir(('s', 'd'))

                if action == 'd':
                    return 'secret_path'
                elif action == 's':
                    return 'outside_cabin'

            elif action == 'no' or action == 'n':
                print(dedent("""
                    You screamed like a little girl and ran away from them
                    """))
                return 'outside_cabin'

        print(dedent("""
            You come back to the cannibal tribe and say hello to your friends
            There is a path to your right
            """))
        action = self.dir(('s', 'd'))
        
        if action == 'd':
            return 'secret_path'
        elif action == 's':
            return 'outside_cabin'


class SecretPath(InitialRoom):
    
    def enter(self):
        if player_stats.player.stats['girl_on_path'] == False:
            player_stats.player.stats['girl_on_path'] = True
            print(dedent("""
                Whle walking along the path you see a girl that has dropped some stuff on the ground
                She hasn't noticed you yet but is about to look up at you
                Do you run over there and steal whatever you can grab for -2 mp?
                """))
            action = self.dir(('yes', 'y', 'no', 'n'))
            
            if action == 'yes' or action == 'y':
                player_stats.player.stats['morality_points'] -= 2
                player_stats.player.stats['items'] = ['map']

                print(dedent("""
                    Quickly you scurry over there and snatch piece of cloth that loooks like a map off the ground
                    The girl screams a string of curse words at you
                    If at any point you'd like to examine the map just type map
                    You can either run ahead on the path or head back
                    """))
                action = self.dir(('w', 's'))

                if action == 'w':
                    return 'south_wiggols_village'
                if action == 's':
                    return 'woods'

            elif action == 'no' or action == 'n':
                player_stats.player.stats['morality_points'] += 2
                player_stats.player.stats['items'] = ['map']
                print(dedent("""
                    As the girl looks up at you, you walk towards her
                    You help her pick up all her stuff
                    To thank you she gives you a map and tells you that A = 10
                    You earned +2 mp for helping her
                    If at any point you'd like to look at the map just type map
                    The path continues ahead of you
                    """))
                action = self.dir(('w', 's'))

                if action == 'w':
                    return 'south_wiggols_village'
                elif action == 's':
                    return 'woods'
                
        return 'south_wiggols_village'


class SouthWiggolsVillage(InitialRoom):
    
    def enter(self):
        print(dedent("""
            You are in South Wiggols Village
            There is a jobs board to your right
            To your left appears to be an abandoned house
            straight ahead will take you further into the village
            """))
        action = self.dir(('w', 'a', 's', 'd'))
        
        if action == 'w':
            return 'north_wiggols_village'
        elif action == 'a':
            return 'abandoned_house'
        elif action == 'd':
            return 'wiggols_job_board'
        elif action == 's':
            return 'woods'

class AbandonedHouse(InitialRoom):

    def enter(self):
        print('Not done yet head back')
        action = self.dir(('s'))
        if action == 's':
            return 'south_wiggols_village'


class WiggolsJobBoard(InitialRoom):

    def enter(self):
        print('Not done yet, head back')
        action = self.dir(('s',))
        if action == 's':
            return 'south_wiggols_village'


class NorthWiggolsVillage(InitialRoom):

    def enter(self):
        print(dedent("""
            You are in North Wiggols Village
            Not finished yet
            Head back
            """))
        action = self.dir(('s',))

        if action == 's':
            return 'south_wiggols_village'


class River(InitialRoom):

    def enter(self):
        if player_stats.player.stats['kid_drowning'] == False:
            print(dedent("""
                Upon approaching the river you see a kid drowning
                He's screaming for help
                You have two options
                Type yes or y to save the kid from drowning
                Type no or n to let him die
                """))
            #self.directions = ['yes', 'y', 'no']
            action = self.dir(('yes', 'y', 'no', 'n'))

            if action == 'yes' or action == 'y':
                player_stats.player.stats['kid_drowning'] = True
                player_stats.player.stats['morality_points'] += 10
                print(dedent(f"""
                    You found some rope next to you and tossed an end to the kid
                    You managed to pull him in and save his life
                    He runs away thanking you
                    This gave you 10 mp
                    """))
            elif action == 'no' or action == 'n':
                player_stats.player.stats['kid_drowning'] = True
                player_stats.player.stats['morality_points'] -= 10
                print(dedent(f"""
                    You stand there and wait till the kid dies
                    After a little while the kid stops screaming for help and floats downstream
                    Shockingly, you lose 10 mp
                    """))

        print("\nYou may follow the river upstream by going straight\n")
        action = self.dir(('s', 'w'))

        if action == 'w':
            return 'waterfall'
        elif action == 's':
            return 'outside_cabin'


class Waterfall(InitialRoom):

    def enter(self):
        print(dedent("""
            After following the river you come across a Waterfall
            There appears to be nowhere to go
            """))
        if 'map' not in (player_stats.player.stats['items']):
            action = self.dir(('s',))
        else:
            action = self.dir(('s', 'open sesame'))

        if action == 's':
            return 'river'
        elif 'map' in (player_stats.player.stats['items']) and action == 'open sesame':
            print(dedent("""
                Straight ahead, behind the Waterfall you see a door screech open
                """))
            action = self.dir(('w', 's'))

            if action == 'w':
                return 'secret_room'
            elif action == 's':
                return 'river'

class SecretRoom(InitialRoom):
    def enter(self):
        print('not done, head back')
        #door shuts after you leave
        action = self.dir(('s',))
        if action == 's':
            return 'waterfall'


class Village(InitialRoom):

    def enter(self):
        print(dedent("""
            You enter the village and there's lots of people walking around
            To your left is a brothel
            To your right is an animal rescue center
            In front of you is more of the village
            """))
        #self.directions = ['a', 'd', 's', 'w']
        action = self.dir(('a', 'd', 's', 'w'))

        if action == 'a':
            print(dedent(f"""
                Woah there sonny!
                You need -50 mp to enter here
                """))
            return 'village'

        elif action == 'd':
            print(dedent("""
                You need 50 mp to enter here
                """))
            return 'village'

        elif action == 'w':
            return 'village_homes'

        elif action == 's':
            return 'outside_cabin'


class VillageHomes(InitialRoom):
   def enter(self):
       print(dedent("""
            To your right there is house labeled 'The Dempster Residence'
            To your left is a house labeled 'The Higalra Residence'
            Straight ahead is an empty road that looks like it goes on for miles           
            """))
       
       action = self.dir(('a', 's', 'w', 'd'))
       
       if action == 'a':
           return 'higalra_residence_porch'
       elif action == 's':
           return 'village'
       elif action == 'w':
           return 'road_map'
       elif action == 'd':
           return 'dempster_residence_porch'

class ResidencePorch(InitialRoom):
    
    def __init__(self, residence_name, residence_class):
            self.residence_name = residence_name
            self.residence_class = residence_class

    def enter(self):
            print(dedent(f"""
                The {self.residence_name} Residence is locked however with a lockpick it may be picked
                Please note that there is only one lockpick and it can only be used once
                By picking the lock there is a 30% chance you will get caught
                If you get caught, you lose the lockpick, 5 mp, and you will go to jail
                Do you attempt to pick the lock for -3 mp?
                """))
            action = self.dir(('yes', 'y', 'no', 'n'))
            if 'lockpick' in player_stats.player.stats['items']:
                if action == 'yes' or action == 'y':
                    player_stats.player.stats['pick_lock'] = True
                    player_stats.player.stats['morality_points'] -= 3
                    if 'lockpick' in (player_stats.player.stats['items']):
                        player_stats.player.stats['items'].remove('lockpick')
                    
                    if randint(1, 101) >= 70:
                        # x = ....
                        return self.residence_class
                    else:
                        return 'jail'

                    
                elif action == 'no' or action == 'n':

                    print("\nWithout picking the lock there is nothing else to do here\n")
                    action = self.dir(('a', 's', 'w', 'd'))

                    if action == 's':
                        return 'village_homes'
            else:
                print(dedent("""
                    You currently do not have the lockpick so all you can do is head back
                    """))
                action = self.dir(('s',))
                if action == 's':
                    return 'village_homes'


class HigalraResidence(InitialRoom):
    
    def enter(self):
        print(dedent("""
            You are in the living room of the Higalra Residence
            There is a bedroom straight ahead
            There is a kitchen to your left
            """))
        action = self.dir(('w', 'a', 's', 'aghrial', 'Agrhial'))

        if action == 'w':
            return 'higalra_bedroom'
        elif action == 'a':
            return 'higalra_bathroom'
        elif action == 's':
            return 'higalra_residence_porch'

        if action == 'aghrial' or action == 'Aghrial':
            print(dedent("""
                A bookshelf creaks open as you utter the words
                To your right there is now a staircase leading down
                """))
            action = self.dir(('d', 's'))

            if action == 'd':
                return 'higalra_basement'
            elif action == 's':
                return 'higalra_residence_porch'


class HigalraBasement(InitialRoom):

    def enter(self):
        print(dedent("""
            After walking down the stairs it is pitch black
            You fumble around until you find a lightswitch
            After turning it on you see not sure yet
            Go back upstairs
            """))
        action = self.dir(('s',))
        if action == 's':
            print(dedent("""
                The door slams shut behind you as you return to the living room
                """))
            return 'higalra_residence'


class HigalraBedroom(InitialRoom):

    def enter(self):
        print(dedent("""
            In the bedroom there is a note that says
            ------------------------------------------------------------------
            If you are reading this it means I am dead
            I can only hope that you will continue my good work
            Everything I did was for the greater good
            Reveal my true name in the living room and it will all make sense
            ------------------------------------------------------------------
            Aside from the note, The rest of the bedroom is very empty and clean
            
            There is a bathroom to your left
            """))

        action = self.dir(('s', 'a'))

        if action == 's':
            return 'higalra_residence'
        elif action == 'a':
            return 'higalra_bathroom'


class HigalraBathroom(InitialRoom):

    def enter(self):
        print("not done yet head back")
        action = self.dir(('s',))
        if action == 's':
            return 'higalra_bedroom'


class HigalraKitchen(InitialRoom):

    def enter(self):
        print('Not done yet, go back')
        action = self.dir(('s',))
        if action == 's':
            return 'higalra_residence'

class DempsterResidence(InitialRoom):

    def enter(self):
        print("Not done yet, leave")
        action = self.dir(('s',))
        if action == 's':
            return 'dempster_residence_porch'

class Jail(InitialRoom):
    def enter(self):
        print("jail not done yet head back to village")
        action = self.dir(('s',))
        if action == 's':
            return 'village_homes'


class RoadMap(InitialRoom):
    
    def enter(self):
        print('not done yet head back')
        action = self.dir(('s',))
        if action == 's':
            return 'village_homes'
