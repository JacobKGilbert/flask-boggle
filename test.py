from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_home_route(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<a href="/board" class="start-game">Start New Game</a>', html)

    def test_init_board(self):
        with app.test_client() as client:
            res = client.get('/board')

            self.assertEqual(res.status_code, 200)
            self.assertTrue(session['board'])

    def test_board_route(self):
        with app.test_client() as client:
            res = client.get('/board')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p id="result"></p>', html)

    def test_guess_route(self):
        with app.test_client() as client:
            client.get('/board')
            res = client.post('/guess', json={'guess': 'hello'})

            self.assertEqual(res.status_code, 200)

    # def test_endgame_route(self):
    #     with app.test_client() as client:
    #         client.get('/board')
    #         res = client.post('/endgame', json={'score': 20})

    #         self.assertEqual(session['high_score'], 20)