from .base import *
SECRET_KEY = env('DJANGO_SECRET_KEY', default='y2ngs*q=g_#@@rocqr^ga!-fg()22yrf9mu8hab59j1vmfe&_f')
DEBUG = env.bool('DJANGO_DEBUG', default=True)

