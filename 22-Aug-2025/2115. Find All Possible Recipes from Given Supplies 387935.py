# Problem: 2115. Find All Possible Recipes from Given Supplies - https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

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
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        