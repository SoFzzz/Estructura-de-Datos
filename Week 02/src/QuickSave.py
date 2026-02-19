import copy
class QuickSave:
    ## """Represents a snapshot of a Visual Novel at a specific dialogue line.""" ##
    def __init__(self, scene_id, dialogue_line, bg_image, player_flags):
        self.scene_id = scene_id
        self.dialogue_line = dialogue_line
        self.bg_image = bg_image
        self.player_flags = copy.deepcopy(player_flags)

    def __str__(self):
        return (f"[Scene: '{self.scene_id}' | Line: {self.dialogue_line} | "
                f"BG: {self.bg_image} | Flags: {self.player_flags}]")