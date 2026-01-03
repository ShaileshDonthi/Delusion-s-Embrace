import random

class GameEngine:
    def __init__(self):
        # We don't store state here in a web app, state is passed in/out.
        # But we define the structure of the story here.
        pass

    @staticmethod
    def get_initial_state():
        return {
            "sanity": 100,
            "doubt": 0,
            "attachment": 0,
            "current_step": "intro",
            "history": [] # List of text lines shown so far
        }

    def process_step(self, state, choice_index=None):
        step_id = state.get("current_step", "intro")
        
        # Dispatcher
        if step_id == "intro":
            return self._step_intro(state, choice_index)
        elif step_id == "act_one_start":
            return self._step_act_one_start(state)
        elif step_id == "act_one_choice_1":
            return self._step_act_one_choice_1(state, choice_index)
        elif step_id == "act_one_choice_2":
            return self._step_act_one_choice_2(state, choice_index)
        elif step_id == "act_one_long_time":
            return self._step_act_one_long_time(state)
        elif step_id == "act_two_start":
            return self._step_act_two_start(state)
        elif step_id == "act_two_choice_time":
            return self._step_act_two_choice_time(state, choice_index)
        elif step_id == "act_two_loop":
            return self._step_act_two_loop(state)
        elif step_id == "act_two_choice_loop":
            return self._step_act_two_choice_loop(state, choice_index)
        elif step_id == "act_three_start":
            return self._step_act_three_start(state)
        elif step_id == "act_three_choice_identity":
            return self._step_act_three_choice_identity(state, choice_index)
        elif step_id == "act_four_reveal":
            return self._step_act_four_reveal(state)
        elif step_id == "act_four_ending":
            return self._step_act_four_ending(state)
        
        return {"text": ["Error: Unknown step"], "choices": [], "next_step": "intro"}

    # --- Step Implementations ---

    def _step_intro(self, state, choice_index=None):
        if choice_index is not None:
            return self._step_act_one_start(state)

        return {
            "text": [
                "DELUSIONS EMBRACE",
                "_________________"
            ],
            "choices": ["Begin"],
            "next_step": "act_one_start"
        }

    def _step_act_one_start(self, state):
        # Initial prose
        text = [
            "You sit exhausted, in a dimly lit café that seems to mirror your sombre mood.",
            "Solitude has become your constant companion.",
            "The world around you appears drenched in shades of perpetual gloom.",
            "",
            "The bell above the door chimes.",
            "She materializes—Irina, a specter of your darkest desires.",
            "",
            "Haunted by your own illusions, you cautiously approach her.",
            "Or does she approach you? The memory is slippery."
        ]
        choices = [
            "Meet her gaze. Smile.",
            "Look away. Pretend you didn't see her.",
            "Stare. Why does she feel so familiar?"
        ]
        # Update state for next step
        state["current_step"] = "act_one_choice_1"
        return {"text": text, "choices": choices}

    def _step_act_one_choice_1(self, state, choice_index):
        text = []
        if choice_index == 0:
            text = [
                "You smile. It feels practiced, but she smiles back.",
                "A warmth spreads in your chest. Or is it just the coffee?"
            ]
            state["attachment"] += 10
        elif choice_index == 1:
            text = [
                "You look at the table. The wood grain swirls like a fingerprint.",
                "But she is already there."
            ]
            state["sanity"] -= 5
            state["doubt"] += 5
        elif choice_index == 2:
            text = [
                "You can't look away. Her face is... correct.",
                "A reflection of your own twisted soul."
            ]
            state["doubt"] += 10
            state["attachment"] += 5
        
        text.append("")
        text.append("\"Is this seat taken?\" she asks.")
        text.append("Her voice sounds like something you heard in a dream.")

        choices = [
            "\"No. Please, sit.\"",
            "\"I'm expecting someone.\" (Lie)",
            "\"I don't know. Is it?\""
        ]
        state["current_step"] = "act_one_choice_2"
        return {"text": text, "choices": choices}

    def _step_act_one_choice_2(self, state, choice_index):
        text = []
        if choice_index == 0:
            text = ["She sits. The air around her smells like rain and old paper."]
            state["attachment"] += 10
        elif choice_index == 1:
            text = [
                "She laughs, soft and dry. \"No you're not.\"",
                "She sits anyway."
            ]
            state["sanity"] -= 5
            state["doubt"] += 10
        elif choice_index == 2:
            text = [
                "She tilts her head. \"That's a dangerous question.\"",
                "She pulls out the chair and sits."
            ]
            state["doubt"] += 15
        
        text.append("")
        text.append("Your conversations dance precariously on the edge of madness.")
        text.append("Each word laced with a poison that seeps deeper into your fragile psyche.")

        choices = ["Continue"]
        state["current_step"] = "act_two_start"
        return {"text": text, "choices": choices}

    def _step_act_two_start(self, state, choice_index=None):
        text = [
            "Together, you descend into the labyrinth of shared darkness.",
            "Laughter, tinged with the bitter taste of despair, mingles with the consuming void.",
            "",
            "Time becomes a treacherous illusion, warping and stretching.",
            "How long have you been entangled within her web?"
        ]
        choices = [
            "A day?",
            "A week?",
            "Months?"
        ]
        state["current_step"] = "act_two_choice_time"
        return {"text": text, "choices": choices}

    def _step_act_two_choice_time(self, state, choice_index):
        text = [
            "It doesn't matter.",
            "Days bleed into nights, nights dissolve into hazy fragments of existence.",
            "The boundaries between reality and nightmare blur into an indistinguishable haze."
        ]
        state["sanity"] -= 10
        
        text.append("")
        text.append("\"...the city is changing. Do you see it?\" she asks.")
        
        if state["sanity"] < 90:
            text.append("Did she say that twice?")
        
        choices = [
            "\"Yes. Everything feels different.\"",
            "\"I think I need to leave.\"",
            "\"Why are you repeating yourself?\""
        ]
        state["current_step"] = "act_two_choice_loop"
        return {"text": text, "choices": choices}

    def _step_act_two_choice_loop(self, state, choice_index):
        text = []
        if choice_index == 0:
            text = ["She nods. \"It's shedding its skin. Just for us.\""]
            state["attachment"] += 10
            state["sanity"] -= 5
        elif choice_index == 1:
            text = [
                "\"Leave?\" She touches your hand. Her skin is cold.",
                "\"Where would you go? Out there? It's not safe.\""
            ]
            state["sanity"] -= 10
            state["doubt"] += 10
        elif choice_index == 2:
            text = [
                "Her expression doesn't change.",
                "\"I'm not repeating myself. You're just listening closer.\""
            ]
            state["doubt"] += 15
            state["sanity"] -= 5
            
        choices = ["Continue"]
        state["current_step"] = "act_three_start"
        return {"text": text, "choices": choices}

    def _step_act_three_start(self, state, choice_index=None):
        text = [
            "On that fateful evening, flickering candles cast their dancing shadows.",
            "You find yourself entwined in a macabre embrace.",
            "The atmosphere of the café seems tainted, emanating a suffocating stench of decay.",
            "",
            "Her hand, icy and lifeless, quivers within yours.",
            "You feel no warmth, no connection.",
            "A disquieting realization settles upon you; something is horribly amiss.",
            "",
            "Then, reality strikes with the force of a venomous serpent."
        ]
        
        glitch_text = "Irina's features contort."
        if state["sanity"] < 70:
            glitch_text = "Irina's f e a t u r e s  c o n t o r t."
        
        text.append(glitch_text)
        text.append("Transforming into a grotesque visage that mirrors your fractured mind.")
        text.append("Her eyes turn hollow, devoid of life. A sadistic smile stretches across her lips.")
        
        text.append("")
        text.append("\"You know what I am,\" she hisses.")
        
        choices = [
            "\"My love.\"",
            "\"A monster.\"",
            "\"Nothing.\""
        ]
        state["current_step"] = "act_three_choice_identity"
        return {"text": text, "choices": choices}

    def _step_act_three_choice_identity(self, state, choice_index):
        text = []
        if choice_index == 0:
            state["attachment"] += 20
            state["sanity"] -= 20
            text = ["\"Yes,\" she mocks. \"Your twisted, beautiful lie.\""]
        elif choice_index == 1:
            state["sanity"] += 10
            state["doubt"] += 10
            text = ["\"I am only what you made me.\""]
        elif choice_index == 2:
            state["sanity"] += 20
            state["doubt"] += 20
            state["attachment"] -= 20
            text = ["She laughs, and the sound is like glass breaking."]
            
        choices = ["Continue"]
        state["current_step"] = "act_four_reveal"
        return {"text": text, "choices": choices}

    def _step_act_four_reveal(self, state, choice_index=None):
        text = [
            "\"I do not exist,\" she hisses.",
            "\"I am but a creation of your diseased imagination.\"",
            "\"A manifestation of your darkest horrors and depravities.\"",
            "\"I am merely a fragment of your crumbling sanity.\"",
            "",
            "Overwhelmed by despair, you reach out.",
            "Desperate to cling to the last vestiges of her presence.",
            "But your trembling hand grasps only emptiness.",
            "The void swallows her ethereal form.",
            "",
            "Irina dissolves into the shadows.",
            "Leaving you abandoned in a desolate wasteland of your own making.",
            "",
            "You are alone in the room.",
            "There is no cafe."
        ]
        
        choices = ["End"]
        state["current_step"] = "act_four_ending"
        return {"text": text, "choices": choices}

    def _step_act_four_ending(self, state, choice_index=None):
        text = []
        sanity = state["sanity"]
        doubt = state["doubt"]
        attachment = state["attachment"]

        if sanity > 80 and doubt > 50:
            text = [
                "You sit in the silence.",
                "You created her because the solitude was too heavy.",
                "But now the weight is back.",
                "So yeah, that's how you found out you were delusional.",
                "At least now you know the truth."
            ]
        elif attachment > 80:
            text = [
                "You close your eyes.",
                "She said she didn't exist.",
                "But when you whisper her name, you hear her answer.",
                "\"I'm still here,\" she says.",
                "So yeah, maybe you are delusional.",
                "But isn't this better than being alone?"
            ]
        elif sanity < 40:
            text = [
                "You tear at your hair.",
                "Where did she go? Where did the world go?",
                "She's screaming inside your head.",
                "So yeah, that's how you found out you were delusional.",
                "But knowing it doesn't make the screaming stop."
            ]
        else:
            text = [
                "You sigh.",
                "The daydream fades, leaving a bitter taste.",
                "Irina was never there.",
                "Just a collection of moments you wished you had.",
                "So yeah, that's how you found out you were delusional.",
                "You turn off the light."
            ]
            
        text.append("")
        text.append("--- FIN ---")
        
        # Reset or disable choices
        state["current_step"] = "intro" # Loop back or just end
        choices = ["Restart"]
        return {"text": text, "choices": choices}
