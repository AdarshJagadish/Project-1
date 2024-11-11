import os
if os.path.exists('Vyshak Sir Batch/FileHandling/sample.txt'):
    os.remove('Vyshak Sir Batch/FileHandling/sample.txt')
else:
    print('file not found')