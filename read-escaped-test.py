
import test

script = '/home/codio/workspace/challenge1/read-escaped.py'
inputs = []
expected = [[
  ['Mary\'s, file','one','22'],
  ['Tariq\'s','golden','fleece','2,2']
]]

test.test(script, inputs, expected)

print('Well done')
