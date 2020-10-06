from flask import Flask, render_template, request, redirect, Blueprint

from models.fixture import Fixture

import repositories.user_repository as user_repository
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

fixtures_blueprint = Blueprint("fixtures", __name__)


# @fixtures_blueprint.route('/fixtures')
# def create_fixtures(teams):

#     teams = []

#     s = []
#     if len(teams) % 2 == 1: teams = teams + [None]
#     n = len(teams)
#     map = list(range(n))
#     mid = n // 2
#     for i in range(n-1):
#         l1 = map[:mid]
#         l2 = map[mid:]
#         l2.reverse()
#         round = []
#         for j in range(mid):
#             t1 = teams[l1[j]]
#             t2 = teams[l2[j]]
#             if j == 0 and i % 2 ==1:
#                 round.append((t2, t1))
#             else:
#                 round.append((t2, t1))
#         s.append(round)

#         map = map[mid:-1] + map[:mid] + map[-1:]
#     return s

#     schedule = create_fixtures(teams)
#     return ("\n".join(["{} vs. {}".format(m[0], m[1])for round in schedule for m in round]))