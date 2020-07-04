from tasks import reverse

r = reverse.delay("Rodrigo")

print(r.status)
print(r.ready())
print(r.get())
print(r.status)
