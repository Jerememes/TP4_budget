import os

bad_hash = 'c1a4be04b972b6c17db242fc37752ad517c29402'
good_hash = 'e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c'

start_status = os.system(f'git bisect start {bad_hash} {good_hash}')
run_status = os.system('git bisect run python manage.py test')
reset_status = os.system('git bisect reset')
