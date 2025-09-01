import time

def get_words_from_user(prompts):
    """
    A helper function to get a dictionary of words from the user.
    Args:
        prompts (list): A list of strings, where each string is a prompt for a word.
    Returns:
        dict: A dictionary where keys are the prompts and values are the user's input.
    """
    user_words = {}
    print("\nPlease provide the following words:")
    for prompt in prompts:
        key = prompt.lower().replace(" ", "_").replace(":", "")
        # BUG FIX: Add a loop to ensure the user provides a non-empty word.
        while True:
            user_input = input(f"{prompt}: ")
            if user_input.strip(): # Check if the input is not just whitespace
                user_words[key] = user_input
                break
            else:
                print("Please enter a word.")
    return user_words




def story_space_adventure():
    """Runs the Space Adventure themed Mad Libs story."""
    print("\n--- Story 1: A Day in Outer Space ---")
    prompts = [
        "An adjective",
        "A planet name",
        "A verb ending in -ing",
        "A type of liquid",
        "A plural noun",
        "A silly word",
        "A number"
    ]
    words = get_words_from_user(prompts)

    story = (
        f"\nOur spaceship journey to the {words['a_planet_name']} was {words['an_adjective']}. "
        f"We spent the whole day {words['a_verb_ending_in_-ing']} on the ship's bridge. "
        f"Suddenly, the captain shouted, '{words['a_silly_word']}!' and spilled his {words['a_type_of_liquid']} "
        f"all over the control panel. This caused the ship to be overrun by {words['a_plural_noun']}. "
        f"We had to eject all {words['a_number']} of them out of the airlock!"
    )
    print(story)

def story_castle_quest():
    """Runs the Castle Quest themed Mad Libs story."""
    print("\n--- Story 2: The Quest for the Lost Scepter ---")
    prompts = [
        "A mythical creature",
        "A verb (past tense)",
        "An adjective",
        "A type of container",
        "A magical spell",
        "A room in a house",
        "A plural noun"
    ]
    words = get_words_from_user(prompts)

    story = (
        f"\nThe brave knight encountered a fearsome {words['a_mythical_creature']} guarding the castle. "
        f"The knight bravely {words['a_verb_(past_tense)']} past the beast. Inside, the castle was {words['an_adjective']}. "
        f"In the main {words['a_room_in_a_house']}, the knight found the lost scepter inside a {words['a_type_of_container']}. "
        f"But it was protected by a magical force! The knight shouted '{words['a_magical_spell']}' and grabbed it. "
        f"The kingdom was safe, all thanks to the knight's collection of {words['a_plural_noun']}."
    )
    print(story)
    
def story_school_day():
    """Runs the funny School Day themed Mad Libs story."""
    print("\n--- Story 3: A Very Strange School Day ---")
    prompts = [
        "A college class",
        "An adjective",
        "An activity",
        "A place",
        "An animal (plural)",
        "An adverb (e.g., slowly, quickly)"
    ]
    words = get_words_from_user(prompts)

    story = (
        f"\n{words['a_college_class']} class was really {words['an_adjective']} today. We learned how to "
        f"{words['an_activity']} today in class. Our professor then took us to the nearby {words['a_place']} "
        f"where we saw a group of wild {words['an_animal_(plural)']} behaving very {words['an_adverb_(e.g.,_slowly,_quickly)']}. "
        f"I can't wait for tomorrow's class!"
    )
    print(story)

def story_pirate_adventure():
    """Runs the Pirate Adventure themed Mad Libs story."""
    print("\n--- Story 4: The Pirate's Treasure ---")
    prompts = [
        "An adjective",
        "A type of bird",
        "A verb (past tense)",
        "A body part",
        "A noun",
        "A liquid",
        "A plural noun"
    ]
    words = get_words_from_user(prompts)

    story = (
        f"\nThe {words['an_adjective']} pirate and his trusty {words['a_type_of_bird']} sailed the seven seas. "
        f"One day, they {words['a_verb_(past_tense)']} upon a hidden island. The pirate hurt his {words['a_body_part']} "
        f"while digging for treasure. Inside the chest, he found a golden {words['a_noun']} and a bottle of {words['a_liquid']}. "
        f"He celebrated by sharing the {words['a_plural_noun']} with his crew."
    )
    print(story)

def story_detective_mystery():
    """Runs the Detective Mystery themed Mad Libs story."""
    print("\n--- Story 5: The Detective's Case ---")
    prompts = [
        "A famous detective's name",
        "A room in a house",
        "A verb ending in -ing",
        "An item of clothing",
        "A silly adjective",
        "A number",
        "A type of food"
    ]
    words = get_words_from_user(prompts)

    story = (
        f"\nDetective {words['a_famous_detective\'s_name']} arrived at the crime scene. In the {words['a_room_in_a_house']}, "
        f"something was {words['a_verb_ending_in_-ing']}. The only clue was a single {words['an_item_of_clothing']}. "
        f"The detective said, 'This is a very {words['a_silly_adjective']} case!' After {words['a_number']} "
        f"hours, he solved it. The culprit was after the last slice of {words['a_type_of_food']}!"
    )
    print(story)


def main():
    """Main function to run the Mad Libs game."""
    print("--- Welcome to Interactive Mad Libs! ---")
    
    while True:
        print("\nChoose a story to play:")
        print("1. A Day in Outer Space")
        print("2. The Quest for the Lost Scepter")
        print("3. A Very Strange School Day")
        print("4. The Pirate's Treasure")
        print("5. The Detective's Case")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            story_space_adventure()
        elif choice == '2':
            story_castle_quest()
        elif choice == '3':
            story_school_day()
        elif choice == '4':
            story_pirate_adventure()
        elif choice == '5':
            story_detective_mystery()
        elif choice == '6':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        time.sleep(2) # Pause for a moment before showing the menu again

if __name__ == "__main__":
    main()

