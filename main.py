# Modified from Tevin Coles by Austin Earl on 5/19/2023
# Story Copyright: Tevin Coles 2023
from typing import Dict, List


class Option:
    def __init__(self, option: str, reference: int = -1):
        self.option = option
        self.reference = reference


class Scene:
    def __init__(self, id: int, scene: str, options: List[Option], instant_move_to: int = None, end_game=False):
        self.id = id
        self.scene = scene
        self.options = options
        self.end_game = end_game
        self.instant_move_to = instant_move_to


scenes: Dict[int, Scene] = {}

scenes[-1] = Scene(-1, 'NOT IMPLEMENTED YET', [Option('RESTART', 1)])

scenes[1] = Scene(1, 'The trail forks to the left and the right. Which path do you take?',
                  [Option('Left', 2), Option('Right', 7), Option('Turn Around', 11)])
scenes[2] = Scene(2, 'If you choose to go left at the fork in the trail, it will lead you deeper into the forest. The '
                     'trees become denser here, blocking out much of the sunlight and casting dappled shadows on the '
                     'ground. As you continue along the winding path, you notice that the underbrush becomes thicker '
                     'and more tangled, making it harder to see what lies ahead. Do you continue to forge ahead? Or do '
                     'you turn back?', [Option('Keep Going', 3), Option('Turn Back', 1)])
scenes[3] = Scene(3, 'As you forge onward, you come across a small clearing with a babbling brook running through its '
                     'center. The sound of rushing water is soothing. Do you stop and rest? Do you drink from the '
                     'brook? Do you press onward? Or turn back?',
                  [Option('Rest', 4), Option('Drink', 5), Option('Keep Going', 6)])
scenes[4] = Scene(4,
                  'As you rest by the brook, you feel yourself slowly slip into a dreamless sleep. However you never '
                  'wake up.... The End.',
                  [], end_game=True)
scenes[5] = Scene(5,
                  'As you take a sip from the babbling brook, the cold water clears your mind. You realize that the '
                  'only way home is back the way you came. However...',
                  [], instant_move_to=1)
scenes[6] = Scene(6,
                  'As you continue onward, you slip and fall into a ravine. Your death is painful, but quick. The End.',
                  [], end_game=True)
scenes[7] = Scene(7,
                  'As you progress along the right fork, the trail twists and turns, eventually getting you hoplessly '
                  'lost. You can see a hill in the distance and you seem to be going that direction. Do you climb a '
                  'tree for a better vantage point? Do you continue on towards the hill? Or do you try to find your '
                  'way back?',
                  [Option('Climb Tree', 10), Option('Go Towards Hill', 8), Option('Turn Back', 8)])
scenes[8] = Scene(8, 'Just when you think all hope is lost, and you\'re never going to make it out of this forest...',
                  [], instant_move_to=1)
scenes[9] = Scene(9,
                  'As you get close to the hill, the sunlight peeks out above the clouds! As you near the crest, '
                  'the view opens before you, and you realize that you weren\'t that lost to begin with. You can '
                  'clearly see the path home from here. Everything will be all right. Congratulations, you made it! ',
                  [], end_game=True)
scenes[10] = Scene(10,
                   'As you get close to the top of the tree you realize that you weren\'t that lost to begin with. '
                   'You can clearly see the path home from here. Everything will be all right. Congratulations, '
                   'you made it! ',
                   [], end_game=True)
scenes[11] = Scene(11, 'You turn around, but somehow the trail keep leading you back to this fork...',
                   [], instant_move_to=1)


def showScene(scene: Scene):
    print(scene.scene)


def runScene(scene: Scene) -> int:
    showScene(scene)
    return runOptions(scene)


def runOptions(scene: Scene):
    if scene.instant_move_to is None:
        return askPrompt(scene)
    else:
        return scene.instant_move_to


def askPrompt(scene: Scene) -> int:
    while True:
        prompt_words = ', '.join(f"'{o.option}'" for o in scene.options)
        result = input(f"{prompt_words}: ")

        for option in scene.options:
            if result.upper() == option.option.upper():
                return option.reference
        print(f"That wasn't one of the options.")


selected_scene = scenes[1]
kill_game = False
print("Let's play a game! You are walking down a trail. You come to a fork in the trail.")

while not kill_game:
    if selected_scene.end_game:
        showScene(selected_scene)
        kill_game = True
    else:
        ref = runScene(selected_scene)
        selected_scene = scenes[ref]
