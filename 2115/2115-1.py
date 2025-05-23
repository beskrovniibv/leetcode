#! /usr/bin/env python

from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        result = []
        s = set(supplies)
        rb = [False]*n
        need = True
        while need:
            need = False
            for i in range(n):
                if rb[i]:
                    continue
                r = recipes[i]
                for e in ingredients[i]:
                    if e not in s:
                        break
                else:
                    result.append(r)
                    s.add(r)
                    need = True
                    rb[i] = True
        return result


def main():
    examples = (
        (
            ["bread"], [["yeast", "flour"]], ["yeast", "flour", "corn"], ["bread"]
        ),
        (
            ["bread", "sandwich"], [["yeast", "flour"], ["bread", "meat"]], ["yeast", "flour", "meat"], ["bread", "sandwich"]
        ),
        (
            ["bread", "sandwich", "burger"], [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], ["yeast", "flour", "meat"], ["bread", "sandwich", "burger"]
        ),
    )
    solution = Solution()
    for idx, example in enumerate(examples):
        recipes, ingredients, supplies, expected = example
        got = solution.findAllRecipes(
            recipes=recipes,
            ingredients=ingredients,
            supplies=supplies
        )
        assert got == expected, f"Error in sample {idx + 1}: expected {expected}, got {got}."


if __name__ == "__main__":
    main()
