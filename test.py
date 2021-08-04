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
            self.assertIn('<h1>Boggle Game Home</h1>', html)

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
            self.assertIn('test', html)
