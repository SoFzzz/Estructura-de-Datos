from Manager import Manager
from QuickSave import QuickSave

def main():
    print("===== VISUAL NOVEL QUICK SAVE TEST =====\n")

save_manager = Manager(max_saves=3)


current_scene = "Prologue"
current_line = 1
current_bg = "classroom.png"
current_flags = {
    "alice_affection": 0,
    "bob_affection": 0
}

print("Starting game...\n")


print("Player reaches a decision point. Quick Save #1")
save1 = QuickSave(current_scene, current_line, current_bg, current_flags)
save_manager.push(save1)


current_scene = "Chapter 1"
current_line = 25
current_flags["alice_affection"] += 10

print("\nPlayer advances story. Quick Save #2")
save2 = QuickSave(current_scene, current_line, current_bg, current_flags)
save_manager.push(save2)


current_scene = "Chapter 1 - Dark Route"
current_line = 40
current_bg = "dark_alley.png"
current_flags["bob_affection"] -= 20
current_flags["bad_ending"] = True

print("\nPlayer makes risky choice. Quick Save #3")
save3 = QuickSave(current_scene, current_line, current_bg, current_flags)
save_manager.push(save3)


print("\nCreating Quick Save #4 (should remove oldest save)")
current_line = 50
save4 = QuickSave(current_scene, current_line, current_bg, current_flags)
save_manager.push(save4)


print("\nTop save currently available:")
print(save_manager.top())

print("\n--- Performing Quick Loads ---")

while not save_manager.is_empty():
    loaded_state = save_manager.pop()
    print(f"Restored to: Scene={loaded_state.scene_id}, "
          f"Line={loaded_state.dialogue_line}, "
          f"Flags={loaded_state.player_flags}")
    print()

print("No more saves left.")
print("\n===== TEST FINISHED =====")


if __name__ == "__main__":
    main()