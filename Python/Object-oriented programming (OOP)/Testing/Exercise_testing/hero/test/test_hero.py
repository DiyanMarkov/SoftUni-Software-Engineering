from unittest import TestCase, main

from project import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Hero", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_initialization(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_hero_can_not_fight_himself_raises(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_is_zero_raises(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_hero_with_0_health_raises(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_battle_draw_both_players_drop_health_below_zero(self):
        self.hero.damage = 150
        self.enemy.damage = 150

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)


    def test_battle_enemy_health_drops_below_zero(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(-50, self.enemy.health)

        self.assertEqual(55 ,self.hero.health)
        self.assertEqual(105 ,self.hero.damage)
        self.assertEqual(2 ,self.hero.level)

        self.assertEqual("You win", result)


    def test_battle_hero_health_drops_below_zero(self):
        self.hero.damage = 120
        self.hero.health = 120

        result = self.enemy.battle(self.hero)

        self.assertEqual(75 ,self.hero.health)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(125, self.hero.damage)

        self.assertEqual(-70, self.enemy.health)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(50, self.enemy.damage)

        self.assertEqual("You lose", result)

    def test_str_method(self):
        self.assertEqual(
            "Hero Hero: 1 lvl\n"
            "Health: 100\n"
            "Damage: 100\n",
            str(self.hero)
        )


if __name__ == "__main__":
    main()