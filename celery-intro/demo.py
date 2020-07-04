from tasks import reverse

r = reverse.delay("Cosmefulanito")

print(r.status)
print(r.get())
print(r.status)
