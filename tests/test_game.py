import unittest
from unittest.mock import patch

import main
from app import app
from game_engine import GameEngine


class GameTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def choose(self, index):
        response = self.client.post("/choice", json={"choice_index": index})
        self.assertEqual(response.status_code, 200)
        return response.json

    def play_web(self, path):
        response = self.client.post("/start").json
        choices = iter(path)
        for _ in range(10):
            index = next(choices) if len(response["choices"]) > 1 else 0
            response = self.choose(index)
        self.assertIsNone(next(choices, None))
        self.assertEqual(response["text"][-1], "--- FIN ---")
        return response

    def test_each_ending_has_a_route_in_both_versions(self):
        routes = (
            ((2, 2, 0, 2, 2), "COLD CLARITY", "You sit in the silence."),
            ((0, 0, 0, 0, 0), "THE GHOST IN THE ROOM", "You close your eyes."),
            ((1, 1, 0, 1, 0), "FRACTURED", "You tear at your hair."),
            ((0, 0, 0, 0, 1), "QUIET RESIGNATION", "You sigh."),
        )
        for path, title, opening_line in routes:
            with self.subTest(ending=title):
                self.assertEqual(self.play_web(path)["text"][0], opening_line)
                with (
                    patch("main.time.sleep"),
                    patch("main.clear_screen"),
                    patch("builtins.print"),
                    patch("builtins.input", side_effect=[str(i + 1) for i in path]),
                    patch("main.type_text") as type_text,
                ):
                    main.main()
                type_text.assert_any_call(f"\nENDING: {title}")
                type_text.assert_any_call("--- FIN ---", speed=0.1)

    def test_restart_returns_to_fresh_intro(self):
        ending = self.play_web((0, 0, 0, 0, 0))
        self.assertEqual(ending["action"], "restart")
        self.assertEqual(ending["choices"], ["Restart"])
        self.assertEqual(self.client.post("/choice", json={"choice_index": 0}).status_code, 400)

        intro = self.client.post("/start").json
        self.assertEqual(intro["text"][0], "DELUSIONS EMBRACE")
        self.assertEqual(intro["choices"], ["Begin"])
        with self.client.session_transaction() as session:
            self.assertEqual(session["game_state"], GameEngine.get_initial_state())

    def test_invalid_choices_leave_state_unchanged(self):
        self.client.post("/start")
        self.assertEqual(self.client.post("/choice", json={"choice_index": 1}).status_code, 400)
        self.choose(0)
        with self.client.session_transaction() as session:
            before = session["game_state"].copy()

        for payload in ([], {}, {"choice_index": None}, {"choice_index": True},
                        {"choice_index": "0"}, {"choice_index": 0.0},
                        {"choice_index": -1}, {"choice_index": 3}):
            with self.subTest(payload=payload):
                response = self.client.post("/choice", json=payload)
                self.assertEqual(response.status_code, 400)
                self.assertIn("error", response.json)
                with self.client.session_transaction() as session:
                    self.assertEqual(session["game_state"], before)
        self.assertEqual(len(self.choose(2)["choices"]), 3)

    def test_both_versions_clamp_stats(self):
        web = GameEngine.get_initial_state()
        web["current_step"] = "act_three_choice_identity"
        GameEngine().process_step(web, 2)
        terminal = main.GameState()
        terminal.update(sanity_change=20, doubt_change=20, attachment_change=-20)
        self.assertEqual((web["sanity"], web["doubt"], web["attachment"]), (100, 20, 0))
        self.assertEqual((terminal.sanity, terminal.doubt, terminal.attachment), (100, 20, 0))
