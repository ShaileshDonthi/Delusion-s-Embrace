#!/usr/bin/env python3
import sys
import time
import random

class GameState:
    def __init__(self):
        self.sanity = 100
        self.doubt = 0
        self.attachment = 0

    def update(self, sanity_change=0, doubt_change=0, attachment_change=0):
        self.sanity = max(0, min(100, self.sanity + sanity_change))
        self.doubt = max(0, min(100, self.doubt + doubt_change))
        self.attachment = max(0, min(100, self.attachment + attachment_change))

    def __str__(self):
        # For debugging purposes only
        return f"Sanity: {self.sanity}, Doubt: {self.doubt}, Attachment: {self.attachment}"

def type_text(text, speed=0.03, end="\n", delay_after=0.5):
    """
    Simulates typing effect for text.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Randomize speed slightly for human feel
        time.sleep(speed + random.uniform(-0.01, 0.01))
    sys.stdout.write(end)
    time.sleep(delay_after)

def slow_print(text, delay=1.0):
    """
    Prints text and waits.
    """
    print(text)
    time.sleep(delay)

def get_choice(options):
    """
    Presents choices and returns the index of the selected option.
    """
    print("\n")
    for i, option in enumerate(options, 1):
        print(f" {i}. {option}")
    
    while True:
        try:
            choice = input("\n> ")
            if choice.strip().isdigit():
                idx = int(choice) - 1
                if 0 <= idx < len(options):
                    return idx
        except ValueError:
            pass
        print(" ...")

def intro():
    clear_screen()
    type_text("\n\n   DELUSIONS EMBRACE", speed=0.1)
    type_text("   _________________", speed=0.05)
    time.sleep(1)
    clear_screen()

def clear_screen():
    print("\n" * 100)

# --- ACT I: THE ENCOUNTER ---
def act_one(state):
    clear_screen()
    type_text("ACT I: THE ENCOUNTER", speed=0.08, delay_after=2)
    
    type_text("You sit exhausted, in a dimly lit café that seems to mirror your sombre mood.")
    type_text("Solitude has become your constant companion.")
    type_text("The world around you appears drenched in shades of perpetual gloom.")
    
    type_text("\nThe bell above the door chimes.")
    type_text("She materializes—Irina, a specter of your darkest desires.")
    time.sleep(1)
    
    type_text("\nHaunted by your own illusions, you cautiously approach her.")
    type_text("Or does she approach you? The memory is slippery.")
    
    options = [
        "Meet her gaze. Smile.",
        "Look away. Pretend you didn't see her.",
        "Stare. Why does she feel so familiar?"
    ]
    choice = get_choice(options)
    
    if choice == 0:
        type_text("\nYou smile. It feels practiced, but she smiles back.")
        type_text("A warmth spreads in your chest. Or is it just the coffee?")
        state.update(attachment_change=10, sanity_change=0)
    elif choice == 1:
        type_text("\nYou look at the table. The wood grain swirls like a fingerprint.")
        type_text("But she is already there.")
        state.update(sanity_change=-5, doubt_change=5)
    elif choice == 2:
        type_text("\nYou can't look away. Her face is... correct.")
        type_text("A reflection of your own twisted soul.")
        state.update(doubt_change=10, attachment_change=5)

    type_text("\n\"Is this seat taken?\" she asks.")
    type_text("Her voice sounds like something you heard in a dream.")
    
    options = [
        "\"No. Please, sit.\"",
        "\"I'm expecting someone.\" (Lie)",
        "\"I don't know. Is it?\""
    ]
    choice = get_choice(options)
    
    if choice == 0:
        type_text("\nShe sits. The air around her smells like rain and old paper.")
        state.update(attachment_change=10)
    elif choice == 1:
        type_text("\nShe laughs, soft and dry. \"No you're not.\"")
        type_text("She sits anyway.")
        state.update(sanity_change=-5, doubt_change=10)
    elif choice == 2:
        type_text("\nShe tilts her head. \"That's a dangerous question.\"")
        type_text("She pulls out the chair and sits.")
        state.update(doubt_change=15)

    type_text("\nYour conversations dance precariously on the edge of madness.")
    type_text("Each word laced with a poison that seeps deeper into your fragile psyche.")
    
    return state

# --- ACT II: THE DESCENT ---
def act_two(state):
    clear_screen()
    type_text("ACT II: THE DESCENT", speed=0.08, delay_after=2)
    
    type_text("Together, you descend into the labyrinth of shared darkness.")
    type_text("Laughter, tinged with the bitter taste of despair, mingles with the consuming void.")
    
    type_text("\nTime becomes a treacherous illusion, warping and stretching.")
    type_text("How long have you been entangled within her web?")
    
    options = [
        "A day?",
        "A week?",
        "Months?"
    ]
    choice = get_choice(options)
    
    type_text("\nIt doesn't matter.")
    type_text("Days bleed into nights, nights dissolve into hazy fragments of existence.")
    type_text("The boundaries between reality and nightmare blur into an indistinguishable haze.")
    
    state.update(sanity_change=-10)

    type_text("\n\"...the city is changing. Do you see it?\" she asks.")
    
    if state.sanity < 90:
        type_text("Did she say that twice?")
    
    options = [
        "\"Yes. Everything feels different.\"",
        "\"I think I need to leave.\"",
        "\"Why are you repeating yourself?\""
    ]
    choice = get_choice(options)
    
    if choice == 0:
        type_text("\nShe nods. \"It's shedding its skin. Just for us.\"")
        state.update(attachment_change=10, sanity_change=-5)
    elif choice == 1:
        type_text("\n\"Leave?\" She touches your hand. Her skin is cold.")
        type_text("\"Where would you go? Out there? It's not safe.\"")
        state.update(sanity_change=-10, doubt_change=10)
    elif choice == 2:
        type_text("\nHer expression doesn't change.")
        type_text("\"I'm not repeating myself. You're just listening closer.\"")
        state.update(doubt_change=15, sanity_change=-5)
    
    return state

# --- ACT III: THE FRACTURE ---
def act_three(state):
    clear_screen()
    type_text("ACT III: THE FRACTURE", speed=0.08, delay_after=2)
    
    type_text("On that fateful evening, flickering candles cast their dancing shadows.")
    type_text("You find yourself entwined in a macabre embrace.")
    type_text("The atmosphere of the café seems tainted, emanating a suffocating stench of decay.")
    
    type_text("\nHer hand, icy and lifeless, quivers within yours.")
    type_text("You feel no warmth, no connection.")
    type_text("A disquieting realization settles upon you; something is horribly amiss.")
    
    type_text("\nThen, reality strikes with the force of a venomous serpent.")
    
    # Glitching effect logic (simple)
    glitch_text = "Irina's features contort."
    if state.sanity < 70:
        glitch_text = "Irina's f e a t u r e s  c o n t o r t."
    
    type_text(f"\n{glitch_text}")
    type_text("Transforming into a grotesque visage that mirrors your fractured mind.")
    type_text("Her eyes turn hollow, devoid of life. A sadistic smile stretches across her lips.")
    
    type_text("\n\"You know what I am,\" she hisses.")
    
    options = [
        "\"My love.\"",
        "\"A monster.\"",
        "\"Nothing.\""
    ]
    choice = get_choice(options)
    
    if choice == 0:
        state.update(attachment_change=20, sanity_change=-20)
        type_text("\n\"Yes,\" she mocks. \"Your twisted, beautiful lie.\"")
    elif choice == 1:
        state.update(sanity_change=10, doubt_change=10)
        type_text("\n\"I am only what you made me.\"")
    elif choice == 2:
        state.update(sanity_change=20, doubt_change=20, attachment_change=-20)
        type_text("\nShe laughs, and the sound is like glass breaking.")

    return state

# --- ACT IV: THE REVEAL ---
def act_four(state):
    clear_screen()
    type_text("ACT IV: THE REVEAL", speed=0.08, delay_after=2)
    
    type_text("\"I do not exist,\" she hisses.")
    type_text("\"I am but a creation of your diseased imagination.\"")
    type_text("\"A manifestation of your darkest horrors and depravities.\"")
    type_text("\"I am merely a fragment of your crumbling sanity.\"")
    
    time.sleep(1)
    
    type_text("\nOverwhelmed by despair, you reach out.")
    type_text("Desperate to cling to the last vestiges of her presence.")
    type_text("But your trembling hand grasps only emptiness.")
    type_text("The void swallows her ethereal form.")
    
    type_text("\nIrina dissolves into the shadows.")
    type_text("Leaving you abandoned in a desolate wasteland of your own making.")
    
    time.sleep(2)
    clear_screen()
    
    type_text("You are alone in the room.")
    type_text("There is no cafe.")
    
    # Ending logic
    if state.sanity > 80 and state.doubt > 50:
        ending_clarity()
    elif state.attachment > 80:
        ending_delusion()
    elif state.sanity < 40:
        ending_collapse()
    else:
        ending_resignation()

def ending_clarity():
    type_text("\nENDING: COLD CLARITY")
    type_text("You sit in the silence.")
    type_text("You created her because the solitude was too heavy.")
    type_text("But now the weight is back.")
    type_text("So yeah, that's how you found out you were delusional.")
    type_text("At least now you know the truth.")

def ending_delusion():
    type_text("\nENDING: THE GHOST IN THE ROOM")
    type_text("You close your eyes.")
    type_text("She said she didn't exist.")
    type_text("But when you whisper her name, you hear her answer.")
    type_text("\"I'm still here,\" she says.")
    type_text("So yeah, maybe you are delusional.")
    type_text("But isn't this better than being alone?")

def ending_collapse():
    type_text("\nENDING: FRACTURED")
    type_text("You tear at your hair.")
    type_text("Where did she go? Where did the world go?")
    type_text("She's screaming inside your head.")
    type_text("So yeah, that's how you found out you were delusional.")
    type_text("But knowing it doesn't make the screaming stop.")

def ending_resignation():
    type_text("\nENDING: QUIET RESIGNATION")
    type_text("You sigh.")
    type_text("The daydream fades, leaving a bitter taste.")
    type_text("Irina was never there.")
    type_text("Just a collection of moments you wished you had.")
    type_text("So yeah, that's how you found out you were delusional.")
    type_text("You turn off the light.")

def main():
    state = GameState()
    intro()
    
    state = act_one(state)
    state = act_two(state)
    state = act_three(state)
    act_four(state)
    
    print("\n\n")
    type_text("--- FIN ---", speed=0.1)
    time.sleep(2)

if __name__ == "__main__":
    main()
