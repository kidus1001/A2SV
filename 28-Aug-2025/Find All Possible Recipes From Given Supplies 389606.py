# Problem: Find All Possible Recipes From Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        available = set(supplies)
        needs = {r: ings for r, ings in zip(recipes, ingredients)}

        updated = True
        while updated:
            updated = False
            for r in recipes:
                if r in available:
                    continue
                if all(ing in available for ing in needs[r]):
                    available.add(r)
                    updated = True

        return [r for r in recipes if r in available]