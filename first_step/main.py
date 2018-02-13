from first_step.tasks import add

result = add.delay(4, 4)
print(result.ready())
print(result.get(timeout=1))
print(result.get(propagate=False))
print(result.traceback)