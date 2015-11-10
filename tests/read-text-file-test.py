
import test
script = 'challenges/read-text-file.py';

test.test(script, ['content/textfiles/parrot.txt', 'parrot'], ['3'])
test.test(script, ['content/textfiles/empty.txt', 'parrot'], ['0'])

print('Well done')


