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
                    h will move left
                    j will move back
                    k will move forward
                    l will move right
                    ---------------------------------------
                    When presented with a choice to do something:
                    yes will agree to something
                    no will disagree to something

                    mp will dislpay current score
                    """))
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
            Aghrial stopped a murder from happening
            Only days later the man that he saved killed hundreds
            
            This game will allow you to choose between good and bad
            Sometimes chosing the wrong thing will lead to
            greater morality points (mp) and vice versa
            You may choose to achieve a score of 100 mp or -100 mp
            If you only choose choices of one side then the game will be imposiible to win
            ---------------------------------------
            The directions to move are as follows:
            h will move left
            j will move back
            k will move forward
            l will move right
            ---------------------------------------
            When presented with a choice to do something:
            yes will agree to something
            no will disagree to something
            ---------------------------------------
            Typing mp will give you your current score
            
            If at any point you are unsure of all available actions just type help

            
            There's a magical door right in front of you
            """))
        action = self.dir(('k',))

        if action == 'k':
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
        #self.directions = ['k', 'l', 'j']
        action = self.dir(('k', 'l', 'j'))

        if action == 'k':
            return 'outside_cabin'
        elif action == 'l':
            return 'cabin_bathroom'
        elif action == 'j':
            return 'cabin_bedroom'


class CabinBathroom(InitialRoom):
    
    def enter(self):
        if player_stats.player.stats['drugs'] == False:
            #self.directions = ['yes', 'no']
            print(dedent("""
                There is a bottle of Xeron Elixir in the bathroom
                The label is scraped off, you don't know what it'll do
                Do you steal it for -5 mp?
                """))
            action = self.dir(('yes', 'no'))

            if action == 'yes':
                player_stats.player.stats['drugs'] = True
                player_stats.player.stats['morality_points'] -= 5
                print(dedent(f"""
                    After taking the l your whole body feels amazing
                    """))

            elif action == 'no':
                print(dedent(f"""
                    You refrained from stealing drugs
                    """))
    
        print(dedent("""
            There is nothing else in the bathroom to use
            All you can do is head back
            """))
        #self.directions = ['j']
        action = self.dir(('j',))

        if action == 'j':
            return 'cabin_main_room'


class CabinBedroom(InitialRoom):

    def enter(self):
        if player_stats.player.stats['cleaned_room'] == False:
            print(dedent("""
                The bedroom is messy
                Do you clean it for +5 mp?
                """))
            #self.directions = ['yes', 'no']
            action = self.dir(('yes', 'no'))

            if action == 'yes':
                player_stats.player.stats['cleaned_room'] = True
                player_stats.player.stats['morality_points'] += 3

                print(dedent(f"""
                    While cleaning the room you came upon a lockpick
                    Do you steal it for -5 mp?
                    """))
                action = self.dir(('yes', 'no'))
                if action == 'yes':
                    player_stats.player.stats['morality_points'] -= 5
                    print("\nYou slide the lockpick into your pocket")
                    player_stats.player.stats['items'] = ['lockpick']

                elif action == 'no':
                    print("\nThe lockpick is left where it is")

            elif action == 'no':
                player_stats.player.stats['morality_points'] -= 1
                print(dedent(f"""
                    Ha!
                    You left the room messy
                    For doing such an evil thing you lost a morality point
                    """))

        print("There is nothing else to do in the bedroom")
        #self.directions = ['j']
        action = self.dir(('j',))

        if action == 'j':
            return 'cabin_main_room'


class OutsideCabin(InitialRoom):

    def enter(self):
        print(dedent("""
            It's a beautiful sunny day outside
            To your left is a river
            To your right is the woods
            Straight ahead is a village
             """))
        #self.directions = ['h', 'j', 'k', 'l']
        action = self.dir(('h', 'j', 'k', 'l'))

        if action == 'h':
            return 'river'
        elif action == 'j':
            return 'cabin_main_room'
        elif action == 'k':
            return 'village'
        elif action == 'l':
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
            #self.directions = ['yes', 'no']
            action = self.dir(('yes', 'no'))

            if action == 'yes':
                player_stats.player.stats['cannibals'] = True
                player_stats.player.stats['morality_points'] -= 5
                print(dedent(f"""
                    You ate the meat and feel full
                    They thank you for eating with them and show you a secret path to the right
                    """))
                #Have path continue here later on instead of head back
                action = self.dir(('j', 'l'))

                if action == 'l':
                    return 'secret_path'
                elif action == 'j':
                    return 'outside_cabin'

            elif action == 'no':
                print(dedent("""
                    You screamed like a little girl and ran away from them
                    """))
                return 'outside_cabin'

        print(dedent("""
            You come back to the cannibal tribe and say hello to your friends
            There is a path to your right
            """))
        #self.directions = ['j']
        action = self.dir(('j', 'k'))
        
        if action == 'l':
            return 'secret_path'
        elif action == 'j':
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
            action = self.dir(('yes', 'no'))
            
            if action == 'yes':
                print(dedent("""
                    Quickly you scurry over there and snatch piece of cloth that loooks like a map off the ground
                    The girl screams a string of curse words at you
                    If at any point you'd like to examine the map just type map
                    You can either run ahead on the path or head back
                    """))
                action = self.dir(('k', 'j'))

                if action == 'k':
                    return 'wiggols_village'
                if action == 'j':
                    return 'woods'

            elif action == 'no':
                player_stats.player.stats['morality_points'] += 2
                print(dedent("""
                    As the girl looks up at you, you walk towards her
                    You help her pick up all her stuff
                    To thank you she gives you a map and tells you that A = 10
                    You earned +3 mp for helping her
                    If at any point you'd like to look at the map just type map
                    The path continues ahead of you
                    """))
                action = self.dir(('k', 'j'))

                if action == 'k':
                    return 'wiggols_village'
                elif action == 'j':
                    return 'woods'
                
        return 'wiggols_village'




class WiggolsVillage(InitialRoom):
    
    def enter(self):
        print(dedent("""
            You find your way into a place called Wiggols Village
            There is a jobs board to your right
            To your left appears to be an abandoned house
            straight ahead will take you further into the village
            """))


class River(InitialRoom):

    def enter(self):
        if player_stats.player.stats['kid_drowning'] == False:
            print(dedent("""
                Upon approaching the river you see a kid drowning
                He's screaming for help
                You have two options
                Type yes to save the kid from drowning
                Type no to pretend like you didn't see him and return to outside the cabin
                """))
            #self.directions = ['yes', 'no']
            action = self.dir(('yes', 'no'))

            if action == 'yes':
                player_stats.player.stats['kid_drowning'] = True
                player_stats.player.stats['morality_points'] += 10
                print(dedent(f"""
                    You found some rope next to you and tossed an end to the kid
                    You managed to pull him in and save his life
                    He runs away thanking you
                    This gave you 10 mp
                    """))
            elif action == 'no':
                player_stats.player.stats['kid_drowning'] = True
                player_stats.player.stats['morality_points'] -= 10
                print(dedent(f"""
                    You casually just turn around and walk back to outside the cabin
                    After a little while the kid stops screaming for help
                    Shockingly you lose 10 mp
                    """))
                return 'outside_cabin'

        print("There is nothing to do here anymore")
        #self.directions = ['j']
        action = self.dir(('j',))

        if action == 'j':
            return 'outside_cabin'


class Village(InitialRoom):

    def enter(self):
        print(dedent("""
            You enter the village and there's lots of people walking around
            To your left is a brothel
            To your right is an animal rescue center
            In front of you is more of the village
            """))
        #self.directions = ['h', 'l', 'j', 'k']
        action = self.dir(('h', 'l', 'j', 'k'))

        if action == 'h':
            print(dedent(f"""
                Woah there sonny!
                You need -50 mp to enter here
                """))
            return 'village'

        elif action == 'l':
            print(dedent("""
                You need 50 mp to enter here
                """))
            return 'village'

        elif action == 'k':
            return 'village_homes'

        elif action == 'j':
            return 'outside_cabin'


class VillageHomes(InitialRoom):
   def enter(self):
       print(dedent("""
            To your right there is house labeled 'The Dempster Residence'
            To your left is a house labeled 'The Higalra Residence'
            Straight ahead is an empty road that looks like it goes on for miles           
            """))
       
       action = self.dir(('h', 'j', 'k', 'l'))
       
       if action == 'h':
           return 'higalra_residence_porch'
       elif action == 'j':
           return 'village'
       elif action == 'k':
           return 'roadmap'
       elif action == 'l':
           return 'dempster_residence_porch'

class ResidencePorch(InitialRoom):

    def enter(self, residence_name, residence_class):
            self.residence_name = residence_name
            self.residence_class = residence_class
            print(dedent(f"""
                The {self.residence_name} Residence is locked however with a lockpick it may be picked
                Please note that there is only one lockpick and it can only be used once
                By picking the lock there is a 30% chance you will get caught
                If you get caught, you lose the lockpick, 5 mp, and you will go to jail
                Do you attempt to pick the lock for -3 mp?
                """))
            action = self.dir(('yes', 'no'))

            if action == 'yes':
                player_stats.player.stats['pick_lock'] = True
                player_stats.player.stats['morality_points'] -= 3
                player_stats.player.stats['items'].remove('lockpick')
                
                if randint(1, 101) >= 70:
                    # x = ....
                    return self.residence_class
                else:
                    return 'jail'

                
            elif action == 'no':

                print("\nWithout picking the lock there is nothing else to do here\n")
                action = self.dir(('h', 'j', 'k', 'l'))

                if action == 'j':
                    return 'village_homes'



class HigalraResidencePorch(ResidencePorch):
    
    def enter(self):
        super(HigalraResidencePorch, self).enter('Higarla', 'higalra_residence')
        # return x?


class DempsterResidencePorch(ResidencePorch):
    
    def enter(self):
        super(DempsterResidencePorch, self).enter('Dempster', 'dempster_residence')

class HigalraResidence(InitialRoom):
    print("higarla")

class DempsterResidence(InitialRoom):
    print("dempster")

class Jail(InitialRoom):
    print("jail")
